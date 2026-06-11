# Gameplay Central

## Objetivo

Definir o loop principal do TBH2 e a experiência que o jogador deve vivenciar ao longo do tempo.

Este documento possui prioridade sobre todos os demais sistemas.

Caso exista conflito entre uma mecânica e o Gameplay Central, o Gameplay Central deve prevalecer.

---

## Status

In Progress

---

## Dependências

* [Visão do projeto](00_VISION.md)
* [Progressão](02_PROGRESSION.md)
* [Combate](03_COMBAT.md)
* [Loot e economia](04_LOOT_ECONOMY.md)
* [UI e UX](05_UI_UX.md)
* [Estrutura do mundo](../maps/01_WORLD_STRUCTURE.md)
* [Identidade de Taskbar](../taskbar/01_TASKBAR_IDENTITY.md)

---

# Visão Geral

TBH2 é um Idle RPG Companion.

O jogador não controla diretamente cada movimento, ataque ou ação do personagem.

O papel do jogador é preparar, equipar e desenvolver seu aventureiro enquanto ele percorre o mundo automaticamente.

O foco principal não está na execução mecânica.

O foco está na progressão, na preparação de build e na sensação de jornada contínua.

O jogador deve sentir que acompanha um aventureiro vivo, avançando pelo mundo enquanto o computador continua sendo usado normalmente.

---

# Fantasia Principal

A experiência desejada é:

> "Meu aventureiro está viajando pelo mundo enquanto eu trabalho, estudo ou utilizo o computador."

O jogo deve transmitir:

* exploração;
* descoberta;
* combate automático;
* recompensas;
* evolução constante;
* avanço de mapas;
* conquista de chefes;
* sensação de jornada contínua.

---

# Loop Principal

O loop central do TBH2 é:

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

Este ciclo deve funcionar continuamente durante toda a vida útil do personagem.

O loop precisa ser compreensível mesmo em atenção periférica.

O jogador deve conseguir olhar rapidamente para a janela e entender o estado atual da jornada.

---

# Exploração

Durante a exploração:

* o personagem caminha automaticamente;
* o mundo se move ao seu redor;
* o mapa transmite sensação de viagem;
* eventos ambientais podem ocorrer;
* novos inimigos podem surgir;
* a progressão visual acompanha a progressão de mundo.

Objetivo:

Criar sensação de deslocamento, continuidade e aventura.

A exploração não é apenas intervalo entre combates.

Ela é parte central da identidade do TBH2.

---

# Encontro

Durante um encontro:

* um inimigo é encontrado;
* a exploração desacelera;
* o personagem interrompe a caminhada;
* o inimigo entra em cena;
* o combate é iniciado.

Objetivo:

Transformar a jornada em desafio.

O encontro deve comunicar visualmente que algo interrompeu o avanço do aventureiro.

---

# Combate

O combate é automático.

O jogador não executa ataques manualmente.

O jogador não escolhe modos de combate como agressivo, balanceado ou defensivo.

O resultado do combate depende da preparação do herói.

Fatores principais:

* nível;
* equipamentos;
* atributos;
* classe;
* habilidades futuras;
* raridade dos itens;
* Power;
* Build Score;
* sinergia da build.

Objetivo:

Validar o progresso acumulado.

O combate deve responder à pergunta:

> "Meu herói está preparado para este desafio?"

---

# Recompensa

Após vencer um encontro, o herói pode receber:

* experiência;
* ouro;
* equipamentos;
* progresso de mapa;
* progresso de campanha;
* eventos de loot.

Objetivo:

Gerar sensação de conquista e alimentar a próxima decisão do jogador.

A recompensa deve reforçar o ciclo:

```text
lutar
↓
ganhar
↓
melhorar
↓
avançar
```

---

# Progressão

A recompensa obtida alimenta sistemas permanentes.

Sistemas principais:

* níveis;
* equipamentos;
* atributos;
* classes;
* habilidades;
* mapas;
* atos;
* dificuldades.

Objetivo:

Preparar o personagem para desafios maiores.

A progressão deve acontecer em camadas.

O jogador deve ter sempre objetivos de curto, médio e longo prazo.

---

# Mapas Como Progressão

No TBH2, mapas não são apenas cenários.

Mapas representam avanço de mundo.

Cada mapa deve possuir:

* identidade visual;
* pool de monstros;
* nível recomendado;
* contexto de loot;
* sensação própria;
* papel dentro do ato.

Inimigos devem ser definidos pelo mundo.

A geração de inimigos deve considerar:

* ato atual;
* mapa atual;
* dificuldade atual;
* pool de monstros da região;
* tipo de encontro.

Inimigos não devem ser gerados apenas pelo nível do herói.

---

# Chefes Como Marcos

Chefes representam bloqueios de progressão.

Eles encerram mapas importantes, atos ou conteúdos especiais.

Um chefe deve testar:

* dano;
* sobrevivência;
* equipamentos;
* atributos;
* consistência da build.

Ao derrotar um chefe, o jogador deve sentir que conquistou uma etapa importante da jornada.

---

# Loop de Curto Prazo

Duração:

Minutos.

Objetivos:

* vencer encontros;
* ganhar XP;
* obter ouro;
* encontrar itens;
* observar eventos visuais.

Sensação desejada:

> "Algo está acontecendo."

---

# Loop de Médio Prazo

Duração:

Horas.

Objetivos:

* concluir mapas;
* melhorar equipamentos;
* derrotar chefes;
* desbloquear novas regiões;
* perceber evolução do herói.

Sensação desejada:

> "Estou avançando."

---

# Loop de Longo Prazo

Duração:

Dias ou semanas.

Objetivos:

* desbloquear dificuldades;
* completar builds;
* otimizar equipamentos;
* avançar atos;
* enfrentar desafios maiores;
* buscar itens raros.

Sensação desejada:

> "Meu personagem está evoluindo continuamente."

---

# Papel do Jogador

O jogador não é um controlador direto.

O jogador é um preparador de build.

Suas principais decisões são:

* escolher equipamentos;
* comparar itens;
* distribuir atributos;
* escolher classe;
* configurar habilidades futuras;
* preparar o herói para chefes;
* decidir quando avançar ou farmar.

A preparação é mais importante que a execução.

---

# Build Acima de Estratégia Manual

O TBH2 não deve depender de modos manuais como:

* agressivo;
* balanceado;
* defensivo.

Esses modos pertencem ao legado técnico e não representam a direção futura do projeto.

A identidade de combate deve surgir de:

* arma usada;
* armadura equipada;
* acessórios;
* atributos;
* classe;
* habilidades;
* efeitos especiais;
* sinergias.

Regra central:

> O jogador não escolhe um modo agressivo.
> O jogador constrói uma build agressiva.

---

# Frequência de Interação

TBH2 deve respeitar o conceito de Idle Companion.

O jogador pode observar o jogo por longos períodos sem interação constante.

Entretanto, deve existir incentivo para retornar regularmente.

Interações esperadas:

* trocar equipamentos;
* revisar inventário;
* comparar loot;
* distribuir atributos;
* revisar habilidades;
* enfrentar chefes;
* observar progresso;
* avançar mapas ou dificuldades.

O jogo deve funcionar sem microgerenciamento constante.

---

# Relação com Taskbar

TBH2 deve funcionar bem como jogo lateral de área de trabalho.

A experiência deve ser:

* compacta;
* legível;
* discreta;
* contínua;
* não invasiva.

O jogo deve permitir atenção periférica.

O usuário não deve precisar parar tudo para entender o que está acontecendo.

---

# O Que NÃO É TBH2

TBH2 não é:

* Action RPG;
* MMORPG;
* Clicker Game;
* Incremental puro;
* simulador passivo sem decisões;
* chatbot;
* ferramenta de produtividade;
* jogo que exige microgerenciamento constante.

O jogador deve tomar decisões relevantes.

Mas não deve executar ações repetitivas constantemente.

---

# Critério de Sucesso

O Gameplay Central está funcionando quando o jogador sente:

> "Meu aventureiro está vivendo uma jornada própria."

Ao retornar após algum tempo, o jogador deve perceber:

* progresso;
* recompensas;
* evolução;
* novos objetivos;
* avanço de mundo;
* possibilidade de melhorar a build.

A experiência deve gerar vontade de acompanhar a jornada, não obrigação de controlar cada ação.

---

# Regras

* O combate é automático.
* O jogador prepara a build.
* O jogo executa a jornada.
* O mundo define os encontros.
* Mapas fazem parte da progressão.
* Chefes são marcos de avanço.
* Equipamentos são a principal fonte de poder.
* Atributos reforçam especialização.
* Habilidades futuras devem ampliar builds, não substituir equipamentos.
* Modos de estratégia manual não fazem parte da direção futura.
* A experiência deve permanecer legível em janela compacta.
* Todo sistema novo deve reforçar o loop central.

---

# Histórico de Alterações

* 2026-06-10: documento central de gameplay criado.
* 2026-06-10: loop principal definido como Exploração, Encontro, Combate, Recompensa e Progressão.
* 2026-06-10: mapas definidos como parte da progressão.
* 2026-06-10: estratégia manual removida como direção futura.
* 2026-06-10: build definida como fonte da identidade de combate.
