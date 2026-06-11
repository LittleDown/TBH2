# Loot e Economia

## Objetivo

Definir a filosofia, fluxo e responsabilidades do sistema de loot e economia do TBH2.

Este documento descreve como recompensas, ouro e drops sustentam a progressão do jogador.

O loot é um dos principais motores de progressão do jogo.

O jogador não deve ficar forte apenas por subir de nível.

O verdadeiro crescimento de poder deve vir principalmente dos equipamentos encontrados durante a jornada.

---

## Status

In Progress

---

## Dependências

* [Gameplay central](01_CORE_GAMEPLAY.md)
* [Progressão](02_PROGRESSION.md)
* [Combate](03_COMBAT.md)
* [Sistema de itens](../items/01_ITEM_SYSTEM.md)
* [Raridades](../items/05_RARITIES.md)
* [Sistema de monstros](../monsters/01_MONSTER_SYSTEM.md)
* [Chefes](../monsters/04_BOSSES.md)
* [Dificuldades](../maps/05_DIFFICULTIES.md)
* [Fórmulas de balanceamento](../technical/03_BALANCE_FORMULAS.md)

---

# Escopo deste Documento

Este documento define:

* filosofia de loot;
* filosofia de economia;
* fluxo conceitual de geração de recompensas;
* relação entre monstros, chefes, mapas e loot;
* papel do ouro;
* fontes de ouro;
* usos planejados do ouro;
* relação entre loot, equipamentos e progressão;
* critérios de sucesso do sistema econômico.

---

# Fora do Escopo

Este documento não deve definir:

* fórmulas finais de drop;
* chances definitivas de raridade;
* lista completa de itens;
* lista completa de afixos;
* valores finais de ouro;
* custo final de upgrades;
* fórmula final de Build Score;
* implementação técnica de Auto-Equip;
* tabelas definitivas de loot por monstro.

Esses assuntos pertencem aos documentos proprietários de cada domínio.

---

# Visão Geral

O sistema de loot transforma combate em progressão.

Ao derrotar inimigos, elites e chefes, o jogador recebe recompensas que alimentam o crescimento do personagem.

Recompensas principais:

* experiência;
* ouro;
* equipamentos;
* progresso de mapa;
* possíveis eventos especiais.

O loot deve gerar expectativa constante.

A pergunta desejada após cada vitória é:

> "Será que o próximo item melhora minha build?"

---

# Filosofia de Loot

O loot do TBH2 é inspirado em ARPGs como:

* Diablo;
* Path of Exile;
* Last Epoch.

Adaptado ao formato Idle Companion.

O jogador não deve precisar clicar repetidamente para obter valor.

O jogo deve apresentar recompensas de forma clara, legível e compatível com uma janela compacta.

Loot saudável deve gerar:

* expectativa;
* surpresa;
* comparação;
* decisão;
* evolução.

---

# Papel do Loot na Progressão

Loot é a principal ponte entre combate e crescimento real de poder.

O nível fornece crescimento constante.

O equipamento fornece saltos de poder.

A progressão saudável acontece quando o jogador percebe que um item novo pode mudar sua eficiência.

Equipamentos devem influenciar:

* dano;
* sobrevivência;
* atributos;
* especialização;
* sinergia;
* Build Score.

---

# Fontes de Loot

Loot pode ser obtido através de:

* monstros comuns;
* campeões;
* elites;
* chefes;
* dungeons futuras;
* eventos futuros;
* recompensas de marco;
* venda ou conversão futura de itens.

A qualidade e quantidade de loot devem variar conforme o desafio.

---

# Hierarquia de Recompensa

A recompensa deve acompanhar o risco.

Ordem conceitual:

```text
Monstro comum
↓
Campeão
↓
Elite
↓
Elite nomeado
↓
Chefe
↓
Chefe de dungeon
↓
Chefe de endgame
```

Quanto maior o risco, maior deve ser o potencial de recompensa.

Potencial não significa garantia.

Um chefe deve ter mais chance de gerar bons itens, mas não precisa garantir sempre um item raro.

---

# Contexto de Loot

A geração de loot deve considerar o contexto do encontro.

Fatores relevantes:

* ato atual;
* mapa atual;
* dificuldade atual;
* nível da área;
* categoria do inimigo;
* tipo de encontro;
* chefe ou elite;
* modificadores futuros;
* eventos futuros.

O loot não deve depender apenas do nível do herói.

O mundo deve influenciar a recompensa.

---

# Fluxo Conceitual de Geração de Loot

A geração de loot deve seguir uma ordem clara.

---

## 1. Determinar Fonte da Recompensa

O sistema identifica a origem da vitória.

Exemplos:

* monstro comum;
* elite;
* chefe;
* dungeon futura.

Essa fonte define o potencial inicial da recompensa.

---

## 2. Determinar Quantidade de Drops

O sistema decide se haverá item e quantos itens podem cair.

A quantidade deve variar conforme:

* categoria do inimigo;
* dificuldade;
* chefe ou elite;
* bônus futuros.

Valores finais pertencem ao documento de balanceamento.

---

## 3. Determinar Categoria do Item

O sistema seleciona o tipo geral de item.

Exemplos:

* arma;
* armadura;
* acessório;
* consumível futuro;
* material futuro.

A lista completa pertence ao Sistema de Itens.

---

## 4. Determinar Slot ou Família

O sistema seleciona o slot ou família do item.

Exemplos:

* weapon;
* offhand;
* helmet;
* chest;
* gloves;
* belt;
* boots;
* ring;
* amulet.

A definição oficial dos slots pertence ao Sistema de Itens.

---

## 5. Determinar Raridade

O sistema sorteia a raridade do item.

A raridade define potencial, complexidade e expectativa.

Exemplos de raridades planejadas:

* Comum;
* Mágico;
* Raro;
* Épico;
* Lendário;
* Set;
* Mítico futuro.

As regras detalhadas pertencem ao documento de Raridades.

---

## 6. Determinar Item Base

O sistema escolhe o item base.

Exemplos:

* Espada Curta;
* Espada Longa;
* Arco Simples;
* Capuz;
* Peitoral de Couro;
* Anel de Ferro.

O item base define identidade, slot e características iniciais.

A lista completa pertence ao Sistema de Itens.

---

## 7. Gerar Instância do Item

O sistema cria uma instância concreta do item.

A instância deve preservar:

* item_id;
* base_item_id;
* raridade;
* item_level;
* atributos gerados;
* afixos;
* tags;
* origem;
* data de criação.

Detalhes pertencem ao Modelo de Dados e ao Sistema de Itens.

---

## 8. Avaliar Impacto na Build

Após gerar o item, o sistema pode calcular ou solicitar o cálculo de:

* Power;
* Build Score;
* sinergia com classe;
* sinergia com atributos;
* impacto em equipamentos atuais.

O cálculo detalhado pertence ao Sistema de Itens e às Fórmulas de Balanceamento.

---

# Raridade

Raridade representa potencial e complexidade.

Raridade não deve significar automaticamente que um item é melhor para qualquer personagem.

Um item raro pode ser ruim para uma build específica.

Um item mágico pode ser útil se possuir boa sinergia.

Regra central:

> Raridade aumenta potencial, não garante utilidade.

As regras completas pertencem a:

* [Raridades](../items/05_RARITIES.md)

---

# Item Level

Item Level representa o nível de poder base do item.

Ele deve ser influenciado por:

* nível da área;
* mapa;
* ato;
* dificuldade;
* tipo do inimigo;
* fonte da recompensa.

Item Level não deve ser confundido com raridade.

Um item de nível alto pode ser comum.

Um item raro de nível baixo pode perder relevância com o avanço da campanha.

---

# Loot por Dificuldade

Dificuldades superiores devem aumentar o potencial do loot.

Elas podem influenciar:

* item level;
* qualidade média;
* chance de raridades superiores;
* quantidade de ouro;
* recompensa de chefes;
* frequência de elites.

Dificuldade maior não deve garantir item perfeito.

Ela deve aumentar o potencial de recompensa.

---

# Loot por Chefe

Chefes são pontos de expectativa.

Ao derrotar um chefe, o jogador deve sentir que venceu um marco importante.

Chefes devem oferecer:

* maior chance de itens relevantes;
* maior quantidade de ouro;
* recompensa superior;
* possível loot exclusivo futuro;
* desbloqueios de campanha ou dificuldade.

As regras de chefes pertencem a:

* [Chefes](../monsters/04_BOSSES.md)

---

# Loot por Elite

Elites devem quebrar a rotina da exploração.

Eles devem ter recompensa superior a monstros comuns.

Função:

* gerar expectativa;
* testar build;
* acelerar progressão;
* oferecer chance melhor de itens relevantes.

As regras de elites pertencem a:

* [Monstros elite](../monsters/03_ELITE_MONSTERS.md)

---

# Economia

A economia existe para sustentar progressão de longo prazo.

O ouro deve possuir valor em todas as etapas do jogo.

O jogador nunca deve atingir um ponto onde acumular ouro deixa de importar.

Uma economia saudável possui:

* fontes de geração;
* fontes de consumo;
* limites de inflação;
* utilidade contínua.

---

# Fontes de Ouro

Ouro pode ser gerado por:

* monstros comuns;
* elites;
* chefes;
* venda de equipamentos;
* eventos futuros;
* dungeons futuras;
* missões futuras;
* conquistas futuras;
* marcos de progressão.

As quantidades finais pertencem ao documento de balanceamento.

---

# Consumo de Ouro

Ouro deve sair da economia de forma constante.

Usos planejados:

* melhoria de equipamentos;
* encantamentos;
* reroll de atributos;
* craft futuro;
* remoção de gemas futura;
* reset de talentos futuro;
* serviços especiais;
* upgrades de sistemas futuros.

Nem todos esses usos pertencem ao MVP.

A função deste documento é preservar a necessidade de consumo econômico.

Sem consumo, a moeda perde valor.

---

# Filosofia do Ouro

O ouro deve acompanhar o crescimento do jogador.

No início, ele deve parecer útil e limitado.

No meio do jogo, deve sustentar decisões.

No longo prazo, deve alimentar sistemas de otimização.

O objetivo não é enriquecer indefinidamente.

O objetivo é criar decisões de uso.

---

# Venda de Itens

A venda de itens deve transformar loot não utilizado em valor econômico.

Funções:

* reduzir excesso de inventário;
* gerar ouro;
* dar valor mínimo a drops ruins;
* sustentar economia.

Itens vendidos devem ser removidos do inventário.

Itens favoritados ou bloqueados não devem ser vendidos automaticamente.

---

# Auto-Equip

Auto-Equip deve ser opcional.

Seu objetivo é reduzir microgerenciamento sem remover escolhas do jogador.

O sistema pode sugerir ou aplicar troca automática quando um item for claramente melhor para a build atual.

Regras conceituais:

* não substituir item favorito;
* não substituir item bloqueado;
* não quebrar conjunto ativo sem ganho relevante;
* não equipar item que reduza Build Score;
* priorizar sinergia, não apenas Power.

Detalhes de implementação pertencem a:

* [Sistema de itens](../items/01_ITEM_SYSTEM.md)

---

# Build Score

Build Score representa o valor real de um item para o herói atual.

Ele deve considerar:

* poder bruto;
* atributos;
* classe;
* tags;
* sinergias;
* efeitos especiais;
* habilidades futuras.

Build Score não é definido por este documento.

Este documento apenas estabelece que loot e Auto-Equip devem respeitar Build Score.

Fórmulas pertencem a:

* [Fórmulas de balanceamento](../technical/03_BALANCE_FORMULAS.md)

---

# Build Tags

Build Tags ajudam o sistema a reconhecer sinergias.

Exemplos conceituais:

* Guerreiro;
* Arqueiro;
* Mago;
* Curandeiro;
* Crítico;
* Sangramento;
* Fogo;
* Gelo;
* Tanque;
* Invocação.

A lista final de tags pertence ao Sistema de Itens.

---

# Relação com Progressão

Loot e economia alimentam a progressão.

O jogador deve sempre possuir algo a perseguir:

* item melhor;
* ouro para upgrade;
* raridade superior;
* item para outro slot;
* build mais eficiente;
* preparação para chefe.

Sem loot relevante, a progressão perde significado.

---

# Relação com Combate

Combate gera recompensas.

Mas o combate não deve concentrar sozinho a lógica de loot.

Fluxo esperado:

```text
Combate vencido
↓
RewardSystem
↓
LootSystem
↓
ItemInstance gerado
↓
Inventory atualizado
↓
Auto-Equip opcional
↓
Save solicitado
```

Essa separação evita que o sistema de combate vire responsável por toda a progressão.

---

# Relação com Save

Itens gerados devem ser persistidos como instâncias.

O save deve preservar:

* item_id;
* base_item_id;
* raridade;
* item_level;
* afixos;
* tags;
* estado equipado;
* estado favorito;
* estado bloqueado.

O save não deve armazenar a definição completa de todos os itens base.

As definições pertencem ao conteúdo do jogo.

---

# Critérios de Sucesso

O sistema de loot e economia será considerado saudável quando:

* encontrar itens for empolgante;
* equipamentos tiverem impacto real;
* o jogador desejar continuar farmando;
* ouro possuir valor constante;
* drops ruins ainda tiverem utilidade econômica;
* Auto-Equip tomar decisões coerentes;
* diferentes builds valorizarem itens diferentes;
* chefes gerarem expectativa;
* elites quebrarem a rotina;
* a progressão não depender apenas de nível.

---

# Regras

* Loot deve ser uma das principais fontes de progressão.
* Equipamentos devem ter impacto perceptível.
* Raridade aumenta potencial, não garante utilidade.
* Ouro deve possuir fontes e consumos.
* Dificuldades superiores aumentam potencial de recompensa.
* Chefes devem possuir recompensas superiores.
* Elites devem possuir recompensas melhores que comuns.
* Build Score deve orientar avaliação de itens.
* Auto-Equip deve ser opcional.
* Itens favoritados ou bloqueados devem ser preservados.
* Fórmulas finais não pertencem a este documento.
* Listas completas de itens não pertencem a este documento.

---

# Dados

Reservado para referências conceituais.

Tabelas finais, chances e fórmulas pertencem aos documentos técnicos e de itens.

---

# Pendências

* Definir tabelas finais no sistema de itens.
* Definir raridades finais no documento de raridades.
* Definir fórmulas de drop no documento de balanceamento.
* Definir valores de ouro no documento de balanceamento.
* Definir custos futuros de consumo de ouro.
* Definir regras completas de Auto-Equip no sistema de itens.
* Definir tags oficiais de build.
* Definir integração final entre RewardSystem, LootSystem e Inventory.
* Definir comportamento de venda automática futura, se existir.

---

# Histórico de Alterações

* 2026-06-10: documento inicial de loot e economia criado.
* 2026-06-10: loot definido como principal motor de progressão.
* 2026-06-10: ouro definido como recurso de longo prazo.
* 2026-06-10: Build Score incorporado como referência de avaliação.
* 2026-06-10: documento reestruturado para separar loot, raridades, fórmulas, itens e Auto-Equip.
