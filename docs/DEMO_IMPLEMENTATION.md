# Relatório da Demo Técnica Jogável

## Base analisada

Foram inspecionadas três fontes:

1. O PDF `TBH2 Demo Técnica Jogável`, usado como especificação funcional.
2. O RAR de aproximadamente 157 MB, que contém o build Unity/IL2CPP
   `TaskBarHero 1.00.11`, executável e assets compilados, mas não o projeto-fonte.
3. O RAR de aproximadamente 1,5 MB, que contém saves ES3, backups e logs locais
   do build Unity.

O repositório Python foi escolhido como base editável. Ele já possuía módulos de
herói, inimigos, combate, itens, save e uma interface CustomTkinter.

## Alterações realizadas

- introdução de `GameState` e save JSON versionado;
- migração automática do formato anterior de `save.json`;
- campanha completa do Ato I com dez mapas e dez vitórias por mapa;
- encontro do chefe Capitão Ossonegro no último progresso do mapa 10;
- recompensas de XP e ouro;
- estratégias Agressivo, Balanceado e Defensivo;
- inventário persistente e equipamento manual ou automático;
- loot escalável com raridades Comum, Raro e Épico;
- interface lateral de 360x600 com áreas Hero, Inventory e Map;
- sprites temporários em pixel art para herói, inimigos, chefe e loot;
- painel de equipamentos com Arma, Armadura e Acessório;
- inventário fixo em grade 5x4 com vinte espaços visuais;
- estado principal de exploração com caminhada horizontal em loop;
- transições visuais entre exploração, encontro, combate e recompensa;
- controlador visual isolado com estados `explore`, `encounter`, `fight` e
  `reward`;
- loop visual com `after()`, `time.perf_counter()` e delta time limitado;
- caminhada em dois frames, avanço de ataque, flash de impacto, dano flutuante,
  queda do inimigo e pose de vitória;
- entrada do inimigo pela direita e retorno automático à exploração;
- camada móvel sobre os ambientes para simular caminhada contínua;
- ambientes distintos para os dez mapas do Ato I;
- testes automatizados para combate, campanha, estratégias e persistência.

## Referência JavaScript

O projeto `thb2-main.zip` foi usado somente como referência técnica. Foram
adaptados o cálculo por delta time, a alternância de frames, o avanço temporário
dos ataques, a aproximação do inimigo e o fluxo `spawn → fight → clear`.

Nenhuma regra de combate ou arquitetura do jogo JavaScript foi portada. No
Python, o fluxo foi integrado à arquitetura existente como
`explore → encounter → fight → reward → explore`, mantendo o `CombatEngine`,
campanha, XP, ouro, loot, mapas e save originais.

## Limitações conhecidas

- os frames animados do herói ainda são assets temporários da referência;
- os ambientes usam formas simples e paletas temporárias;
- não existem áudio, interpolação avançada, partículas complexas ou blend real
  de opacidade no Canvas do Tkinter;
- o conteúdo está definido em módulos Python, ainda não em arquivos declarativos;
- não há progressão offline;
- a campanha termina no Ato I e permanece em combate livre após o chefe;
- as fórmulas precisam de uma rodada posterior de balanceamento.

## Próximos passos recomendados

1. Substituir os frames temporários por sprites autorais consistentes.
2. Adicionar animações próprias para cada família de inimigo e para o chefe.
3. Incluir efeitos leves de partículas, sombra e transição entre mapas.
4. Adicionar testes de longa duração para balancear progressão e chefe.
5. Criar build Windows com PyInstaller depois da validação mecânica.
