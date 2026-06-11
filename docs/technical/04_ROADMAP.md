# Roadmap

## Objetivo

Organizar a expansão incremental do TBH2 sem comprometer sua identidade de RPG
idle compacto. Cada fase deve preservar um jogo executável e validar diversão,
clareza e custo de manutenção antes da fase seguinte.

## Status

In Progress

## Dependências

- [Gameplay central](../core/01_CORE_GAMEPLAY.md)
- [Arquitetura técnica](05_ARCHITECTURE.md)
- [Sistema de herói](../heroes/01_HERO_SYSTEM.md)
- [Dungeons](../maps/06_DUNGEONS.md)

## Visão Geral

O núcleo prioritário permanece:

`Exploração → Combate → Loot → Progressão`

Raças, classes, habilidades, resistências, companheiros e modos de grupo são
camadas posteriores. Nenhuma fase deve ser iniciada apenas porque aparece neste
roadmap.

## Fases

### Fase 1 - Núcleo Jogável

Escopo:

- exploração contínua;
- combate automático;
- loot e equipamento;
- experiência, ouro e progressão de mapas;
- feedback visual para encontro, ataque, dano, vitória e retorno à exploração.

Critério de saída:

- o ciclo completo funciona repetidamente sem intervenção obrigatória;
- save e progressão não apresentam regressões;
- o jogador identifica claramente cada estado da jornada.

Status: implementado na demo técnica; ainda sujeito a balanceamento e arte final.

### Fase 2 - Identidade do Herói

Escopo:

- criação de personagem;
- raças Humano, Elfo, Anão e Meio-Orc;
- arquétipos Tank, Healer e DPS;
- atributos primários STR, DEX, INT e CON;
- migração compatível dos saves existentes.

Critério de entrada: Fase 1 validada por sessões de jogo.

Critério de saída:

- cada escolha muda ao menos uma decisão de build;
- nenhuma opção é obrigatória para completar o conteúdo base;
- atributos derivados possuem fórmulas testadas;
- saves antigos recebem defaults neutros.

### Fase 3 - Habilidades

Escopo:

- habilidades automáticas por classe;
- autocast configurável;
- ativação e desativação individual;
- passivas raciais;
- prioridade de habilidades.

Critério de entrada: raças, classes e atributos estáveis.

Critério de saída:

- o combate continua legível na janela compacta;
- cada classe possui uma rotação automática distinta;
- desativar uma habilidade produz consequência compreensível.

### Fase 4 - Combate Avançado

Escopo:

- dano físico, mágico e puro;
- armor, spell armor, evasion, parry e redução de controle;
- crítico, velocidade de ataque, cura e regeneração;
- revisão de balanceamento de inimigos e equipamentos.

Critério de entrada: habilidades validadas e eventos de combate estruturados.

Critério de saída:

- ordem de resolução documentada e coberta por testes;
- feedback visual diferencia categorias relevantes;
- complexidade adicional gera decisões, não apenas números maiores.

### Fase 5 - Grupo e Dungeons

Escopo:

- até três NPCs companheiros;
- equipamentos e progressão sincronizada dos companheiros;
- Solo AFK Dungeon com quinze andares;
- Party Dungeon para até quatro participantes, também jogável solo;
- recompensas e dificuldade superiores no modo Party.

Critério de entrada: combate avançado estável e arquitetura preparada para mais de
dois participantes.

Critério de saída:

- composição de grupo altera estratégia;
- o modo solo permanece completo;
- Party Dungeon reutiliza os sistemas existentes;
- escalonamento não exige um segundo motor de combate.

## Regras

- Cada sistema novo deve agregar decisão, reforçar a fantasia de RPG e aproveitar
  a estrutura atual.
- A simplicidade de uso e a compatibilidade com Taskbar têm prioridade sobre
  quantidade de sistemas.
- Não desenvolver duas fases simultaneamente quando compartilham contratos ainda
  instáveis.
- Toda mudança persistente exige default ou migração de save.
- Fórmulas numéricas pertencem ao documento de balanceamento.

## Riscos

- excesso de estatísticas reduzir a legibilidade;
- classes e raças virarem apenas bônus passivos sem decisão;
- habilidades automáticas transformarem o combate em ruído visual;
- Party Dungeon exigir infraestrutura online antes da validação do modo solo;
- expansão de equipamentos ultrapassar o espaço disponível na interface.

## Próxima Sprint Recomendada

Finalizar a validação da Fase 1. Depois, prototipar somente o modelo de identidade
da Fase 2 com defaults neutros, sem habilidades, resistências ou companheiros.

## Histórico de Alterações

- 2026-06-10: roadmap expandido a partir do briefing de expansão de sistemas.
- 2026-06-10: criado o template modular.
