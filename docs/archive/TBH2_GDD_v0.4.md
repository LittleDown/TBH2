# TBH2 — TaskBar Hero 2

## Game Design Document Atualizado

**Versão do documento:** 0.4  
**Versão-alvo inicial do jogo:** 0.1  
**Gênero:** Idle RPG de fantasia sombria  
**Plataforma:** Windows  
**Formato:** Taskbar Companion em janela lateral compacta  
**Referências:** Diablo, Warcraft, Dungeons & Dragons, Melvor Idle e ARPGs de progressão por loot

---

# 1. Visão do Jogo

TBH2 é um Idle RPG Companion para Windows.

O jogo acompanha o usuário durante o uso normal do computador em uma janela lateral compacta. Nessa janela, um aventureiro percorre mapas, encontra inimigos, luta automaticamente, coleta recompensas, melhora equipamentos e avança por uma campanha persistente.

O jogador não controla golpes individuais.

O jogador prepara o herói.

O jogo executa a jornada.

A experiência central é:

> Meu aventureiro continua sua jornada mesmo quando minha atenção está em outro lugar.

Sempre que olhar para o jogo, o jogador deve entender:

- onde o herói está;
- qual mapa está sendo explorado;
- qual inimigo está enfrentando;
- quanto falta para concluir o mapa;
- qual recompensa recente foi obtida;
- qual é a próxima meta relevante.

---

# 2. Promessa Central

> Uma campanha de RPG persistente acontece na lateral da tela, com progresso automático, combate idle, loot relevante e decisões ocasionais de build que respeitam a atenção do usuário.

TBH2 não deve parecer apenas um contador de números.

Ele deve parecer uma pequena jornada visual acontecendo ao lado do usuário.

---

# 3. Fantasia Central

O jogador acompanha um aventureiro que atravessa regiões perigosas em busca da origem de uma corrupção crescente.

A jornada começa em uma fronteira medieval abandonada e avança para regiões cada vez mais hostis, antigas e sobrenaturais.

O herói luta sozinho, mas sua evolução depende das decisões do jogador:

- equipamentos;
- atributos;
- classe;
- habilidades futuras;
- leitura de recompensas;
- preparação para chefes;
- avanço por mapas, atos e dificuldades.

O herói deve parecer um companheiro persistente.

Não uma unidade aguardando comandos constantes.

---

# 4. Pilares de Design

## 4.1 Jornada Contínua

O mundo deve transmitir movimento constante.

Mesmo com baixa interação, o jogador deve sentir que o herói está viajando.

---

## 4.2 Progresso com Destino

Nível mede crescimento.

Mapas, atos e dificuldades mostram onde esse crescimento está sendo aplicado.

O mapa é parte da progressão.

---

## 4.3 Estratégia por Build

O jogador não escolhe um modo de combate como agressivo, balanceado ou defensivo.

O estilo de combate surge da build:

- arma equipada;
- armadura;
- acessórios;
- atributos;
- classe;
- habilidades futuras;
- efeitos especiais.

Uma build agressiva deve nascer de escolhas de item e atributo, não de um botão de postura.

---

## 4.4 Agência de Baixa Frequência

O jogador toma decisões importantes em momentos específicos.

O jogo não exige atenção a cada combate.

Decisões esperadas:

- equipar item melhor;
- revisar atributos;
- avaliar build;
- enfrentar chefe;
- avançar dificuldade;
- reorganizar habilidades futuras.

---

## 4.5 Presença Discreta

O jogo deve permanecer aberto sem competir com a atividade principal do usuário.

A janela deve ser compacta, legível e estável.

---

## 4.6 Recompensas Sustentáveis

Experiência oferece crescimento previsível.

Ouro constrói valor acumulado.

Loot gera surpresa e saltos reais de poder.

---

## 4.7 Baixa Punição

A derrota bloqueia avanço, mas não apaga progresso principal.

O jogador deve entender que precisa fortalecer a build.

Não sentir que foi punido injustamente.

---

## 4.8 Expansão em Camadas

Classes, habilidades, raças, dungeons, companion e sistemas de Taskbar devem ser adicionados por fases.

Nenhum sistema futuro deve exigir reconstrução do núcleo.

---

# 5. Escopo da Versão 0.1

## Incluído

- herói persistente;
- exploração contínua;
- combate automático;
- experiência e níveis;
- ouro persistente;
- loot básico;
- equipamento automático ou manual;
- dificuldade Normal;
- Ato I com 10 mapas;
- inimigos comuns iniciais;
- chefe do Ato I;
- interface lateral 360x600;
- feedback visual de exploração, encontro, combate, recompensa e retorno à exploração;
- save JSON versionado;
- progressão de mapa.

---

## Preparado Conceitualmente

- atributos STR, DEX, INT e CON;
- classes;
- raças;
- habilidades automáticas;
- raridades superiores;
- elites;
- dificuldades superiores;
- dungeons;
- companion;
- sistema diário;
- sistema de sessão;
- progressão offline.

---

## Fora do Escopo Inicial

- multiplayer;
- Party Dungeon;
- árvore de talentos;
- habilidades manuais;
- economia completa com loja;
- crafting avançado;
- afixos complexos;
- eventos temporários;
- cloud save;
- sistemas invasivos de leitura do computador.

---

# 6. Game Loop

O loop central do TBH2 representa a jornada automática do aventureiro.

O jogador prepara o herói.

O jogo executa a jornada.

O ciclo principal é:

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

---

## 6.1 Loop Principal

1. O jogo cria um novo `GameState` ou carrega um save existente.
2. O herói é posicionado no mapa atual da campanha.
3. Durante a exploração, o mundo permanece em movimento para transmitir jornada contínua.
4. O sistema seleciona um encontro compatível com:
   - ato atual;
   - mapa atual;
   - dificuldade atual;
   - pool de monstros da região.
5. Ao encontrar um inimigo, a exploração desacelera e o combate é iniciado.
6. Herói e inimigo executam ações automaticamente.
7. O resultado do combate depende da preparação do herói:
   - nível;
   - equipamentos;
   - atributos;
   - classe;
   - habilidades futuras;
   - Power;
   - Build Score.
8. Ao derrotar o inimigo, o herói recebe recompensas:
   - experiência;
   - ouro;
   - chance de loot;
   - progresso no mapa.
9. Caso um item seja encontrado, ele é adicionado ao inventário.
10. O sistema pode sugerir ou aplicar auto-equipamento quando o novo item for melhor para a build atual.
11. Ao acumular experiência suficiente, o herói sobe de nível.
12. Ao completar o objetivo do mapa, o próximo mapa é desbloqueado.
13. Ao chegar ao mapa final de um ato, o herói enfrenta o chefe do ato.
14. Ao derrotar o chefe, o próximo ato ou dificuldade pode ser desbloqueado.
15. Eventos importantes solicitam salvamento automático.
16. O ciclo retorna à exploração.

---

## 6.2 Derrota

Se o herói for derrotado:

1. O combate é encerrado.
2. O avanço atual é interrompido.
3. O herói retorna a um estado seguro.
4. A vida é restaurada conforme regra de balanceamento.
5. O chefe ou mapa permanece como bloqueio de progresso.
6. O jogador deve fortalecer o herói antes de tentar avançar novamente.

A derrota não remove progresso principal.

Ela comunica que a build ainda não está pronta.

---

## 6.3 Eventos de Save

O jogo deve salvar automaticamente em eventos importantes:

- criação de personagem;
- ganho de nível;
- obtenção de item relevante;
- alteração de equipamento;
- conclusão de combate;
- avanço de mapa;
- derrota de chefe;
- desbloqueio de ato;
- desbloqueio de dificuldade;
- fechamento do jogo.

---

# 7. Progressão

A progressão principal segue:

```text
Mapa → Ato → Dificuldade
```

O jogador progride em várias escalas:

| Camada | Horizonte | Objetivo |
|---|---|---|
| Combate | Segundos | Derrotar o inimigo atual |
| Mapa | Minutos | Completar a meta do mapa |
| Ato | Sessões | Preparar-se e derrotar o chefe |
| Dificuldade | Longo prazo | Repetir a campanha em ciclo mais perigoso |
| Build | Contínuo | Melhorar equipamentos, atributos e sinergias |

---

## 7.1 Mapas

Cada ato possui 10 mapas sequenciais.

Os mapas 1 a 9 representam progressão e exploração.

O mapa 10 representa o chefe do ato.

Cada mapa define:

- identidade visual;
- nível recomendado;
- pool de monstros;
- chance de elites futura;
- tabela de loot;
- progresso necessário;
- chefe, quando aplicável.

---

## 7.2 Atos

Os atos representam grandes capítulos da campanha.

| Ato | Região | Tema |
|---|---|---|
| Ato I | Fronteira Esquecida | Estradas abandonadas, bosques, ruínas e mortos-vivos |
| Ato II | Terras da Cinza | Deserto, império perdido, ruínas soterradas e maldição antiga |
| Ato III | Selva Carmesim | Natureza corrompida, ruínas ancestrais e ameaça global |

Somente o Ato I pertence ao escopo jogável inicial.

Ato II e Ato III ficam documentados para direção futura.

---

## 7.3 Dificuldades

Dificuldades representam novos ciclos de progressão.

Estrutura inicial:

1. Normal
2. Veterano
3. Pesadelo
4. Infernal

A dificuldade Mítica não pertence ao escopo inicial.

Pode ser avaliada futuramente como expansão.

Cada dificuldade aumenta:

- vida dos monstros;
- dano dos monstros;
- experiência recebida;
- ouro recebido;
- potencial de loot;
- frequência de elites futura;
- relevância dos chefes.

O herói mantém:

- nível;
- experiência;
- ouro;
- equipamentos;
- inventário;
- estatísticas;
- progresso de build.

A campanha reinicia no novo ciclo de dificuldade.

---

# 8. Mundo e Campanha

O mundo deve transformar números em jornada.

A progressão visual deve acompanhar a progressão mecânica.

O jogador deve sentir que saiu de uma região relativamente segura e avançou para lugares cada vez mais perigosos.

---

## 8.1 Ato I — A Fronteira Esquecida

Função:

- introduzir jornada;
- ensinar progressão;
- apresentar ameaça sobrenatural;
- validar primeiro chefe.

Progressão emocional:

```text
Curiosidade
↓
Exploração
↓
Estranheza
↓
Perigo
↓
Sobrenatural
↓
Confronto
```

Mapas planejados:

1. Estrada Abandonada
2. Bosque dos Sussurros
3. Acampamento Saqueado
4. Colinas da Fronteira
5. Cemitério da Vigília
6. Ruínas do Mosteiro
7. Ponte Quebrada
8. Fortaleza Arruinada
9. Salão dos Caídos
10. Covil do Senhor dos Ossos

Chefe oficial:

- Senhor dos Ossos

Observação:

`Capitão Ossonegro`, usado em demo técnica, deve ser tratado como nome temporário, legado ou possível elite nomeado futuro.

---

## 8.2 Ato II — Terras da Cinza

Função:

- contrastar com o Ato I;
- apresentar deserto e império perdido;
- elevar hostilidade do mundo;
- introduzir maldição antiga.

Chefe planejado:

- Rei Escorpião

---

## 8.3 Ato III — Selva Carmesim

Função:

- revelar que a corrupção não é local;
- apresentar natureza corrompida;
- ampliar escala da ameaça.

Chefe planejado:

- Coração da Selva

---

# 9. Combate

O combate é automático.

O jogador não controla ataques individuais.

O combate testa decisões tomadas antes dele.

---

## 9.1 Filosofia

O combate deve ser simples de acompanhar e difícil de otimizar.

O jogador deve entender:

- quem está atacando;
- quem recebeu dano;
- se venceu;
- se perdeu;
- qual recompensa recebeu;
- se precisa fortalecer a build.

---

## 9.2 Remoção de Estratégias

O projeto não deve manter modos selecionáveis como:

- Agressivo;
- Balanceado;
- Defensivo.

Esses elementos existiram na demo técnica, mas agora são considerados legado.

A identidade de combate deve vir de:

- equipamentos;
- atributos;
- classe;
- habilidades futuras;
- efeitos especiais;
- Power;
- Build Score.

---

## 9.3 Categorias Futuras de Dano

Sistema planejado para fases futuras:

- dano físico;
- dano mágico;
- dano puro.

Defesas futuras:

- Armor;
- Spell Armor;
- Evasion;
- Parry;
- redução de controle.

Essas categorias pertencem a fases posteriores, após validação do núcleo.

---

# 10. Herói e Build

O herói é a entidade principal do jogador.

Inicialmente pode ser genérico.

Futuramente será definido por:

- raça;
- classe;
- atributos;
- habilidades;
- equipamentos;
- build.

---

## 10.1 Atributos Futuros

Todo herói terá:

- STR — Strength;
- DEX — Dexterity;
- INT — Intelligence;
- CON — Constitution.

Função esperada:

| Atributo | Função |
|---|---|
| STR | dano físico, armas pesadas, força bruta |
| DEX | precisão, velocidade, crítico, evasão futura |
| INT | dano mágico, cura, efeitos arcanos |
| CON | vida, resistência, sustentação |

---

## 10.2 Classes Futuras

Classes planejadas:

- Guerreiro;
- Arqueiro;
- Mago;
- Curandeiro.

Cada classe deve alterar decisões de build.

Não deve ser apenas um bônus passivo.

---

## 10.3 Raças Futuras

Raças planejadas:

- Humano;
- Elfo;
- Anão;
- Meio-Orc.

Raças devem ser implementadas apenas após atributos e classes estarem estáveis.

---

# 11. Itens e Loot

Loot é uma das principais fontes de poder do TBH2.

O nível oferece crescimento constante.

Equipamentos oferecem saltos de poder.

---

## 11.1 Filosofia de Itemização

O jogador deve se perguntar:

> Este item melhora minha build?

Não apenas:

> Este número é maior?

---

## 11.2 Slots Atuais e Futuros

A demo técnica utiliza slots simplificados:

- Arma;
- Armadura;
- Acessório.

A estrutura futura prevê:

- weapon;
- offhand;
- helmet;
- chest;
- gloves;
- belt;
- boots;
- ring_1;
- ring_2;
- amulet.

---

## 11.3 Raridades

Raridades planejadas:

- Comum;
- Mágico;
- Raro;
- Épico;
- Lendário;
- Set;
- Mítico futuro.

Regra principal:

> Raridade não é poder garantido. Raridade é potencial.

---

## 11.4 Power e Build Score

Power representa leitura geral de força.

Build Score representa valor real para a build atual.

Auto-equip deve priorizar Build Score quando o sistema estiver disponível.

---

# 12. Monstros

Monstros sustentam combate, progressão e loot.

Eles devem criar variedade sem exigir IA complexa.

---

## 12.1 Categorias

Hierarquia planejada:

```text
Comum
↓
Campeão
↓
Elite
↓
Elite Nomeado
↓
Chefe
```

---

## 12.2 Monstros Comuns

Função:

- sustentar o fluxo;
- oferecer XP;
- oferecer ouro;
- gerar chance de loot;
- representar o ecossistema da região.

Monstros comuns devem ser reconhecíveis rapidamente.

---

## 12.3 Elites

Elites quebram a rotina.

Devem possuir:

- modificadores;
- visual destacado;
- maior risco;
- maior recompensa.

Elites não substituem chefes.

---

## 12.4 Chefes

Chefes são marcos de progressão.

Eles respondem à pergunta:

> Meu personagem está pronto para avançar?

Chefes devem:

- bloquear avanço;
- validar build;
- encerrar atos;
- oferecer recompensas superiores;
- permanecer relevantes em dificuldades maiores.

---

# 13. UI e UX

A interface deve servir à jornada.

Não deve competir com ela.

O jogo precisa ser legível em uma janela compacta de 360x600.

---

## 13.1 Áreas Principais

A interface deve priorizar:

- área de exploração;
- herói e inimigo;
- informações essenciais;
- progresso do mapa;
- loot recente;
- inventário e equipamentos;
- eventos importantes.

---

## 13.2 Atenção Periférica

O jogador deve conseguir acompanhar o jogo com olhares rápidos.

Feedbacks importantes:

- movimento do mundo;
- entrada de inimigo;
- dano flutuante;
- item raro;
- level up;
- chefe encontrado;
- vitória;
- avanço de mapa.

---

# 14. Identidade de Taskbar

TBH2 é um Companion de desktop.

Ele deve existir ao lado do usuário, não acima da tarefa principal.

---

## 14.1 Princípios

- presença discreta;
- baixa interrupção;
- jornada contínua;
- progresso silencioso;
- mensagens curtas;
- visual legível;
- nenhuma coleta invasiva.

---

## 14.2 Privacidade

O jogo não deve ler:

- janelas abertas;
- textos digitados;
- sites acessados;
- arquivos pessoais;
- aplicativos em uso;
- conversas;
- dados sensíveis.

Sistemas futuros podem usar apenas dados internos do jogo:

- tempo de sessão;
- último acesso;
- progresso salvo;
- eventos internos;
- horário local para atmosfera.

---

# 15. Save e Dados

O save deve preservar a jornada do jogador com segurança.

Formato inicial recomendado:

```text
save_data.json
```

O save deve ser:

- versionado;
- migrável;
- validável;
- recuperável por backup;
- compatível com campos futuros.

---

## 15.1 Fonte de Verdade

Regra principal:

```text
SaveData salva progresso.
Definitions descrevem conteúdo.
```

O save armazena identificadores e estado do jogador.

O conteúdo do jogo fica em definições.

---

## 15.2 GameState

O estado persistente principal deve evoluir para:

```text
GameState
├── save_version
├── created_at
├── updated_at
├── hero
├── inventory
├── equipment
├── world_progress
├── wallet
├── statistics
├── session_state
├── daily_state
└── companion_state
```

Nem todos os campos precisam existir na v0.1.

Mas a arquitetura deve permitir sua adição futura.

---

# 16. Arquitetura Técnica

A arquitetura futura deve separar:

1. Domínio
2. Aplicação
3. Infraestrutura
4. Apresentação

---

## 16.1 Regra Central

A UI não decide regras de jogo.

A UI envia comandos.

A aplicação processa.

O domínio aplica regras.

A infraestrutura salva, carrega, fornece conteúdo, tempo e aleatoriedade.

---

## 16.2 Sistemas Principais

Sistemas planejados:

- GameSession;
- EncounterSystem;
- CombatSystem;
- RewardSystem;
- LootSystem;
- EquipmentSystem;
- ProgressionSystem;
- EconomySystem;
- AttributeSystem;
- SaveCoordinator.

Sistemas removidos ou legados:

- StrategySystem;
- CombatStrategy ativo;
- ChangeCombatStrategy.

---

# 17. Roadmap Resumido

## Fase 1 — Núcleo Jogável

- exploração;
- combate;
- loot;
- progressão;
- save;
- Ato I técnico;
- feedback visual.

---

## Fase 2 — Identidade do Herói

- atributos STR, DEX, INT e CON;
- class_id padrão;
- race_id padrão;
- derivados básicos;
- migração de save;
- Power e Build Score.

---

## Fase 3 — Classes e Habilidades

- classes iniciais;
- habilidades automáticas;
- autocast;
- cooldowns;
- feedback visual.

---

## Fase 4 — Combate Avançado

- dano físico, mágico e puro;
- armor e spell armor;
- evasion;
- parry;
- crítico;
- regeneração;
- cura.

---

## Fase 5 — Mundo Expandido e Chefes

- Ato I consolidado;
- Ato II planejado;
- Ato III planejado;
- monstros por região;
- elites;
- chefes;
- dificuldade Normal validada.

---

## Fase 6 — Dificuldades e Endgame Inicial

- Veterano;
- Pesadelo;
- Infernal;
- loot quality;
- escalonamento de chefes e monstros.

---

## Fase 7 — Solo AFK Dungeon

- dungeon solo;
- 15 andares;
- chefe intermediário;
- chefe final;
- recompensas acumuladas.

---

## Fase 8 — Companheiros e Party Dungeon

- NPCs companheiros;
- composição de grupo;
- Party Dungeon jogável solo;
- multiplayer real apenas como possibilidade futura.

---

# 18. Riscos Principais

- excesso de sistemas antes do balanceamento;
- poluição visual na janela compacta;
- classes virarem apenas bônus passivos;
- habilidades automáticas virarem ruído;
- dungeons competirem com campanha;
- Party Dungeon exigir multiplayer cedo demais;
- save quebrar por ausência de migração;
- documentos históricos conflitarem com a direção atual.

---

# 19. Decisões Revogadas ou Legadas

As seguintes decisões não devem guiar o design futuro:

- estratégia de combate Agressiva, Balanceada e Defensiva como sistema ativo;
- inimigos gerados apenas pelo nível do herói;
- dificuldade Mítica no escopo inicial;
- chefe `Capitão Ossonegro` como nome final do Ato I;
- UI decidindo regras de combate, loot, progressão ou save.

---

# 20. Próxima Sprint Recomendada

Prioridade atual:

1. consolidar Fase 1;
2. remover estratégias legadas;
3. padronizar chefe do Ato I como Senhor dos Ossos;
4. validar save versionado;
5. melhorar loop visual da exploração;
6. testar progressão completa do Ato I;
7. revisar balanceamento inicial de XP, ouro, loot e chefe.

Não iniciar habilidades, raças completas, dungeons ou party antes dessa consolidação.

---

# 21. Critérios de Sucesso da V0.1

A v0.1 será considerada saudável quando:

- o ciclo principal funcionar continuamente;
- o jogador entender exploração, encontro, combate, recompensa e progressão;
- o Ato I puder ser concluído;
- o chefe funcionar como bloqueio justo;
- loot e equipamentos tiverem impacto perceptível;
- o save preservar progresso corretamente;
- a janela compacta continuar legível;
- sistemas legados estiverem removidos ou isolados;
- o jogo permanecer estável por longas sessões.

---

# 22. Histórico de Alterações

- 2026-06-10: GDD atualizado para alinhar com documentação modular.
- 2026-06-10: Game Loop atualizado para usar exploração, encontro, combate, recompensa e progressão.
- 2026-06-10: estratégias de combate marcadas como legado.
- 2026-06-10: mundo, atos, dificuldades, monstros, chefes, save e roadmap consolidados.
- 2026-06-10: removida dificuldade Mítica do escopo inicial.
- 2026-06-10: identidade de Taskbar e privacidade incorporadas ao GDD.
