# Visão do Projeto

## Objetivo

Definir a fantasia principal, proposta de valor, pilares de design e experiência desejada do TBH2.

Este documento possui prioridade máxima sobre toda a documentação do projeto.

Quando houver conflito entre sistemas, mecânicas, funcionalidades ou decisões técnicas, a Visão do Projeto deve prevalecer.

A visão responde à pergunta:

> "Que experiência o TBH2 precisa entregar?"

---

## Status

In Progress

---

## Dependências

Este documento orienta todos os demais.

Documentos diretamente derivados:

* [Gameplay central](01_CORE_GAMEPLAY.md)
* [Progressão](02_PROGRESSION.md)
* [Combate](03_COMBAT.md)
* [Loot e economia](04_LOOT_ECONOMY.md)
* [UI e UX](05_UI_UX.md)
* [Identidade de Taskbar](../taskbar/01_TASKBAR_IDENTITY.md)
* [Roadmap](../technical/04_ROADMAP.md)

---

# Visão Geral

TBH2 é um Idle RPG Companion executado na lateral da área de trabalho.

O jogador acompanha a jornada de um aventureiro que continua explorando, combatendo, encontrando recompensas e evoluindo enquanto o usuário trabalha, estuda ou utiliza o computador.

O personagem não é apenas um conjunto de números.

Ele representa um aventureiro em uma jornada contínua.

A experiência central do jogo é observar essa jornada acontecer em segundo plano, com retornos ocasionais para tomar decisões importantes.

---

# Fantasia Principal

A fantasia principal do TBH2 é:

> "Meu aventureiro continua sua jornada mesmo quando minha atenção está em outro lugar."

Essa fantasia deve orientar todos os sistemas.

O jogador deve sentir que existe um pequeno mundo vivo acontecendo ao lado dele.

Mesmo quando não está interagindo, o aventureiro deve parecer ativo.

---

# Proposta de Valor

TBH2 não busca competir com RPGs tradicionais.

O objetivo não é exigir atenção constante.

O objetivo é oferecer uma experiência persistente, compacta e contínua.

Enquanto RPGs tradicionais exigem foco total, o TBH2 existe ao lado do usuário.

O jogo acompanha a rotina do jogador.

Ele ocupa um pequeno espaço da tela e transmite a sensação de que existe uma jornada em andamento.

O valor do TBH2 está em:

* progressão contínua;
* baixa necessidade de interação;
* sensação de companhia;
* evolução de longo prazo;
* observação da jornada;
* recompensas frequentes;
* decisões ocasionais de build.

---

# O Que Torna o TBH2 Único

A maioria dos Idle RPGs apresenta principalmente números, menus e barras de progresso.

O TBH2 busca mostrar a jornada.

O jogador deve ver:

* exploração;
* encontros;
* combates;
* recompensas;
* chefes;
* regiões;
* progressão visual;
* evolução do aventureiro.

O mundo existe visualmente.

O aventureiro está sempre fazendo algo.

A diferença central não é apenas ser idle.

A diferença é ser um RPG idle com presença visual contínua na área de trabalho.

---

# Pilares de Design

Toda decisão de desenvolvimento deve respeitar estes pilares.

---

## 1. Jornada Contínua

O personagem deve estar sempre avançando.

O jogador deve sentir movimento constante.

Exploração é tão importante quanto combate.

O mundo não deve parecer uma tela parada esperando cliques.

---

## 2. Progressão Significativa

Toda recompensa deve possuir valor.

Subir de nível deve importar.

Encontrar equipamentos deve importar.

Derrotar chefes deve importar.

Avançar mapas deve importar.

Nenhum sistema deve gerar progresso vazio.

---

## 3. Preparação Acima de Execução

O jogador é um preparador de build.

Não um executor de ações manuais.

As decisões importantes acontecem fora do combate.

Exemplos:

* equipamentos;
* atributos;
* classe;
* habilidades futuras;
* build;
* avanço de mapas;
* preparação para chefes.

O combate valida decisões tomadas anteriormente.

O jogador não escolhe um modo agressivo, balanceado ou defensivo.

O jogador constrói uma build que pode se tornar agressiva, defensiva, rápida, resistente, mágica ou sustentável.

---

## 4. Mundo Vivo

O mundo deve parecer habitado.

Mesmo quando nada importante acontece, a cena deve transmitir presença.

Elementos visuais devem sugerir:

* viagem;
* descoberta;
* ambientação;
* perigo;
* identidade regional.

A exploração deve reforçar a sensação de jornada.

---

## 5. Longo Prazo

O TBH2 deve funcionar por:

* horas;
* dias;
* semanas;
* meses.

A progressão deve suportar crescimento prolongado.

O jogador deve sempre possuir algum objetivo relevante.

---

# Experiência Desejada

## Primeiros Minutos

O jogador deve compreender rapidamente:

* quem é seu personagem;
* onde ele está;
* como o combate funciona;
* como recompensas aparecem;
* como o herói evolui;
* qual é o próximo objetivo.

A experiência inicial deve ser simples e clara.

---

## Primeiras Horas

O jogador deve:

* explorar novos mapas;
* encontrar equipamentos;
* perceber evolução;
* derrotar primeiros chefes;
* entender o valor do loot;
* notar que o mundo está avançando.

A progressão deve ser constante.

---

## Longo Prazo

O jogador deve possuir sempre um objetivo.

Exemplos:

* próximo mapa;
* próximo chefe;
* próxima dificuldade;
* próximo equipamento;
* próxima melhoria de build;
* próximo marco de poder.

Nunca deve existir sensação prolongada de estagnação.

Quando uma camada desacelera, outra deve sustentar o interesse.

---

# Estrutura Conceitual do Projeto

A visão do TBH2 é sustentada pelas seguintes camadas:

```text
Gameplay Central
↓
Progressão
↓
Combate
↓
Loot e Equipamentos
↓
Atributos
↓
Classes
↓
Habilidades
↓
Conteúdo
↓
Sistemas Futuros
```

Cada camada existe para reforçar a jornada do aventureiro.

Nenhuma camada deve existir apenas por acúmulo de complexidade.

---

# Regras Não Negociáveis

## O Combate Continuará Automático

O foco do jogo não é execução mecânica.

O foco é preparação, progressão e build.

---

## O Jogador Não Deve Precisar de Atenção Constante

TBH2 deve respeitar o conceito de Idle Companion.

O jogo deve funcionar bem com atenção periférica.

---

## Progressão Deve Ser Mais Importante que Microgerenciamento

A evolução do personagem é o centro da experiência.

Interações devem ser relevantes, não repetitivas.

---

## O Mundo Deve Ser Visível

O jogador deve observar a jornada.

Não apenas menus, números ou barras.

---

## A Build Define o Estilo de Combate

O projeto não deve depender de modos manuais como:

* agressivo;
* balanceado;
* defensivo.

O estilo emerge da combinação entre:

* equipamentos;
* atributos;
* classe;
* habilidades;
* efeitos especiais;
* sinergias.

---

## Toda Nova Funcionalidade Deve Reforçar a Fantasia Principal

Pergunta obrigatória antes de qualquer implementação:

> "Esta funcionalidade faz o jogador sentir que está acompanhando a jornada de um aventureiro?"

Se a resposta for não, a funcionalidade deve ser reavaliada.

---

# O Que TBH2 Não É

TBH2 não é:

* Action RPG;
* MMORPG;
* Clicker Game;
* Incremental puro;
* jogo de microgerenciamento constante;
* chatbot;
* ferramenta de produtividade;
* simulador passivo sem decisões.

O jogador deve tomar decisões relevantes.

Mas não deve precisar executar ações repetitivas constantemente.

---

# Indicadores de Sucesso

O TBH2 será considerado bem-sucedido quando o jogador:

* deixar o jogo aberto por longos períodos;
* entender o estado da jornada com olhares rápidos;
* retornar frequentemente para verificar progresso;
* sentir apego ao personagem;
* perceber evolução constante;
* encontrar recompensas significativas;
* possuir objetivos de curto, médio e longo prazo;
* sentir que o mundo continua existindo mesmo com pouca interação.

O sucesso do TBH2 não será medido pela quantidade de sistemas.

Será medido pela qualidade da jornada que o jogador acompanha.

---

# Regras

* A visão do projeto prevalece sobre sistemas específicos.
* O jogo deve permanecer compatível com baixa frequência de interação.
* A jornada visual é parte central da proposta.
* Progressão vazia deve ser evitada.
* Sistemas novos devem reforçar o loop principal.
* Complexidade só deve ser adicionada quando gerar decisão real.
* Build substitui modos manuais de combate.
* Taskbar Companion é identidade central, não detalhe de interface.

---

# Histórico de Alterações

* 2026-06-10: documento de visão criado.
* 2026-06-10: fantasia principal consolidada.
* 2026-06-10: pilares de design registrados.
* 2026-06-10: visão reestruturada para reforçar build acima de modos manuais.
* 2026-06-10: adicionada distinção entre visão, gameplay e sistemas específicos.
