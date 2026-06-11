# Relatório da Demo Técnica Jogável

## Objetivo

Registrar o estado da demo técnica jogável do TBH2, as fontes analisadas, as alterações realizadas, as limitações conhecidas e os próximos passos recomendados.

Este relatório descreve a implementação técnica existente.

Ele não substitui os documentos oficiais de design, arquitetura, progressão, combate ou roadmap.

---

## Status

Concluído — Demo Técnica

---

# Base Analisada

Foram inspecionadas três fontes principais:

1. PDF `TBH2 Demo Técnica Jogável`, utilizado como especificação funcional inicial.
2. RAR de aproximadamente 157 MB contendo o build Unity/IL2CPP `TaskBarHero 1.00.11`, executável e assets compilados, sem projeto-fonte editável.
3. RAR de aproximadamente 1,5 MB contendo saves ES3, backups e logs locais do build Unity.

Após análise, o repositório Python foi escolhido como base editável do projeto.

Motivos:

* código-fonte acessível;
* estrutura já existente em módulos;
* facilidade de alteração;
* compatibilidade com prototipagem rápida;
* menor dependência de assets compilados.

---

# Base Python Existente

O repositório Python já possuía módulos para:

* herói;
* inimigos;
* combate;
* itens;
* save;
* interface em CustomTkinter.

Essa base foi utilizada como ponto de partida para transformar o protótipo em uma demo técnica jogável.

---

# Alterações Realizadas

## Persistência

Foram implementados:

* `GameState`;
* save JSON versionado;
* migração automática do formato anterior de `save.json`;
* persistência de progresso;
* persistência de inventário;
* persistência de equipamentos;
* persistência de XP e ouro.

---

## Campanha

Foi implementada uma campanha inicial do Ato I com:

* dez mapas;
* dez vitórias necessárias por mapa;
* avanço progressivo entre mapas;
* encontro de chefe no encerramento do mapa 10;
* continuidade de combate livre após o fim da campanha.

---

## Chefe

Foi implementado um chefe técnico no final do Ato I:

* Capitão Ossonegro.

Observação:

O nome atual deve ser considerado temporário ou legado.

A documentação de mundo e chefes define o chefe conceitual do Ato I como:

* Senhor dos Ossos.

A nomenclatura final deve ser padronizada antes da consolidação do conteúdo.

---

## Progressão

Foram implementados:

* ganho de experiência;
* ganho de ouro;
* progressão de mapa;
* recompensas após combate;
* avanço automático do ciclo de jogo.

---

## Combate

Foram implementados:

* combate automático;
* estados de exploração, encontro, combate e recompensa;
* dano aplicado ao inimigo;
* dano recebido pelo herói;
* vitória;
* derrota;
* retorno automático à exploração.

---

## Estratégias de Combate

A demo técnica implementou:

* Agressivo;
* Balanceado;
* Defensivo.

Observação importante:

Esse sistema deve ser tratado como legado técnico.

A direção atual do projeto remove modos de combate selecionáveis.

A identidade de combate deve surgir de:

* equipamentos;
* atributos;
* classe;
* habilidades futuras;
* efeitos especiais;
* Build Score.

Portanto, `StrategySystem`, `CombatStrategy` e comandos de troca de estratégia devem ser removidos ou ignorados em fases futuras.

---

## Itens e Loot

Foram implementados:

* inventário persistente;
* equipamento manual;
* equipamento automático;
* loot escalável;
* raridades:

  * Comum;
  * Raro;
  * Épico;
* painel de equipamentos com:

  * Arma;
  * Armadura;
  * Acessório;
* inventário visual em grade 5x4 com vinte espaços.

Observação:

O sistema atual ainda utiliza slots simplificados.

A documentação futura prevê expansão para:

* weapon;
* offhand;
* helmet;
* chest;
* gloves;
* belt;
* boots;
* ring_1;
* ring_2;
* amulet.

---

## Interface

Foi implementada uma interface lateral de 360x600 com áreas principais:

* Hero;
* Inventory;
* Map.

A interface foi adaptada para funcionar como janela compacta de Taskbar Companion.

---

## Estados Visuais

Foi implementado um controlador visual isolado com os estados:

* `explore`;
* `encounter`;
* `fight`;
* `reward`.

Esses estados sustentam o ciclo visual principal:

Exploração
↓
Encontro
↓
Combate
↓
Recompensa
↓
Exploração

---

## Animações

Foram implementados:

* caminhada horizontal em loop;
* caminhada em dois frames;
* avanço de ataque;
* flash de impacto;
* dano flutuante;
* queda do inimigo;
* pose de vitória;
* entrada do inimigo pela direita;
* retorno automático à exploração.

---

## Loop Visual

O loop visual utiliza:

* `after()`;
* `time.perf_counter()`;
* delta time limitado.

Essa abordagem foi inspirada na referência JavaScript, mas adaptada à interface Python.

---

## Exploração Viva

Foram implementados elementos para simular jornada contínua:

* camada móvel sobre ambientes;
* parallax na Estrada Abandonada;
* movimento em profundidade com camadas de 20%, 50% e 100%;
* elementos procedurais leves reciclados ao sair da tela;
* desaceleração gradual antes de encontros;
* aceleração após recompensas.

---

## Ambientação

Foi implementado um kit modular inicial em pixel art com:

* árvores;
* pedras;
* vegetação;
* vestígios de estrada;
* rastros;
* fogueira;
* espada;
* carroça;
* bandeira.

Também foram adicionados eventos ambientais ocasionais:

* corvos;
* folhas;
* poeira.

---

## Mapas

Foram criados ambientes distintos para os dez mapas do Ato I.

Observação:

Apenas a Estrada Abandonada possui kit modular inicial mais desenvolvido.

Os demais mapas ainda exigem refinamento artístico, kits próprios e maior identidade visual.

---

## Testes

Foram adicionados testes automatizados para:

* combate;
* campanha;
* estratégias;
* persistência.

Observação:

Os testes de estratégia devem ser revisados ou removidos quando o sistema legado de estratégias for retirado.

---

# Referência JavaScript

O projeto `thb2-main.zip` foi utilizado somente como referência técnica visual.

Foram adaptados conceitos como:

* cálculo por delta time;
* alternância de frames;
* avanço temporário de ataque;
* aproximação do inimigo;
* fluxo `spawn → fight → clear`.

Nenhuma regra de combate ou arquitetura do projeto JavaScript foi portada diretamente.

No Python, o fluxo foi integrado à estrutura existente como:

Exploração
↓
Encontro
↓
Combate
↓
Recompensa
↓
Exploração

Mantendo:

* `CombatEngine`;
* campanha;
* XP;
* ouro;
* loot;
* mapas;
* save.

---

# Limitações Conhecidas

## Arte

* frames animados do herói ainda são temporários;
* sprites de inimigos ainda são provisórios;
* chefe ainda utiliza asset técnico;
* somente a Estrada Abandonada possui kit modular inicial mais completo;
* os demais mapas precisam de identidade visual mais forte.

---

## Tecnologia Visual

A interface atual não possui:

* áudio;
* interpolação avançada;
* partículas complexas;
* blend real de opacidade no Canvas do Tkinter;
* sistema avançado de iluminação;
* transições visuais completas entre mapas.

---

## Conteúdo

* campanha termina no Ato I;
* não existem Ato II e Ato III jogáveis;
* monstros ainda são limitados;
* chefes ainda precisam ser alinhados à documentação oficial;
* loot ainda não possui afixos avançados;
* equipamentos ainda usam slots simplificados.

---

## Arquitetura

* conteúdo ainda está definido em módulos Python;
* ainda não há conteúdo declarativo em JSON;
* `CombatEngine` concentra responsabilidades demais;
* UI ainda participa de parte do fluxo;
* save precisa evoluir para `GameState` completo;
* estratégia de combate ainda aparece como legado técnico.

---

## Progressão

* não há progressão offline;
* fórmulas precisam de balanceamento;
* curva de XP precisa ser testada;
* recompensas de ouro precisam ser calibradas;
* chefe final do Ato I precisa de validação real.

---

# Dívidas Técnicas

As principais dívidas técnicas identificadas são:

1. Remover sistema de estratégias de combate.
2. Separar melhor combate, recompensa, loot e progressão.
3. Padronizar o chefe do Ato I.
4. Expandir equipamentos para slots oficiais.
5. Separar ItemBase de ItemInstance.
6. Separar MonsterDefinition de MonsterInstance.
7. Consolidar `GameState` como agregado persistente.
8. Criar ou preparar ContentRepository.
9. Revisar testes ligados a sistemas legados.
10. Validar balanceamento da campanha.

---

# Próximos Passos Recomendados

## 1. Consolidar Fase 1

Prioridade:

* estabilidade;
* save;
* loop;
* progressão;
* clareza visual;
* balanceamento inicial.

---

## 2. Remover Estratégias Legadas

Remover ou desativar:

* Agressivo;
* Balanceado;
* Defensivo;
* `CombatStrategy`;
* `StrategySystem`;
* comandos de troca de estratégia;
* testes específicos desse sistema.

Substituir por leitura de build baseada em:

* equipamentos;
* atributos;
* Power;
* Build Score.

---

## 3. Padronizar Chefe do Ato I

Decidir nomenclatura oficial:

* Capitão Ossonegro;
* Senhor dos Ossos.

A recomendação atual é manter `Senhor dos Ossos` como chefe oficial do Ato I e tratar `Capitão Ossonegro` como nome técnico temporário ou elite nomeado futuro.

---

## 4. Melhorar Assets Autorais

Substituir frames temporários por sprites consistentes para:

* herói;
* inimigos comuns;
* elites;
* chefe;
* loot;
* efeitos de combate.

---

## 5. Validar Longa Duração

Criar testes e sessões reais para medir:

* tempo médio por mapa;
* taxa de vitória;
* ganho médio de XP;
* ganho médio de ouro;
* frequência de loot;
* dificuldade do chefe;
* estabilidade da janela aberta por longos períodos.

---

## 6. Preparar Build Windows

Criar build com PyInstaller apenas após validação mecânica.

Não empacotar antes de estabilizar:

* save;
* assets;
* dependências;
* caminho de arquivos;
* logs;
* comportamento de fechamento.

---

# Critérios de Sucesso da Demo Técnica

A demo técnica será considerada validada quando:

* o ciclo principal funcionar continuamente;
* o jogador entender os estados da jornada;
* a campanha do Ato I puder ser concluída;
* o save preservar progresso corretamente;
* o jogo permanecer estável em janela compacta;
* o chefe funcionar como bloqueio justo;
* loot e equipamento tiverem impacto perceptível;
* sistemas legados estiverem identificados e controlados.

---

# Conclusão

A demo técnica cumpriu sua função principal:

transformar o TBH2 em um protótipo jogável com exploração, combate, loot, progressão, save e feedback visual.

O projeto agora possui uma base funcional.

A próxima etapa não deve ser adicionar sistemas grandes.

A próxima etapa deve ser consolidar a base, remover legados conflitantes, padronizar o design oficial e validar o loop principal com balanceamento e arte mais consistentes.

---

# Histórico de Alterações

* 2026-06-10: relatório técnico inicial produzido.
* 2026-06-10: base Python definida como repositório editável.
* 2026-06-10: demo técnica jogável registrada.
* 2026-06-10: estratégias de combate marcadas como legado técnico.
* 2026-06-10: próximos passos de consolidação definidos.
