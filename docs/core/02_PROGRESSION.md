# Progressão

## Objetivo

Definir os princípios, camadas e ritmo de progressão do TBH2.

Este documento descreve como o jogador deve perceber evolução ao longo do tempo.

Ele não define fórmulas finais, habilidades específicas, listas de itens, chefes específicos ou valores numéricos definitivos.

A progressão deve responder à pergunta:

> "O que faz o jogador sentir que avançou?"

---

## Status

In Progress

---

## Dependências

* [Gameplay central](01_CORE_GAMEPLAY.md)
* [Combate](03_COMBAT.md)
* [Loot e economia](04_LOOT_ECONOMY.md)
* [Sistema de itens](../items/01_ITEM_SYSTEM.md)
* [Sistema de herói](../heroes/01_HERO_SYSTEM.md)
* [Estrutura do mundo](../maps/01_WORLD_STRUCTURE.md)
* [Dificuldades](../maps/05_DIFFICULTIES.md)
* [Fórmulas de balanceamento](../technical/03_BALANCE_FORMULAS.md)

---

# Escopo deste Documento

Este documento define:

* filosofia de progressão;
* ritmo de evolução;
* função dos níveis;
* função dos mapas;
* função dos atos;
* função das dificuldades;
* horizontes de curto, médio e longo prazo;
* relação entre nível, equipamento, atributos, classe e habilidades;
* critérios de validação da progressão.

---

# Fora do Escopo

Este documento não deve definir:

* fórmulas finais de XP;
* fórmulas finais de HP, dano ou defesa;
* lista completa de habilidades;
* cooldowns de habilidades;
* lista completa de itens;
* afixos;
* raridades detalhadas;
* chefes específicos;
* tabelas de loot;
* valores finais de ouro;
* implementação técnica.

Esses assuntos pertencem aos documentos proprietários de cada domínio.

---

# Visão Geral

TBH2 é um Idle RPG Companion.

A progressão deve ser:

* perceptível;
* recompensadora;
* escalável;
* duradoura;
* compatível com baixa frequência de interação.

O jogador deve sentir evolução constante sem precisar controlar cada ação do personagem.

A progressão ideal acontece quando o jogador sempre possui algo a perseguir.

---

# Filosofia de Progressão

A progressão do TBH2 deve funcionar em múltiplas camadas.

O jogador não deve depender apenas do próximo nível para sentir evolução.

Quando uma camada desacelera, outra deve assumir importância.

Exemplo:

* se o próximo nível demora, o jogador busca um item melhor;
* se o item não aparece, o jogador tenta avançar mapa;
* se o mapa trava, o jogador melhora a build;
* se o chefe bloqueia, o jogador farma e retorna mais forte.

A progressão saudável mantém o jogador em movimento.

---

# Princípios Fundamentais

## 1. O Início Deve Ser Rápido

Os primeiros níveis funcionam como tutorial.

Objetivos:

* apresentar exploração;
* apresentar combate;
* apresentar loot;
* apresentar equipamentos;
* apresentar progressão de mapas.

O jogador deve sentir crescimento imediato.

---

## 2. A Progressão Deve Desacelerar Gradualmente

A velocidade de progressão deve diminuir conforme o personagem evolui.

O jogador não deve alcançar níveis altos em poucos minutos.

A desaceleração deve ser natural, não frustrante.

---

## 3. O Poder Deve Continuar Crescendo

Mesmo quando subir de nível demora mais, o jogador deve encontrar outras formas de progresso.

Exemplos:

* item melhor;
* novo mapa;
* nova raridade;
* melhoria de build;
* novo chefe;
* nova dificuldade.

---

## 4. O Mapa é Progresso

O nível não é o único indicador de evolução.

No TBH2, mapas representam a jornada física do aventureiro pelo mundo.

Enquanto níveis representam experiência acumulada, mapas representam conquista, exploração e acesso a novos desafios.

Um personagem de mesmo nível pode estar em mapas diferentes dependendo de:

* equipamentos;
* eficiência da build;
* dificuldade escolhida;
* tempo investido;
* sorte no loot.

O jogador deve sentir orgulho tanto ao subir de nível quanto ao conquistar uma nova região.

---

## 5. A Progressão Deve Gerar Objetivos Constantes

O jogador deve possuir simultaneamente:

* objetivo imediato;
* objetivo de sessão;
* objetivo de longo prazo.

A ausência de objetivo é sinal de falha na progressão.

---

# Loop de Progressão

A progressão acompanha o loop central do jogo:

Exploração
↓
Encontro
↓
Combate
↓
Recompensa
↓
Progressão
↓
Exploração

Cada ciclo deve gerar alguma forma de avanço, mesmo que pequena.

---

# Estrutura de Níveis

A progressão de níveis define a velocidade com que o personagem ganha experiência e crescimento base.

Ela deve ser rápida no início e desacelerar conforme o personagem se torna mais poderoso.

---

## Tutorial — Níveis 1 a 10

## Objetivo

Apresentar os sistemas fundamentais.

O jogador aprende:

* exploração;
* combate;
* loot;
* equipamentos;
* progressão de mapas.

## Características

* level up frequente;
* recompensas constantes;
* baixa exigência de otimização;
* primeiros equipamentos relevantes.

## Sensação desejada

> "Estou ficando mais forte rapidamente."

---

## Early Game — Níveis 11 a 20

## Objetivo

Consolidar o aprendizado.

O jogador começa a perceber que equipamentos possuem impacto real.

## Características

* progressão moderada;
* primeiros gargalos leves;
* maior atenção ao loot;
* primeiros sinais de build.

## Sensação desejada

> "Agora preciso melhorar meu personagem para avançar."

---

## Mid Game — Níveis 21 a 50

## Objetivo

Introduzir otimização.

O jogador deixa de depender apenas do nível.

Equipamentos passam a ter impacto maior.

## Características

* progressão mais lenta;
* chefes mais relevantes;
* necessidade crescente de equipamentos melhores;
* primeiras decisões claras de build.

## Sensação desejada

> "Preciso encontrar itens melhores."

---

## Late Game — Níveis 51 a 100

## Objetivo

Criar metas de longo prazo.

O personagem já possui identidade mais definida.

## Características

* progressão lenta;
* dependência forte de equipamentos;
* preparação para dificuldades superiores;
* busca por sinergias.

## Sensação desejada

> "Meu personagem está entrando em um novo patamar."

---

## Endgame — Nível 100+

## Objetivo

Manter o jogo vivo após a progressão principal.

A progressão deixa de depender principalmente de nível e passa a depender de otimização.

## Foco

* equipamentos raros;
* builds especializadas;
* dificuldades superiores;
* farm direcionado;
* chefes avançados;
* conteúdo repetível futuro.

## Sensação desejada

> "Ainda posso melhorar."

---

# Progressão por Mapas

Cada ato é composto por dez mapas.

Os mapas possuem identidade própria e representam regiões distintas do mundo.

Mapas não são apenas cenários.

Eles são etapas da jornada.

---

## Mapas 1 a 9

## Função

* exploração;
* farm;
* obtenção de ouro;
* obtenção de equipamentos;
* preparação para o chefe;
* avanço gradual de dificuldade.

Cada mapa deve possuir:

* tema visual próprio;
* inimigos próprios;
* ambientação própria;
* ritmo próprio;
* aumento gradual de desafio.

O jogador deve perceber que está atravessando uma região real.

---

## Mapa 10

## Função

Chefe do ato.

Todo mapa 10 deve representar o fechamento de um capítulo.

Deve conter:

* chefe único;
* maior dificuldade do ato;
* recompensa superior;
* bloqueio de avanço;
* sensação de conquista.

Se o jogador não consegue derrotar o chefe, provavelmente precisa:

* subir níveis;
* melhorar equipamentos;
* revisar atributos;
* otimizar build;
* farmar mapas anteriores.

## Sensação desejada

> "Conquistei esta região."

---

# Progressão por Atos

Atos representam capítulos maiores da campanha.

Cada ato deve possuir:

* tema visual próprio;
* identidade de monstros;
* curva de dificuldade;
* chefe final;
* recompensas compatíveis;
* sensação de avanço de mundo.

A progressão por atos deve fazer o jogador sentir que saiu de uma região e entrou em outra etapa da jornada.

---

# Progressão por Dificuldades

Dificuldades representam novos ciclos de progressão.

Elas não devem servir apenas para aumentar números.

Ao avançar de dificuldade, o jogador revisita conteúdos anteriores sob maior ameaça e com melhores recompensas.

Dificuldades previstas:

* Normal;
* Veterano;
* Pesadelo;
* Infernal.

As regras detalhadas pertencem ao documento:

* [Dificuldades](../maps/05_DIFFICULTIES.md)

---

# Progressão em Camadas

O TBH2 deve operar em três horizontes de recompensa.

---

## Curto Prazo

Recompensas percebidas em minutos.

## Objetivo

Manter o jogador engajado durante a sessão atual.

## Exemplos

* próximo combate vencido;
* próximo item;
* próximo upgrade;
* próxima raridade;
* próximo nível;
* próximo progresso de mapa.

## Sensação desejada

> "Algo está acontecendo."

---

## Médio Prazo

Recompensas percebidas em horas.

## Objetivo

Criar metas claras de avanço.

## Exemplos

* concluir um mapa;
* derrotar um chefe;
* completar um ato;
* desbloquear nova região;
* alcançar novo marco de poder.

## Sensação desejada

> "Estou avançando."

---

## Longo Prazo

Recompensas percebidas em dias ou semanas.

## Objetivo

Manter o jogo relevante por longos períodos.

## Exemplos

* desbloquear nova dificuldade;
* completar uma build;
* encontrar equipamentos raros;
* otimizar atributos;
* superar chefes avançados;
* preparar conteúdo futuro de endgame.

## Sensação desejada

> "Meu personagem está evoluindo continuamente."

---

# Fontes de Poder

O poder do personagem deve crescer por múltiplas camadas.

Nenhuma camada deve substituir completamente as demais.

---

## Nível

## Função

Crescimento constante.

O nível representa experiência acumulada.

Deve fornecer:

* aumento base de poder;
* sensação de continuidade;
* referência de maturidade do personagem;
* acesso futuro a conteúdos.

O nível não deve ser a principal fonte de poder.

## Sensação desejada

> "Meu personagem está ficando mais experiente."

---

## Equipamentos

## Função

Principal fonte de poder.

Equipamentos devem representar os maiores saltos de força do personagem.

Um item relevante deve poder gerar mais impacto do que vários níveis consecutivos.

Equipamentos devem permitir:

* aumento de poder;
* especialização;
* melhoria de build;
* busca constante por upgrades.

As regras detalhadas pertencem ao documento:

* [Sistema de itens](../items/01_ITEM_SYSTEM.md)

## Sensação desejada

> "Encontrei algo que realmente deixou meu personagem mais forte."

---

## Atributos

## Função

Especialização.

Atributos definem como o personagem cresce.

Todos os personagens possuem:

* STR;
* DEX;
* INT;
* CON.

Os detalhes pertencem ao documento:

* [Atributos](../heroes/03_ATTRIBUTES.md)

## Sensação desejada

> "Estou moldando meu personagem."

---

## Classe

## Função

Identidade.

A classe determina o estilo geral do personagem.

Ela influencia:

* atributos prioritários;
* equipamentos desejados;
* habilidades disponíveis;
* papel em combate.

Os detalhes pertencem ao documento:

* [Classes](../heroes/02_CLASSES.md)

## Sensação desejada

> "Este personagem possui uma identidade própria."

---

## Habilidades

## Função

Multiplicar e expressar a build.

Habilidades não devem substituir equipamentos como principal fonte de poder.

Elas devem ampliar o estilo da classe e transformar atributos e itens em ações visíveis no combate automático.

Os detalhes pertencem ao documento:

* [Habilidades](../heroes/04_SKILLS.md)

## Sensação desejada

> "Minha build está funcionando."

---

# Repetição Saudável

A repetição deve ser recompensadora.

O jogador pode revisitar conteúdos para obter:

* experiência;
* ouro;
* equipamentos;
* progresso de build;
* preparação para chefes;
* preparação para dificuldades superiores.

A repetição não deve parecer desperdício de tempo.

Ela deve representar preparação.

---

# Relação com Ouro

O ouro deve acompanhar o crescimento do jogador.

Ele deve funcionar como recurso de longo prazo.

Possíveis usos futuros:

* upgrades;
* serviços;
* reroll;
* craft;
* ajustes de build;
* manutenção de sistemas futuros.

As fórmulas e valores pertencem aos documentos:

* [Loot e economia](04_LOOT_ECONOMY.md)
* [Fórmulas de balanceamento](../technical/03_BALANCE_FORMULAS.md)

---

# Relação com Monstros

Inimigos devem escalar conforme:

* mapa;
* ato;
* dificuldade;
* categoria;
* modificadores.

Monstros não devem escalar apenas pelo nível do herói.

O mundo define o desafio.

As regras detalhadas pertencem ao documento:

* [Sistema de monstros](../monsters/01_MONSTER_SYSTEM.md)

---

# Relação com Chefes

Chefes representam marcos de progressão.

Eles devem validar:

* nível;
* equipamentos;
* atributos;
* build;
* sobrevivência;
* dano.

Chefes não são apenas inimigos com mais vida.

Eles bloqueiam avanço e encerram capítulos.

As regras detalhadas pertencem ao documento:

* [Chefes](../monsters/04_BOSSES.md)

---

# Relação com Balanceamento

Este documento define intenção e sensação.

As fórmulas pertencem ao documento:

* [Fórmulas de balanceamento](../technical/03_BALANCE_FORMULAS.md)

Exemplos de assuntos que não devem ser definidos aqui:

* XP exata por nível;
* multiplicador de dificuldade;
* HP de monstros;
* dano final;
* ouro por encontro;
* Power exato;
* Build Score exato.

---

# Critérios de Validação

A progressão será considerada saudável quando responder positivamente aos critérios abaixo.

---

## 1. O Jogador Percebe Evolução?

Perguntas:

* o jogador percebe que está ficando mais forte?
* o próximo nível é desejado?
* o progresso continua interessante após várias horas?
* existem objetivos de curto, médio e longo prazo?

Sinais de problema:

* níveis sem impacto;
* progressão rápida demais;
* progressão lenta demais;
* sensação de estagnação.

---

## 2. O Level Up Possui Valor?

Subir de nível deve ser relevante.

O jogador deve perceber:

* aumento de poder;
* aumento de sobrevivência;
* acesso ou aproximação de novos conteúdos.

Sinais de problema:

* subir de nível não muda nada;
* níveis viram apenas números;
* equipamentos anulam totalmente o valor do nível.

---

## 3. Os Equipamentos Possuem Impacto?

Equipamentos são a principal fonte de crescimento.

Perguntas:

* o jogador fica animado ao encontrar loot?
* trocar item é uma decisão?
* existe sensação de recompensa?
* Build Score ajuda a entender valor real?

Sinais de problema:

* itens são ignorados;
* loot parece irrelevante;
* equipamentos possuem diferenças mínimas.

---

## 4. Os Mapas Possuem Identidade?

Cada mapa deve possuir personalidade.

Diferenças esperadas:

* ambientação;
* inimigos;
* ritmo;
* recompensas;
* sensação de ameaça.

Sinais de problema:

* todos os mapas parecem iguais;
* apenas números mudam;
* não existe sensação de jornada.

---

## 5. Os Chefes Funcionam Como Marcos?

Chefes devem encerrar etapas.

Perguntas:

* o chefe exige preparação?
* derrotá-lo gera satisfação?
* ele bloqueia avanço de forma justa?
* a recompensa é percebida como superior?

Sinais de problema:

* chefe morre como inimigo comum;
* chefe parece injusto;
* não existe expectativa;
* não existe recompensa especial.

---

## 6. O Jogador Sempre Possui Objetivo?

O jogador deve possuir simultaneamente:

## Curto Prazo

* próximo combate;
* próximo item;
* próximo nível.

## Médio Prazo

* próximo mapa;
* próximo chefe;
* próximo ato.

## Longo Prazo

* próxima dificuldade;
* próxima build;
* próximo item raro.

Se o jogador não possui objetivo claro, a progressão falhou.

---

## 7. O Poder Está Distribuído Corretamente?

Distribuição desejada:

* equipamentos como principal fonte de poder;
* atributos como especialização;
* classe como identidade;
* habilidades como expressão da build;
* nível como crescimento base.

Sinais de problema:

* níveis fazem tudo;
* habilidades fazem tudo;
* equipamentos não importam;
* atributos não mudam decisões.

---

## 8. Existe Espaço Para Crescimento Futuro?

Todo sistema deve deixar espaço para expansão.

Perguntas:

* ainda existem melhorias desejáveis?
* ainda existem itens para buscar?
* ainda existem desafios para superar?
* ainda existe uma próxima meta?

O jogador não deve sentir que concluiu completamente o personagem cedo demais.

---

# Regra Principal

Nenhum sistema novo deve ser implementado para corrigir um sistema antigo.

Exemplos:

* não criar habilidades porque o combate está sem graça;
* primeiro corrigir o combate;
* não criar raças porque atributos estão sem identidade;
* primeiro corrigir atributos;
* não criar novos mapas porque a progressão está rápida demais;
* primeiro corrigir a progressão.

Cada problema deve ser resolvido em sua camada de origem.

---

# Meta da Versão 1.0

Ao deixar o TBH2 aberto durante longos períodos, o jogador deve perceber:

* evolução constante;
* novos equipamentos;
* avanço de mapas;
* aumento gradual de poder;
* objetivos de curto prazo;
* objetivos de longo prazo;
* sensação de jornada contínua.

A progressão deve incentivar retorno sem exigir atenção constante.

---

# Regras

* Progressão deve ser perceptível.
* Progressão não deve depender apenas de nível.
* Equipamentos devem ser a principal fonte de poder.
* Mapas representam conquista física do mundo.
* Chefes representam bloqueios e marcos.
* Dificuldades representam novos ciclos.
* Habilidades não devem ser documentadas em detalhe neste arquivo.
* Fórmulas não devem ser definidas neste arquivo.
* Conteúdo específico deve permanecer nos documentos proprietários.
* Todo novo sistema deve reforçar o loop central.

---

# Dados

Reservado para marcos conceituais de progressão.

Fórmulas, constantes e tabelas pertencem ao documento de balanceamento.

---

# Pendências

* Validar tempo real dos níveis 1 a 10.
* Validar tempo real dos níveis 11 a 20.
* Validar ritmo dos mapas do Ato I.
* Validar dificuldade do chefe do Ato I.
* Validar impacto dos equipamentos na progressão.
* Definir metas de tempo por mapa.
* Definir critérios numéricos no documento de balanceamento.
* Remover conteúdo de habilidades deste arquivo e manter em `heroes/04_SKILLS.md`.
* Remover regras técnicas de balanceamento deste arquivo quando já existirem em `technical/03_BALANCE_FORMULAS.md`.

---

# Histórico de Alterações

* 2026-06-10: documento inicial de progressão criado.
* 2026-06-10: conceito de Mapa como Progresso incorporado.
* 2026-06-10: progressão em camadas registrada.
* 2026-06-10: curva de poder reorganizada.
* 2026-06-10: documento reestruturado para separar progressão de GDD, habilidades e fórmulas.
