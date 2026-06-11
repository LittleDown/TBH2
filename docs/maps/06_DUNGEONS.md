# Dungeons

## Objetivo

Definir a estrutura futura dos modos Solo AFK Dungeon e Party Dungeon.

## Status

Planned - Fase 5

## Dependências

- [Estrutura do mundo](01_WORLD_STRUCTURE.md)
- [Combate](../core/03_COMBAT.md)
- [Companheiros de grupo](../heroes/06_PARTY_COMPANIONS.md)
- [Roadmap](../technical/04_ROADMAP.md)

## Solo AFK Dungeon

Modo principal planejado:

- quinze andares por dungeon;
- chefe intermediário no andar 10;
- chefe final no andar 15;
- progressão automática entre encontros;
- recompensas acumuladas e apresentadas sem interromper o fluxo.

## Party Dungeon

Modo posterior:

- utiliza o mesmo sistema base do TBH2;
- suporta até quatro participantes;
- pode ser jogado solo;
- possui dificuldade e recompensas superiores;
- deve preservar automação e baixa frequência de interação.

Participantes podem ser jogadores ou NPCs conforme a evolução do produto. Rede,
matchmaking e sincronização não estão aprovados nesta fase.

## Regras

- O modo Solo deve ser validado antes do Party.
- Dungeons reutilizam combate, loot e progressão existentes.
- Chefes não recebem um motor separado.
- A composição de grupo deve gerar decisões sem exigir microgerenciamento.
- Recompensas exclusivas só entram após o balanceamento do modo base.

## Dados Planejados

- identificador e tema da dungeon;
- quantidade e estado dos andares;
- encontros permitidos por faixa;
- chefe do andar 10;
- chefe final do andar 15;
- modificadores de dificuldade;
- tabela ou contexto de recompensa.

## Pendências

- Definir duração-alvo de cada dungeon.
- Definir regra de retomada após fechar o jogo.
- Decidir se o progresso parcial faz parte do save.
- Definir o significado técnico de participantes no Party.

## Histórico de Alterações

- 2026-06-10: criado a partir do briefing de expansão de sistemas.
