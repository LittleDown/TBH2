# Consolidação do Repositório TBH2

## Status

Implementado em 2026-06-11 a partir da reavaliação completa do repositório.

## Escopo Analisado

- código Python em `src`;
- testes automatizados;
- save local e formatos anteriores;
- documentação modular ativa;
- demo visual de jornada;
- campanha, combate, inimigos, itens, progressão e persistência.

## Problemas Encontrados

- estratégias Agressivo, Balanceado e Defensivo ainda alteravam atributos;
- inimigos escalavam principalmente pelo nível do herói;
- nomes e ordem de mapas divergiam da documentação;
- o chefe técnico Capitão Ossonegro ainda era tratado como final;
- `CombatEngine` concentrava combate, XP, ouro, loot, mapa e renovação do encontro;
- save usava um agregado parcial, sem backup recuperável;
- progressão linear de XP e crescimento alto de atributos aceleravam demais a demo;
- itens não separavam definição base e instância gerada;
- UI ainda expunha controles de estratégia legados.

## Arquivos e Sistemas Alterados

- `src/balance.py`: fórmulas e constantes centralizadas;
- `src/maps/world.py`: Ato I, mapas, níveis e pools regionais;
- `src/enemies/enemies.py`: definições estáveis e encontros contextuais;
- `src/combat/combat.py`: resolução isolada de turnos e desfechos;
- `src/application`: sessão, encontro, loot, recompensa, progressão e save;
- `src/game_state.py`: agregado persistente v3;
- `src/save/save_manager.py`: escrita atômica, backup e recuperação;
- `src/items/items.py`: `ItemBaseDefinition`, `ItemInstance` e metadados futuros;
- `src/hero/hero.py`: build por equipamento e progressão revisada;
- `src/ui/main_window.py`: remoção do seletor legado e integração dos serviços;
- `tests/test_demo.py`: migração, combate, progressão, boss gate, loot e balanceamento.

## Legado Neutralizado

- o campo `strategy` de saves antigos é aceito e ignorado;
- novos saves não persistem estratégia;
- a UI não oferece troca de estratégia;
- Capitão Ossonegro permanece apenas em documentos históricos;
- saves v1 e v2 são migrados para `save_version: 3`.

## Arquitetura Atual

```text
MainWindow
  -> GameSession
     -> EncounterSystem
     -> CombatSystem
     -> RewardSystem
        -> LootSystem
     -> ProgressionSystem
  -> SaveCoordinator
     -> SaveManager
```

`CombatSystem` apenas aplica golpes e informa vitória ou derrota. A sessão
orquestra o ciclo, enquanto serviços específicos concedem recompensas e avançam
o mundo.

## Balanceamento

- XP necessário usa curva exponencial por fase;
- ganho por nível foi reduzido para preservar o peso do equipamento;
- monstros usam nível recomendado do mapa;
- vida, ataque, defesa, XP e ouro usam categoria e dificuldade;
- elites têm chance inicial de 5%;
- loot comum, elite e chefe possui chances distintas;
- autoequipamento usa `build_score` e respeita itens favoritos ou bloqueados.

## Validação

- compilação de `src` e `tests`;
- 22 testes automatizados aprovados;
- migração de save antigo;
- recuperação de save principal corrompido por backup;
- jornada visual preservada;
- vitória, derrota, loot, mapa e chefe cobertos.
- 100 campanhas simuladas concluíram o Ato I sem bloqueio no chefe.

## Limitações Conhecidas

- conteúdo ainda está em módulos Python, não em repositório declarativo;
- sprites regionais reutilizam placeholders existentes;
- carteira, inventário e equipamento ainda pertencem à entidade `Hero`;
- tempo médio de combate precisa de telemetria em sessões longas;
- encontro em andamento não é persistido;
- classes, raças, habilidades, dungeons e progresso offline continuam fora do escopo.

## Próxima Sprint Recomendada

1. Executar simulações longas de progressão e ajustar números em `balance.py`.
2. Criar sprites ou variações visuais para os pools regionais.
3. Extrair conteúdo para um repositório declarativo validado.
4. Adicionar telemetria local de duração de combate e taxa de derrota.
5. Preparar defaults persistentes de `class_id` e `race_id` sem ativar esses sistemas.
