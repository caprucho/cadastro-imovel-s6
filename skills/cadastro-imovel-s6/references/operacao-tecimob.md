# Operação do Tecimob e tratamento convencional de fotos

## Navegador e retomada

- Preferir o navegador do Codex, visível para acompanhamento. Usar os controles de navegador disponíveis e a documentação atual da sessão.
- Rotas úteis observadas: `/properties/search`, `/properties/condos`, `/people/show`; novo imóvel parte de `/properties/store`. Confirmar navegação pela interface, sem fixar IDs de abas, índices AX, UUIDs ou referências de imóveis anteriores.
- Ler o estado atual antes de cada sequência. O usuário pode estar editando ao mesmo tempo; evitar sobrescrever campos ou salvar configurações com base em uma captura antiga.
- Após navegação, o formulário pode aparecer temporariamente vazio antes de carregar os dados. Não preencher ou salvar nessa fase. Obter o estado atualizado e verificar valores carregados, evitando também duplicação de clientes/condomínios.
- Se uma aba ficar obsoleta, listar as abas do mesmo navegador e recuperar a adequada. Não criar outro cadastro para resolver um erro de aba.
- Preservar a aba útil usando o mecanismo vigente de entrega/retomada. Não deixar uma etapa não salva desaparecer ao encerrar o turno.

## Sequência funcional

O cadastro observado usa: Informações → Cômodos → Medidas → Preço → Características do Imóvel → Características do Condomínio → Localização → Proximidades → Descrição → Complementos → Dados privativos → Imagens do imóvel → Publicação.

Siga as telas reais, não essa lista como contrato de API. É possível preencher dados confirmados em outras etapas enquanto o usuário responde uma dúvida independente.

Em Localização, a identificação da unidade tem controle específico de exibição. Conferir `Mostrar o número da unidade: Não` e `Mostrar complemento: Não` quando possa expor unidade. Número do prédio e número da unidade são campos diferentes. Não deduzir andar a partir da unidade.

## Editor de descrição: ponto frágil observado

O editor rico usado pelo Tecimob pode reagir de forma diferente a `fill`, digitação, colagem e atalhos. A colagem HTML foi recebida como texto literal/truncado em uma execução; não insistir nessa técnica nem salvar esse conteúdo.

Fluxo que funcionou:

1. Ler e, se necessário, preservar o texto existente em um arquivo local da tarefa antes de substituir.
2. Selecionar apenas o editor correto, selecionar todo seu conteúdo e apagar. Nos condomínios há editores público e privado: não confundi-los.
3. Verificar que o editor ficou vazio. Inserir o texto completo por um método documentado que funcione na sessão. Tópicos com `•` em parágrafos são um fallback legível se a formatação de lista não funcionar.
4. Ler de volta o **texto inteiro**, não só o começo. Conferir que não há HTML literal, trechos antigos duplicados, partes truncadas ou unidade pública.
5. Sair do foco do editor, conferir o estado e só então salvar. A leitura visual do DOM não comprova que o formulário gravará esse texto.
6. Reabrir a etapa, esperar os dados carregarem e comparar texto completo, título e formatação com o que deveria estar salvo. Um toast `Salvo!` sozinho não basta. Se reaparecer vazio, restabelecer o texto, verificar, desfocar e salvar novamente; não prosseguir com descrição apagada.

Usar apenas ações de edição autorizadas/documentadas. Não manipular estado interno da aplicação, fazer requisições privadas descobertas ou injetar HTML no DOM para contornar o editor.

## Salvar e publicar

- As etapas têm `Salvar e Próximo`; o condomínio pode ter `Salvar e Adicionar Fotos`. Rever depois do salvamento.
- A configuração específica de SEO fica em Publicação. `Configurar SEO` pode já estar expandido. Não falhar procurando esse botão quando os campos já estiverem visíveis.
- `Título da página` e `Descrição` de SEO são diferentes do título e texto comercial do imóvel. Conferir ambos. `Modificar URL` não é necessário para editar o texto; manter URL existente.
- Na interface observada, gravar a etapa final/SEO requer `Finalizar`. Se o usuário reservou a publicação/finalização para revisão, preparar tudo e pedir o OK apenas nesse ponto, explicando o efeito do botão. Depois da autorização, finalizar e reabrir para conferir.
- Não supor que configuração de portal equivale a anúncio já integrado. Confirmar o que é observável e relatar eventual sincronização pendente.
- Após publicação, obter o link público por meios visíveis da interface e verificar título, descrição, fotos e unidade oculta. Para SEO, conferir os metadados públicos quando acessíveis, sem prometer atualização imediata do Google.
- Salvar uma captura do resultado relevante e apresentá-la na entrega. Não deixar a ficha interna com dados privados aberta como se fosse prova da ausência desses dados no anúncio público.

## Fotos: helper convencional opcional

`scripts/enhance_photos.py` exige Python, Pillow e NumPy. Localizar o runtime disponível na sessão; não depender de um caminho de Python fixo. Não instalar pacotes sem necessidade.

```text
python enhance_photos.py --input-dir <originais> --output-dir <nova-pasta> [--order-json <ordem.json>]
```

- Lê apenas fotos da pasta indicada, sem recursão. A pasta de saída deve ser nova e diferente da entrada.
- O JSON opcional é uma lista com os nomes dos arquivos, na ordem editorial escolhida. Deve incluir todas as fotos elegíveis, sem duplicações; a ordem alfabética é só o padrão de processamento, não uma escolha editorial.
- Salva cópias numeradas `01-foto.jpg`, etc., e um manifesto de origem, hash e dimensões. Não usa identificadores de unidade nos nomes enviados.
- Aplica exclusivamente uma curva tonal global, monotônica e moderada, ajustada pela luminosidade de cada foto. Não recorta, redimensiona, gira, corrige perspectiva, remove objetos, insere detalhes nem utiliza IA. Preserva orientação EXIF e perfil de cor quando presentes.
- Arquivos JPEG sofrem nova compressão ao salvar: não alegar que todos os pixels são idênticos. A preservação exigida é de conteúdo/enquadramento/dimensões; a luz é a mudança autorizada.
- Inspecionar visualmente as cópias e comparar com os originais. O helper não detecta todas as imagens estouradas, não recupera informação perdida, não garante que cada foto precise de ajuste e não substitui revisão. Se uma foto já estiver adequada, usar a original ou ajustar parâmetros após análise.
- Verificar hashes dos originais e dimensões antes/depois. Nunca enviar folhas de contato como fotos individuais do imóvel. Não enviar o manifesto à galeria.
- Aplicar a marca d’água oficial pelo Tecimob depois do tratamento; confirmar que está legível e aplicada uma única vez. As fotos do condomínio podem aparecer automaticamente depois das fotos do apartamento: conferir a galeria resultante.
