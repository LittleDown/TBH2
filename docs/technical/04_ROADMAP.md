# Roadmap

## Objetivo

Organizar a evolução incremental do TBH2 sem comprometer sua identidade de RPG idle compacto para Taskbar.

Cada fase deve preservar um jogo executável, validar diversão, clareza, balanceamento e custo de manutenção antes da fase seguinte.

O roadmap não é uma lista de desejos.

Ele é um controle de risco.

---

## Status

In Progress

---

## Dependências

* [Visão do projeto](../core/00_VISION.md)
* [Gameplay central](../core/01_CORE_GAMEPLAY.md)
* [Progressão](../core/02_PROGRESSION.md)
* [Combate](../core/03_COMBAT.md)
* [Loot e economia](../core/04_LOOT_ECONOMY.md)
* [UI e UX](../core/05_UI_UX.md)
* [Sistema de herói](../heroes/01_HERO_SYSTEM.md)
* [Sistema de itens](../items/01_ITEM_SYSTEM.md)
* [Sistema de monstros](../monsters/01_MONSTER_SYSTEM.md)
* [Estrutura do mundo](../maps/01_WORLD_STRUCTURE.md)
* [Sistema de save](01_SAVE_SYSTEM.md)
* [Modelo de dados](02_DATA_MODEL.md)
* [Fórmulas de balanceamento](03_BALANCE_FORMULAS.md)
* [Arquitetura técnica](05_ARCHITECTURE.md)

---

# Visão Geral

O núcleo prioritário do TBH2 permanece:

```text
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
```

Todo sistema novo deve reforçar esse ciclo.

A fantasia central é:

> O aventureiro continua sua jornada enquanto o usuário utiliza o computador.

O jogador não controla ataques individuais.

O jogador prepara a build.

O jogo executa a jornada.

---

# Princípios do Roadmap

## 1. Jogo Sempre Executável

Cada fase deve terminar com o jogo funcionando.

Não aceitar fases que deixam o projeto quebrado, incompleto ou dependente de implementação futura para ser testável.

---

## 2. Expansão por Validação

Sistemas novos só entram quando a fundação anterior estiver estável.

Exemplos:

* não implementar habilidades antes de atributos;
* não implementar Party Dungeon antes de Solo Dungeon;
* não implementar multiplayer antes de NPCs companheiros;
* não expandir itens sem save e modelo de dados preparados.

---

## 3. Identidade de Taskbar

O TBH2 deve continuar legível em janela compacta.

A expansão de sistemas não pode destruir a leitura periférica.

Prioridade:

* clareza;
* baixa interrupção;
* progresso visível;
* jornada contínua.

---

## 4. Compatibilidade de Save

Toda mudança persistente exige:

* default;
* migração;
* fallback seguro;
* teste de carregamento de save antigo.

---

## 5. Balanceamento Centralizado

Fórmulas numéricas pertencem ao documento:

```text
technical/03_BALANCE_FORMULAS.md
```

O roadmap não define valores finais de HP, dano, XP, ouro, Power ou Build Score.

---

# Decisões Atuais Consolidadas

## Estratégias de Combate

O projeto não deve seguir com modos de combate selecionáveis.

Sistemas legados:

* Agressivo;
* Balanceado;
* Defensivo;
* StrategySystem;
* CombatStrategy;
* ChangeCombatStrategy.

Esses sistemas devem ser removidos ou ignorados com segurança.

A identidade de combate deve surgir de:

* equipamentos;
* atributos;
* classe;
* habilidades futuras;
* efeitos especiais;
* Power;
* Build Score.

Regra central:

> O jogador não escolhe modo agressivo.
> O jogador constrói uma build agressiva.

---

## Chefe Oficial do Ato I

O chefe oficial do Ato I é:

```text
Senhor dos Ossos
```

Nomes técnicos anteriores, como `Capitão Ossonegro`, devem ser tratados como legado ou reaproveitados futuramente como elite nomeado.

---

## Geração de Inimigos

Inimigos não devem ser gerados apenas pelo nível do herói.

A geração deve considerar:

* ato atual;
* mapa atual;
* dificuldade atual;
* pool de monstros da região;
* tipo de encontro.

O mundo é parte da progressão.

---

# Fase 1 — Consolidação do Núcleo Jogável

## Objetivo

Validar o ciclo principal do jogo.

---

## Escopo

* exploração contínua;
* encontros;
* combate automático;
* recompensa;
* XP;
* ouro;
* loot básico;
* equipamentos básicos;
* progressão de mapas;
* save funcional;
* estados visuais da jornada;
* Ato I jogável;
* chefe do Ato I;
* retorno automático à exploração.

---

## Estados Esperados

O jogador deve identificar claramente:

* exploração;
* encontro;
* combate;
* ataque;
* dano;
* vitória;
* recompensa;
* avanço;
* retorno à exploração.

---

## Ajustes Obrigatórios

Concluídos em 2026-06-11:

* estratégias legadas neutralizadas;
* `GameState` e save versionado validados;
* XP inicial e ganho de ouro centralizados;
* nomenclatura do chefe do Ato I padronizada.

Validações contínuas:

* revisar tempo por mapa;
* revisar dificuldade do chefe;
* executar simulações longas de progressão.

---

## Critério de Entrada

Demo técnica jogável existente.

---

## Critério de Saída

A Fase 1 será considerada validada quando:

* o ciclo completo funcionar repetidamente;
* o jogador não precisar intervir constantemente;
* save e progressão não apresentarem regressões;
* exploração, combate e recompensa forem visualmente compreensíveis;
* o jogo permanecer estável em uso prolongado;
* o Ato I puder ser concluído;
* o chefe funcionar como bloqueio justo;
* loot e equipamento tiverem impacto perceptível;
* sistemas legados estiverem controlados.

---

## Status

Em consolidação.

---

# Fase 2 — Modelo de Herói e Atributos

## Objetivo

Transformar o personagem em uma entidade de RPG mais sólida, com atributos primários e estrutura preparada para classes, raças e builds.

---

## Escopo

* STR;
* DEX;
* INT;
* CON;
* derivados básicos;
* `class_id` padrão;
* `race_id` padrão;
* defaults para saves antigos;
* migração compatível;
* recalculação de Power;
* recalculação de Build Score;
* revisão de HP, dano e defesa base.

---

## Fora do Escopo

Não implementar ainda:

* múltiplas classes completas;
* múltiplas raças completas;
* habilidades automáticas;
* passivas raciais avançadas;
* talentos;
* resistências avançadas;
* companions;
* dungeons.

---

## Critério de Entrada

Fase 1 validada.

---

## Critério de Saída

A Fase 2 será considerada validada quando:

* saves antigos carregarem com defaults seguros;
* todos os heróis possuírem STR, DEX, INT e CON;
* atributos influenciarem derivados de forma clara;
* Power for recalculável;
* Build Score for recalculável;
* equipamentos continuarem sendo a principal fonte de poder;
* o jogador entender por que o herói ficou mais forte.

---

# Fase 3 — Equipamentos Expandidos

## Objetivo

Expandir o sistema de equipamentos para sustentar builds reais e progressão de longo prazo.

---

## Escopo

* slots completos;
* ItemInstance;
* ItemBaseDefinition;
* raridades;
* Power;
* Build Score;
* auto-equip por Build Score;
* favoritos ou bloqueio de item;
* separação entre item base e item gerado;
* revisão de inventário;
* revisão de loot.

---

## Slots Oficiais

```text
weapon
offhand
helmet
chest
gloves
belt
boots
ring_1
ring_2
amulet
```

---

## Critério de Entrada

Fase 2 validada.

---

## Critério de Saída

A Fase 3 será considerada validada quando:

* todos os slots funcionarem;
* itens forem persistidos como instâncias;
* raridade alterar potencial, não apenas cor;
* Power servir como leitura geral;
* Build Score representar valor real para a build;
* auto-equip respeitar Build Score, favoritos e bloqueios;
* loot gerar decisões reais.

---

# Fase 4 — Classes e Habilidades

## Objetivo

Adicionar identidade de combate através de classes e habilidades automáticas.

O combate continua automático.

A decisão do jogador continua sendo preparação de build.

---

## Escopo

* classes jogáveis iniciais;
* habilidades automáticas;
* cooldowns;
* prioridade de habilidades;
* ativação e desativação individual;
* feedback visual de habilidade;
* passivas simples;
* integração com atributos e equipamentos.

---

## Classes Planejadas

* Guerreiro;
* Arqueiro;
* Mago;
* Curandeiro.

---

## Critério de Entrada

Fase 3 validada.

Atributos, equipamentos, Power e Build Score devem estar estáveis.

---

## Critério de Saída

A Fase 4 será considerada validada quando:

* cada classe possuir identidade distinta;
* habilidades não tornarem a tela ilegível;
* desativar uma habilidade gerar consequência compreensível;
* cooldowns forem claros;
* combate continuar automático;
* builds diferentes produzirem resultados diferentes.

---

# Fase 5 — Combate Avançado

## Objetivo

Expandir o combate com categorias de dano, defesas avançadas e estatísticas especializadas.

---

## Escopo

* dano físico;
* dano mágico;
* dano puro;
* Armor;
* Spell Armor;
* Evasion;
* Parry;
* crítico;
* velocidade de ataque;
* cura;
* regeneração;
* redução de controle;
* revisão de monstros;
* revisão de equipamentos;
* revisão de chefes.

---

## Critério de Entrada

Fase 4 validada.

Eventos de combate devem estar estruturados.

---

## Critério de Saída

A Fase 5 será considerada validada quando:

* ordem de resolução estiver documentada;
* testes cobrirem tipos principais de dano;
* feedback visual diferenciar eventos relevantes;
* defesas não anularem combate;
* crítico, evasão e parry forem úteis sem serem obrigatórios;
* complexidade adicional gerar decisões reais de build.

---

# Fase 6 — Mundo, Chefes e Dificuldades

## Objetivo

Consolidar campanha, atos, mapas, monstros, elites, chefes e dificuldades como estrutura principal de progressão.

---

## Escopo

* Ato I completo e validado;
* Ato II planejado;
* Ato III planejado;
* monstros comuns por região;
* elites;
* chefes de ato;
* recompensas por chefe;
* desbloqueio de atos;
* Normal;
* Veterano;
* Pesadelo;
* Infernal.

---

## Critério de Entrada

Combate, loot, equipamentos e progressão estáveis.

---

## Critério de Saída

A Fase 6 será considerada validada quando:

* cada mapa possuir identidade;
* cada ato possuir tema próprio;
* chefes funcionarem como bloqueios justos;
* elites quebrarem a rotina;
* dificuldades criarem novos ciclos de progressão;
* loot melhorar sem quebrar o jogo;
* o jogador sentir progressão de mundo.

---

# Fase 7 — Dungeons Solo AFK

## Objetivo

Adicionar conteúdo repetível opcional sem substituir a campanha.

---

## Escopo

* Solo AFK Dungeon;
* quinze andares;
* chefe intermediário no andar 10;
* chefe final no andar 15;
* recompensas acumuladas;
* regra de retomada ou descarte de run;
* integração com combate, loot e monstros existentes.

---

## Critério de Entrada

Campanha, dificuldades e balanceamento base validados.

---

## Critério de Saída

A Fase 7 será considerada validada quando:

* dungeon reutilizar sistemas existentes;
* recompensas forem boas sem serem obrigatórias;
* duração-alvo for adequada;
* progresso parcial tiver regra clara;
* dungeon não criar um segundo motor de progressão.

---

# Fase 8 — Companheiros e Party Dungeon

## Objetivo

Expandir o jogo para composição de grupo sem exigir microgerenciamento.

---

## Escopo

* até três NPCs companheiros;
* composição de grupo;
* equipamentos de companheiros;
* progressão sincronizada;
* Party Dungeon jogável solo;
* possibilidade futura de participantes reais.

---

## Critério de Entrada

Solo AFK Dungeon validada.

Arquitetura preparada para múltiplos participantes.

---

## Critério de Saída

A Fase 8 será considerada validada quando:

* composição de grupo alterar decisões;
* modo solo continuar completo;
* Party Dungeon reutilizar combate existente;
* companions não exigirem microgerenciamento constante;
* não houver dependência de infraestrutura online.

---

# Sistemas Futuros

Sistemas que podem ser avaliados após validação das fases principais:

* raças com passivas completas;
* talentos;
* crafting;
* sets;
* itens míticos;
* afixos avançados;
* eventos temporários;
* conquistas;
* offline progress;
* cosméticos;
* endgame bosses;
* torres;
* escaladas infinitas;
* multiplayer real.

Nenhum desses sistemas é prioridade até o núcleo estar sólido.

---

# Ordem Atual de Desenvolvimento

## Sprint Atual — Consolidação da Fase 1

Prioridades:

* balanceamento inicial;
* XP;
* ouro;
* progressão de mapas;
* chefe do Ato I;
* save;
* estabilidade;
* remoção de estratégias legadas;
* clareza visual;
* validação de longa duração.

---

## Sprint Seguinte — Modelo de Herói

Escopo permitido:

* STR;
* DEX;
* INT;
* CON;
* `class_id` padrão;
* `race_id` padrão;
* defaults de migração;
* derivados básicos;
* Power;
* Build Score.

Escopo proibido:

* habilidades;
* classes completas;
* raças completas;
* dungeons;
* companions;
* party;
* resistências avançadas.

---

## Sprint Posterior — Equipamentos Expandidos

Escopo permitido:

* slots completos;
* ItemInstance;
* ItemBaseDefinition;
* raridades;
* Build Score por item;
* auto-equip revisado.

---

# Fora do Escopo Atual

Não implementar agora:

* talentos;
* crafting;
* pets;
* guildas;
* PvP;
* multiplayer;
* party system;
* dungeons;
* passivas raciais completas;
* árvore de habilidades;
* endgame avançado.

---

# Riscos

## Progressão Rápida Demais

O jogador não deve alcançar níveis altos em poucos minutos.

A progressão deve sustentar:

* horas;
* dias;
* semanas;
* meses.

---

## Legibilidade

Muitos efeitos, estatísticas e mensagens podem prejudicar a janela compacta.

A identidade de Taskbar tem prioridade.

---

## Sistemas Prematuros

Implementar classes, habilidades ou dungeons antes da base pode gerar retrabalho.

---

## Save Instável

Mudanças em Hero, Item, WorldProgress ou DungeonRun sem migração podem quebrar saves antigos.

---

## Estratégias Legadas

Manter modos Agressivo, Balanceado e Defensivo cria conflito com a filosofia atual de build.

---

## Equipamentos Sem Modelo

Expandir itens sem ItemInstance, Build Score e save adequado pode gerar retrabalho.

---

# Meta da Versão 1.0

A versão 1.0 deve entregar uma experiência completa de Idle RPG Companion.

Ao deixar o TBH2 aberto durante longos períodos, o jogador deve perceber:

* progresso constante;
* exploração contínua;
* encontros automáticos;
* evolução do herói;
* descoberta de equipamentos;
* avanço de mapas;
* chefes como marcos;
* sensação de jornada.

A experiência principal deve funcionar antes da expansão do conteúdo.

---

# Critérios de Sucesso do Roadmap

O roadmap será considerado saudável quando:

* cada fase terminar com jogo executável;
* sistemas novos não quebrarem a identidade de Taskbar;
* o jogador sempre tiver objetivos claros;
* o projeto puder ser balanceado progressivamente;
* o save continuar compatível entre versões;
* Codex conseguir implementar sem misturar responsabilidades;
* a expansão parecer crescimento natural, não acúmulo de features.

---

# Histórico de Alterações

* 2026-06-10: roadmap oficial reestruturado.
* 2026-06-10: estratégias de combate marcadas como legado.
* 2026-06-10: Senhor dos Ossos definido como chefe oficial do Ato I.
* 2026-06-10: progressão reorganizada por fases técnicas e risco.
* 2026-06-10: Dungeons Solo separadas de Party Dungeon.
* 2026-06-10: priorizada consolidação da Fase 1 antes de novas features.
