# TBH2 - TaskBar Hero 2

Idle RPG para Windows concebido como um companheiro de Taskbar. O herói combate,
evolui e encontra recompensas automaticamente enquanto o usuário utiliza outras
aplicações.

## Projeto

O projeto busca combinar progressão idle, campanha estruturada, loot escalável e
decisões de baixa frequência em uma interface lateral compacta.

## Demo Técnica Jogável

A base Python agora inclui uma demo compacta de 360x600 com:

- combate automático com pools de monstros próprios para cada mapa;
- identidade de combate baseada em nível e equipamentos, sem estratégia manual;
- experiência, level up, ouro, mortes e renascimento;
- loot Comum, Raro e Épico com Poder escalável;
- sprites temporários em pixel art para herói, inimigos, chefe e loot;
- jornada visual contínua com loop baseado em delta time;
- fluxo Exploração → Encontro → Combate → Recompensa;
- animações de caminhada, ataque, impacto, dano flutuante, vitória e morte;
- Guerreiro corpo a corpo e Arqueiro MVP com ataque automático à distância;
- projétil visual de flecha desacoplado do cálculo de dano;
- entrada do inimigo pela direita e cenário com movimento contínuo;
- parallax em três camadas na Estrada Abandonada;
- desaceleração antes do combate e retomada gradual da jornada;
- kit modular em pixel art e vestígios narrativos na estrada;
- eventos ambientais de corvos, folhas e poeira;
- ambientes simples específicos para cada mapa do Ato I;
- inventário visual 5x4, autoequipamento e equipamento manual por clique;
- painel de equipamentos com Arma, Armadura e Acessório;
- dez mapas oficiais do Ato I, com progressão por vitórias e portal de chefe;
- Senhor dos Ossos como chefe oficial e conclusão do Ato I;
- abas Hero, Inventory e Map;
- save JSON v4, migração de formatos antigos e recuperação por backup.

## Documentação

A documentação de design, balanceamento e arquitetura está organizada por
domínios em [`docs/README.md`](docs/README.md).

Documentos de entrada:

- [Visão do projeto](docs/core/00_VISION.md)
- [Gameplay central](docs/core/01_CORE_GAMEPLAY.md)
- [Progressão](docs/core/02_PROGRESSION.md)
- [Combate](docs/core/03_COMBAT.md)
- [Loot e economia](docs/core/04_LOOT_ECONOMY.md)
- [Arquitetura técnica](docs/technical/05_ARCHITECTURE.md)
- [Roadmap](docs/technical/04_ROADMAP.md)
- [Raças planejadas](docs/heroes/05_RACES.md)
- [Dungeons planejadas](docs/maps/06_DUNGEONS.md)
- [Relatório da demo](docs/DEMO_IMPLEMENTATION.md)
- [Consolidação do repositório](docs/REPOSITORY_CONSOLIDATION.md)
- [Sprint Exploração Viva](docs/EXPLORACAO_VIVA_SPRINT.md)
- [Direção artística e worldbuilding](docs/art/01_ART_DIRECTION_WORLDBUILDING.md)

## Requisitos

- Windows 10 ou 11;
- Python 3.12 ou superior;
- dependências de `requirements.txt`.

## Execução

No PowerShell, a partir da raiz do projeto:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe src\main.py
```

O progresso é salvo automaticamente em `save.json` a cada evento importante,
a cada dez segundos e ao fechar a janela.

Durante o desenvolvimento, a classe atual pode ser configurada e persistida:

```powershell
.\.venv\Scripts\python.exe src\main.py --class-id archer
.\.venv\Scripts\python.exe src\main.py --class-id warrior
```

## Controles

- `Hero`: atributos, poder da build e equipamentos.
- `Inventory`: clique em um item para equipá-lo.
- `Map`: acompanhe a campanha e o progresso até o chefe.

Durante a jornada, o herói caminha automaticamente pela região. Os encontros
interrompem a exploração, iniciam o combate e, após a recompensa, devolvem o
aventureiro à estrada. O loop visual usa `after()` e `time.perf_counter()`, sem
adicionar uma engine externa ao projeto.

## Testes

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

## Arquivos RAR analisados

O RAR de aproximadamente 157 MB contém o build Unity/IL2CPP `1.00.11`, sem
código-fonte editável. O RAR menor contém saves e logs locais desse build. A base
correta para esta implementação é o projeto Python deste repositório.

## Limitações da demo

- os sprites do Guerreiro ainda usam a referência JS; o Arqueiro possui arte MVP própria;
- não há áudio, loja, sistema completo de classes, habilidades, talentos ou progresso offline;
- após concluir o Ato I, o combate continua em modo livre no último mapa;
- o balanceamento é inicial e serve apenas para validar o loop.
