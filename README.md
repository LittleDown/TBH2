# TBH2 - TaskBar Hero 2

Idle RPG para Windows concebido como um companheiro de Taskbar. O herói combate,
evolui e encontra recompensas automaticamente enquanto o usuário utiliza outras
aplicações.

## Projeto

O projeto busca combinar progressão idle, campanha estruturada, loot escalável e
decisões de baixa frequência em uma interface lateral compacta.

## Documentação

A documentação de design, balanceamento e arquitetura está organizada por
domínios em [`docs/README.md`](docs/README.md).

Documentos de entrada:

- [Visão do projeto](docs/core/00_VISION.md)
- [Gameplay central](docs/core/01_CORE_GAMEPLAY.md)
- [Progressão](docs/core/02_PROGRESSION.md)
- [Combate](docs/core/03_COMBAT.md)
- [Loot e economia](docs/core/04_LOOT_ECONOMY.md)
- [Roadmap](docs/technical/04_ROADMAP.md)

## Protótipo

O código existente representa uma prova de conceito anterior à documentação
modular. As próximas implementações devem usar os documentos de domínio como
fonte de decisão.

## Execução Atual

Requer Python 3.12+ e CustomTkinter.

```powershell
python -m pip install -r requirements.txt
python src/main.py
```

