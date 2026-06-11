# Sistema de Herói

## Objetivo

Definir identidade, estado persistente, ciclo de vida e progressão individual do
herói.

## Status

In Progress

## Dependências

- [Progressão](../core/02_PROGRESSION.md)
- [Classes](02_CLASSES.md)
- [Atributos](03_ATTRIBUTES.md)
- [Habilidades](04_SKILLS.md)
- [Raças](05_RACES.md)

## Identidade

Na demo atual, o herói possui nome, nível, estratégia e equipamento. A criação de
personagem da Fase 2 adicionará raça e classe sem substituir a entidade existente.

Escolhas planejadas:

- raça: Humano, Elfo, Anão ou Meio-Orc;
- classe funcional: Tank, Healer ou DPS;
- nome e identidade visual.

## Estado

Estado atual:

- nível, XP, vida, ataque e defesa;
- ouro;
- estratégia;
- inventário e equipamentos;
- estatísticas de vitórias, mortes e chefes.

Estado futuro:

- `race_id`;
- `class_id`;
- STR, DEX, INT e CON;
- habilidades e passivas desbloqueadas;
- referências de companheiros ativos.

## Progressão

O nível continua sendo o eixo principal. Raça representa identidade persistente;
classe representa estilo e progressão; equipamentos e atributos compõem a build.

Novos sistemas devem estender o herói por dados e serviços, evitando subclasses
profundas ou cópias da lógica de progressão.

## Morte e Retorno

A derrota mantém o comportamento idle: registrar a morte, restaurar o herói e
retomar a jornada. Penalidades adicionais não fazem parte deste briefing.

## Regras

- Raça e classe são independentes.
- O combate continua automático por padrão.
- Nenhuma escolha de criação pode invalidar saves existentes.
- Fórmulas derivadas pertencem ao sistema de atributos.
- Passivas e habilidades não entram antes de suas fases do roadmap.

## Pendências

- Aprovar o fluxo visual de criação.
- Definir defaults de migração.
- Definir quando raça e classe podem ser alteradas.

## Histórico de Alterações

- 2026-06-10: incorporada a visão de criação de personagem do briefing.
- 2026-06-10: criado o template modular.
