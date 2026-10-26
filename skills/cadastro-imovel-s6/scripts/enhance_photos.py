#!/usr/bin/env python3
"""Conservative tonal enhancement of listing photos; never modifies originals."""
import argparse
import hashlib
import json
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input-dir', type=Path, required=True)
    parser.add_argument('--output-dir', type=Path, required=True,
                        help='New directory for copies and manifest; must not exist.')
    parser.add_argument('--order-json', type=Path,
                        help='JSON list of all source basenames, in editorial order.')
    parser.add_argument('--target-median', type=float, default=.48,
                        help='Moderate target median in sRGB, default 0.48.')
    parser.add_argument('--max-lift', type=float, default=.85,
                        help='Maximum shadow/midtone curve coefficient (0 to 1).')
    return parser.parse_args()


def main():
    args = parse_args()
    try:
        import numpy as np
        from PIL import Image
    except ImportError as exc:
        raise SystemExit('Requires Pillow and NumPy in the selected Python runtime.') from exc
    if not .25 <= args.target_median <= .65 or not 0 <= args.max_lift <= 1:
        raise SystemExit('Use target-median 0.25..0.65 and max-lift 0..1.')
    source_dir = args.input_dir.resolve(strict=True)
    destination = args.output_dir.resolve()
    if not source_dir.is_dir() or destination == source_dir or destination.exists():
        raise SystemExit('Input must be a directory; output must be a new, different path.')
    extensions = {'.jpg', '.jpeg', '.png', '.webp'}
    sources = sorted(p for p in source_dir.iterdir()
                     if p.is_file() and p.suffix.lower() in extensions)
    if not sources:
        raise SystemExit('No supported photos in input directory (non-recursive).')
    if args.order_json:
        order = json.loads(args.order_json.read_text(encoding='utf-8-sig'))
        if (not isinstance(order, list) or not all(isinstance(n, str) for n in order)
                or len(order) != len(set(order))
                or set(order) != {p.name for p in sources}):
            raise SystemExit('Order JSON must contain each source basename exactly once.')
        sources = [source_dir / name for name in order]
    # Refuse inputs whose conversion would lose transparency or multiple frames.
    for path in sources:
        with Image.open(path) as photo:
            if 'A' in photo.getbands() or 'transparency' in photo.info:
                raise SystemExit(f'Transparent input requires separate handling: {path.name}')
            if getattr(photo, 'n_frames', 1) != 1:
                raise SystemExit(f'Animated input requires separate handling: {path.name}')
    destination.mkdir(parents=True, exist_ok=False)
    records = []
    x = np.arange(256, dtype=np.float64) / 255
    for index, path in enumerate(sources, 1):
        original_hash = hashlib.sha256(path.read_bytes()).hexdigest()
        with Image.open(path) as original:
            original_size = original.size
            exif = original.getexif()
            orientation = exif.get(274, 1)
            rgb = original.convert('RGB')
            values = np.asarray(rgb, dtype=np.float32) / 255
            luminance = values @ np.array([.2126, .7152, .0722], dtype=np.float32)
            median = float(np.median(luminance))
            near_white = float(np.mean(luminance > .95))
            delta = args.target_median - median
            strength = 0.0 if abs(delta) < .03 else float(np.clip(
                delta / max(median * (1-median)**2, .04), -.35, args.max_lift))
            compress = .10 if near_white > .03 or median > .65 else 0.0
            curve = x + strength*x*(1-x)**2 - compress*x**5*(1-x)
            lut = np.rint(np.clip(curve, 0, 1)*255).astype(np.uint8)
            if not np.all(lut[1:] >= lut[:-1]):
                raise RuntimeError('Non-monotonic curve rejected.')
            enhanced = rgb.point(lut.tolist()*3)
            if enhanced.size != original_size:
                raise RuntimeError('Image dimension change rejected.')
            output = destination / f'{index:02d}-foto.jpg'
            options = dict(quality=96, subsampling=0, exif=exif)
            if original.info.get('icc_profile'):
                options['icc_profile'] = original.info['icc_profile']
            enhanced.save(output, **options)
        with Image.open(output) as check:
            if check.size != original_size or check.getexif().get(274, 1) != orientation:
                raise RuntimeError(f'Dimensions/orientation check failed: {output.name}')
        if hashlib.sha256(path.read_bytes()).hexdigest() != original_hash:
            raise RuntimeError(f'Source modification detected: {path.name}')
        records.append(dict(source=str(path), output=str(output), order=index,
                            source_sha256=original_hash, dimensions=list(original_size),
                            exif_orientation=orientation,
                            median_luminance=round(median, 4),
                            near_white_fraction=round(near_white, 4),
                            tone_coefficient=round(strength, 4),
                            highlight_compression=compress))
    (destination / 'manifest.json').write_text(
        json.dumps(records, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f'{len(records)} copies saved. Originals unchanged; dimensions/orientation verified.')
    print(f'Output: {destination}')


if __name__ == '__main__':
    main()
