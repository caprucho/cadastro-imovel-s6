---
name: cadastro-imovel-s6
description: "Cadastre ou complete imóveis e condomínios no Tecimob para a S6 Imóveis, pesquisando e confirmando dados, organizando fotos e descrições com SEO e verificando o salvamento. Use também para revisar esses cadastros conforme o padrão da S6."
---

# Cadastro de Imóveis S6

Cadastre o imóvel correto, vinculado ao condomínio correto, com informações verificáveis e texto complementar ao anúncio. Trabalhe em português e no navegador do Codex, deixando a execução visível para o usuário acompanhar. Reutilize a sessão existente e respeite os campos que ele já preencheu.

## Escopo e decisões

- Considere as instruções mais recentes do usuário e as autorizações já dadas. Não refaça perguntas respondidas.
- Se o usuário estiver preenchendo parte do cadastro, confira o estado atual antes de prosseguir. Não crie um segundo imóvel ao retomar.
- Pergunte diante de qualquer dúvida real sobre dados ou escolhas do cadastro, mesmo pequena. Agrupe perguntas relacionadas e prossiga apenas com o trabalho independente das respostas.
- Não transforme os dados de um imóvel anterior em padrão: preços, metragem, IPTU, cômodos, mobília, origem da captação, unidade, existência de depósito e características construtivas são específicos.
- A skill não autoriza mensagens ao proprietário, contato com anunciantes, compra de imagens, mudanças de plano, exclusão de arquivos ou publicação não solicitada.

## Pesquisa e confirmação de dados

Antes de preencher informações pesquisadas, leia [references/pesquisa-e-confirmacao.md](references/pesquisa-e-confirmacao.md). Use esse procedimento tanto para o imóvel quanto para o condomínio e seu entorno.

1. Separe dados do proprietário, dados do apartamento e dados do condomínio. Identifique a origem de cada informação relevante.
2. Confira endereço completo, identidade do empreendimento e, privadamente, a unidade. O nome parecido de outro prédio não é evidência.
3. Pesquise as lacunas em fontes adequadas: documentos e proprietário para dados da unidade; fontes oficiais para instituições, transporte e endereços; anúncios do mesmo condomínio para corroborar sua estrutura.
4. Diferencie confirmado, corroborado por anúncios, inferido e pendente. Anúncios repetidos não são fontes independentes. Não preencha campos com palpites.
5. Exponha divergências de forma objetiva e consulte o usuário quando necessário. Não deixe um campo padrão do sistema virar uma afirmação falsa por falta de revisão.

Os padrões do usuário abaixo orientam o preenchimento; **não são prova externa** da existência de uma instalação. Se a pesquisa ou o contexto os contradisser, mostre o conflito e peça orientação antes de marcar ou divulgar a informação.

## Proprietário, informações e privacidade

- Cadastre o cliente somente com seu nome. Remova identificadores da agenda, como `pp` (proprietário), número da unidade e nome do prédio. Preserve o telefone correto e pesquise nome e telefone antes de criar um cliente para evitar duplicidade.
- Origem da captação: perguntar se não informada; `Indicação` foi uma escolha de um caso, não um padrão geral.
- Corretor responsável: usar o profissional indicado pelo usuário para esse cadastro; se não informado, perguntar. Não presumir que a pessoa operando o Codex seja o corretor responsável.
- Código de referência: deixar o sistema gerar; não inventar, forçar sequência nem apagar o código gerado automaticamente.
- **Nunca exibir o número da unidade em nenhuma parte pública do anúncio.** Use apenas o campo próprio com a opção de exibição desativada ou um campo explicitamente privado. Não inserir em título, descrição, complemento público, legenda, texto de SEO ou nomes de arquivos enviados. Não confundir número da unidade com número do prédio.
- Conferir as opções de mostrar unidade, andar e complemento. Ao publicar, verificar também a página pública e as informações destinadas aos portais; a ficha interna pode mostrar dados privados legitimamente.
- CPF, matrícula, averbação, quitação, orientação solar, andar e outras informações não fornecidas não devem ser inventados. `Escriturado` só quando informado/confirmado; não o generalizar da escolha feita em um cadastro anterior.

## Condomínio antes do apartamento

- Pesquise se o condomínio já existe. Se não existir, cadastre-o antes de vincular o apartamento.
- Mantenha nesse cadastro a descrição de lazer, portaria, gerador, elevadores, áreas comuns e serviços. Não repetir essa descrição no texto do apartamento.
- A descrição privada do condomínio deve ficar vazia, salvo nova instrução explícita. Evidências de pesquisa ficam em notas locais da tarefa, não nesse campo.
- Padrões solicitados para características: permite animais, bicicletário, elevador social e de serviço. Jardim quando confirmado, inclusive por foto. Não inventar contagens de elevadores.
- Academia nova, salão novo, portaria blindada e atendimento presencial 24h devem vir de informação específica confirmada. Ter piscina não confirma aquecimento nem funcionamento atual.
- Confira se o Tecimob herdou as características e fotos corretas no imóvel vinculado. Salvar o condomínio pode oferecer propagação aos imóveis ligados: não marcar propagação ampla sem necessidade/autorização.

## Cômodos, medidas e condições

- Confirme dormitórios, suítes, banheiros, lavabo e cada tipo de sala. Não contar cômodos distintos apenas pelo número de fotos nem importar quantidades de outro apartamento do prédio.
- Esclareça se lavabo e banheiro de serviço estão incluídos no total de banheiros quando houver ambiguidade.
- Registre área útil no campo de área privativa correspondente; não copiar esse valor para área total ou construída sem confirmação.
- Confirme quantidade, cobertura e condição das vagas; `escrituradas` não significa vagas livres, fixas ou independentes.
- Havendo depósito confirmado, o padrão informado pelo usuário é depósito na garagem. Não marcar depósito em um imóvel sem saber se existe; não confundir depósito com vaga/box sem conferir o significado do campo.
- Padrões comerciais do usuário: **aceita financiamento: Sim; aceita permuta: Não**. Não confundir aceitar financiamento com o imóvel estar financiado.
- IPTU: conferir valor e periodicidade em cada caso. Comparações com outras unidades corroboram a periodicidade, mas não comprovam o débito da unidade. Não converter valores entre mensal/anual ou multiplicar parcelas sem base.
- Mobília: seguir a escolha explícita do usuário e descrever exatamente o que está incluído. Armários planejados não autorizam afirmar que sofá, camas, eletrodomésticos ou todos os objetos das fotos acompanham a venda. A opção `Mobiliado` com apenas armários incluídos foi uma decisão específica; não a aplicar automaticamente em outros imóveis.

## Proximidades do imóvel e do condomínio

- Conferir e marcar nos dois cadastros: academias, farmácias, supermercados, restaurantes, padarias, escolas, faculdades, praças, principais avenidas e comércio local relevante.
- Priorizar estações de metrô, shoppings, hospitais e principais vias com nomes próprios quando disponíveis. Pesquisar o entorno de fato, sem assumir estabelecimentos só porque são comuns no bairro.
- Pesquisar **todas as faculdades e polos de ensino superior identificáveis em raio de até 1 km**, distinguir campus presencial de polo EAD e evitar duplicar faculdades da mesma instituição no mesmo campus. Usar raio em linha reta; não apresentar como trajeto a pé. Se a pesquisa não for exaustiva, informar a cobertura e pendências.
- Marcar os shoppings próximos e as avenidas pertinentes, sem incluir todo o catálogo da cidade. Se distância ou relevância de uma referência limítrofe for incerta, perguntar.
- Não cadastrar uma academia como faculdade por erro de categoria de mapas ou portais. Revalidar endereços e operação de instituições/estações quando necessário.

## Fotos e vídeo

- Preservar os originais. Fazer inventário e inspeção visual antes do upload; conferir se as imagens pertencem ao imóvel/condomínio correto e se não expõem a unidade.
- Para fotos obtidas na internet: confirmar o prédio, verificar marca d’água/créditos e condições de uso; salvar candidatas separadamente e **obter aprovação do usuário antes de enviar**. Ausência de marca d’água não comprova licença de uso. Não remover ou esconder marcas.
- Quando solicitado tratamento, fazer somente enhancement fotográfico convencional: exposição, sombras, realces e contraste moderados. **Nunca alterar conteúdo, enquadramento, dimensões, proporção, arquitetura, móveis, materiais ou vistas; nunca inventar detalhes.** Não usar geração, preenchimento generativo, troca de céu ou decoração virtual nesse tratamento.
- O usuário escolheu processamento local convencional para essa finalidade. O auxiliar opcional [scripts/enhance_photos.py](scripts/enhance_photos.py) implementa esse fluxo com Pillow e NumPy; leia `--help` e a seção de fotos da [referência operacional](references/operacao-tecimob.md) antes de executar. Se ferramentas/instruções vigentes exigirem outro método, esclarecer a limitação em vez de substituir por IA generativa.
- Ajustar cada foto conforme a necessidade e revisar o resultado: evitar brancos estourados, excesso de contraste e aspecto artificial. Realces já sem informação não podem ser reconstruídos como se fossem detalhes reais.
- **Sempre aplicar a marca d’água da S6 pelo Tecimob, por padrão**, verificando o resultado. Para uma galeria já aprovada sem marca, não alterá-la retroativamente fora da tarefa. Não aplicar duas vezes.
- Ordenar por uma visita coerente: melhor foto da área social como capa, demais áreas sociais/varanda, área íntima e banheiros, cozinha e serviço. Ajustar conforme o imóvel; confirmar a ordem persistida, não presumir que o upload a manteve. Fotos do condomínio podem ser acrescentadas automaticamente ao final.
- Em `Complementos → Vídeo`, se não houver vídeo específico do imóvel, usar o vídeo institucional genérico: `https://www.youtube.com/shorts/Kf3iJlMCKnQ`. Não substituir um vídeo específico existente sem orientação. Não apresentar o institucional como filmagem do apartamento.

## Texto e SEO

- Descrição do apartamento é um complemento ao anúncio: **não mencionar valores de venda, aluguel, condomínio ou IPTU**. Não repetir detalhes de lazer/estrutura do condomínio.
- Escrever de forma profissional, objetiva e específica, no padrão editorial dos grandes portais: abertura com atributos relevantes, benefícios sustentados pelos ambientes reais, listas dos destaques, breve localização e convite para visita. Não copiar textos de concorrentes nem usar superlativos vazios ou promessas de valorização.
- Usar tópicos para informações importantes e títulos curtos de seção. Evitar blocos longos, repetição e excesso de palavras-chave. Manter apenas fatos confirmados e preservar a unidade oculta.
- Título: tipo + intenção (venda/locação) + bairro + diferenciais principais. Exemplo abstrato: `Apartamento à venda em [bairro]: [área] m², [n] suítes e [n] vagas`. Adaptar ao caso, sem carregar colchetes nem afirmar suítes inexistentes.
- Abertura e meta descrição: mencionar naturalmente tipo, transação, bairro/cidade e diferenciais. Preencher também `Publicação → Configurar SEO` quando disponível. Não usar preços ou unidade. Preservar a URL existente, salvo pedido para alterá-la.
- Título e meta descrição devem ser claros e concisos; não prometer posição no Google nem tratar limites aproximados de caracteres como garantia de exibição.

## Revisão, publicação e entrega

Leia [references/operacao-tecimob.md](references/operacao-tecimob.md) ao executar o cadastro no navegador, especialmente a gravação do editor rico e a conferência de publicação.

- Portais padrão acordados: **Chaves na Mão: Padrão; comprealugueagora: Padrão; ImovelWeb: Simples**. As cotas variam: conferir a tela, não fixar números de uso. Outros portais, como Guru, seguem a configuração existente; não adicionar/remover nem comprar destaque por inferência.
- Não ativar lembretes ou mensagens automáticas ao proprietário sem instrução específica. A referência de vídeo não autoriza contato externo.
- Quando o usuário quiser revisar primeiro, concluir tudo que for possível, deixar a prévia concreta aberta e aguardar seu OK antes de `Finalizar`. Se `Finalizar` também for necessário para salvar SEO, explicar isso e apresentar os campos preparados. Depois do OK, executar sem pedir a mesma confirmação outra vez.
- Se o cadastro já aparecer publicado ao retomar, não alegar que está em rascunho. Conferir o estado atual antes de qualquer ação e não atribuir a si mudanças feitas pelo usuário.
- Reabrir/recarregar após salvar e comparar os dados efetivamente gravados, incluindo texto inteiro, galeria e privacidade. Verificar a página pública quando houver publicação; distinguir configuração salva no Tecimob de integração concluída nos portais e indexação pelo Google.
- Entregar um resumo do que foi salvo, confirmação visual e pendências concretas. Manter a tela útil aberta para o usuário continuar. Não declarar cadastro/publicação concluídos com campos ou verificações necessários pendentes.
