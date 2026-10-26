# Cadastro de Imóveis S6

Skill para o Codex cadastrar, completar e revisar imóveis e condomínios no Tecimob seguindo o padrão da S6 Imóveis.

Inclui pesquisa e confirmação de dados, privacidade da unidade, organização de fotos, descrições e SEO, além da conferência do salvamento. O tratamento fotográfico opcional é convencional e preserva o conteúdo das imagens.

## Instalação no Codex

Copie e cole no Codex do computador em que deseja usar a skill:

```text
Instale a skill cadastro-imovel-s6 deste repositório público:
https://github.com/caprucho/cadastro-imovel-s6

A pasta da skill é skills/cadastro-imovel-s6, na branch main. Use a skill-installer disponível no seu ambiente e instale no diretório pessoal de skills do Codex. Inclua o SKILL.md, agents, references e scripts. Se já existir uma instalação, preserve a versão atual antes de atualizá-la. Confira a instalação e me explique brevemente como usar. Apenas instale; não abra nem altere cadastros no Tecimob agora.
```

Para instalar com o auxiliar oficial `install-skill-from-github.py` da skill-installer:

```text
python <caminho-da-skill-installer>/scripts/install-skill-from-github.py --repo caprucho/cadastro-imovel-s6 --path skills/cadastro-imovel-s6
```

O instalador usa o diretório pessoal de skills configurado no ambiente. A skill fica disponível no próximo turno; se não aparecer, abra uma nova conversa ou reinicie o Codex.

## Como usar

```text
Use $cadastro-imovel-s6 para me ajudar a cadastrar este imóvel no Tecimob. Vou fornecer os dados, as fotos e o corretor responsável. Prepare o cadastro para minha revisão antes de finalizar ou publicar.
```

O computador precisa ter ferramentas de navegação disponíveis no Codex e uma sessão própria autorizada no Tecimob. A instalação não transfere login, cookies, senhas ou acesso à conta de outra pessoa.

O auxiliar opcional de fotos exige Python, Pillow e NumPy; as instruções principais podem ser usadas sem executar esse auxiliar. O pacote contém instruções e código, sem fichas de clientes ou fotos de imóveis.

## Padrões S6

As opções comerciais, os portais, a marca d'água e o vídeo institucional são padrões específicos da S6 descritos na skill. Dados de cada imóvel precisam ser confirmados. O corretor responsável deve ser indicado em cada cadastro. A instalação não autoriza publicação, contato com proprietários ou alterações no CRM.

