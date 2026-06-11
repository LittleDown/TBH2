# Sistema de Itens

## Objetivo

Definir o modelo compartilhado de equipamentos, atributos, Poder, Build Score e sistemas automáticos de gerenciamento de itens.

O sistema de itens é a principal fonte de crescimento do personagem.

Seu objetivo não é apenas aumentar números.

Seu objetivo é criar decisões, especializações e metas de longo prazo.

---

## Status

In Progress

---

## Dependências

* Loot e Economia
* Atributos
* Raridades
* Modelo de Dados

---

# Filosofia de Itemização

O sistema de itens é o principal motor de progressão do TBH2.

O jogador não deve ficar forte apenas por subir de nível.

O verdadeiro crescimento deve vir de:

* equipamentos;
* sinergias;
* especialização da build;
* otimização dos atributos.

Todo item deve cumprir pelo menos uma das seguintes funções:

* aumentar poder;
* melhorar sobrevivência;
* fortalecer uma build existente;
* habilitar uma nova estratégia.

O jogador deve avaliar:

> "Este item fortalece minha build?"

e não apenas:

> "Este item possui um número maior?"

---

# Estrutura de Equipamentos

O sistema completo utiliza dez espaços de equipamento.

## Espaços Planejados

* Helm
* Weapon
* Weapon 2
* Chest
* Gloves
* Belt
* Boots
* Ring 1
* Ring 2
* Amulet

Os identificadores internos devem permanecer estáveis e independentes dos nomes exibidos ao jogador.

---

# Função dos Espaços

Cada espaço possui uma função principal dentro da progressão.

## Weapon

Principal fonte ofensiva.

Responsável pela maior parte do dano do personagem.

Prioriza:

* dano base;
* velocidade de ataque;
* efeitos ofensivos.

---

## Weapon 2

Espaço de especialização.

Pode representar:

* escudos;
* focos arcanos;
* adagas;
* segunda arma;
* tomos sagrados.

Disponibilidade depende da classe e do tipo de arma principal.

---

## Helm

Defesa secundária.

Focado em:

* atributos;
* resistência;
* utilidade.

---

## Chest

Maior fonte defensiva do personagem.

Focado em:

* vida;
* armadura;
* resistência mágica.

---

## Gloves

Precisão e agressividade.

Focado em:

* velocidade de ataque;
* chance crítica;
* precisão.

---

## Belt

Sustentação.

Focado em:

* vida;
* regeneração;
* resistência.

---

## Boots

Mobilidade.

Focado em:

* evasão;
* velocidade;
* recuperação.

---

## Rings

Especialização.

Os anéis direcionam a build.

Exemplos:

* crítico;
* fogo;
* gelo;
* sangramento;
* invocação.

---

## Amulet

Maior fonte de multiplicadores secundários.

Itens raros e lendários costumam possuir grande impacto neste espaço.

---

# Poder

Poder é um indicador simplificado da qualidade geral do item.

Objetivos:

* comparação rápida;
* feedback visual;
* suporte ao Auto-Equip.

Poder não substitui análise de build.

Ele existe apenas como referência inicial.

---

# Build Score

Build Score representa o valor real de um item para o personagem atual.

Ele considera:

* dano;
* vida;
* defesa;
* atributos;
* sinergias;
* tags;
* bônus de classe;
* efeitos especiais.

O Build Score deve ser mais relevante que o Poder sempre que ambos estiverem disponíveis.

---

# Tags de Equipamento

Itens podem possuir tags para auxiliar sistemas futuros.

Exemplos de tags:

Classe:

* Guerreiro
* Arqueiro
* Mago
* Curandeiro

Especialização:

* Crítico
* Sangramento
* Fogo
* Gelo
* Tanque
* Invocador

As tags auxiliam:

* filtros;
* Auto-Equip;
* recomendações;
* sinergias.

---

# Estado Atual

A versão atual utiliza:

* weapon;
* armor;
* accessory;
* Poder para comparação;
* Auto-Equip baseado em Poder.

Este sistema permanece válido até a expansão completa dos equipamentos.

---

# Sistema de Auto-Equip

O Auto-Equip existe para reduzir microgerenciamento.

Ele não deve substituir decisões importantes do jogador.

---

## Regras Gerais

O sistema deve:

* comparar apenas itens do mesmo espaço;
* explicar por que um item foi equipado;
* respeitar configurações do jogador;
* funcionar para heróis e companheiros.

---

## Critérios de Equipamento

Primeira versão:

* comparação baseada em Poder.

Versões futuras:

* comparação baseada em Build Score;
* análise de sinergias;
* análise de atributos;
* análise de conjuntos.

---

## Restrições

Nunca equipar automaticamente quando:

* reduzir significativamente o Build Score;
* quebrar bônus de conjunto;
* substituir item favoritado;
* contrariar regras definidas pelo jogador.

---

# Filosofia de Progressão

A frequência de upgrades deve mudar ao longo do jogo.

## Early Game

Trocas frequentes.

O jogador encontra melhorias constantemente.

---

## Mid Game

Trocas moderadas.

O jogador começa a avaliar qualidade dos atributos.

---

## Late Game

Trocas raras.

Os upgrades passam a ter grande impacto.

---

## Endgame

Busca por perfeição.

O foco deixa de ser encontrar qualquer upgrade.

O objetivo passa a ser encontrar o item ideal.

Essa sensação é inspirada em Diablo, Path of Exile e Last Epoch.

---

# Regras

* A expansão dos dez espaços deve ocorrer em sprint dedicada.
* Weapon 2 depende da definição de armas de duas mãos.
* Dois anéis são instâncias independentes.
* Novos espaços exigem migração de save.
* Não implementar afixos complexos antes da validação dos atributos principais.
* Build Score não substitui Poder na Fase 1.
* Tags não devem alterar estatísticas diretamente.

---

# Pendências

* Definir compatibilidade de armas.
* Definir regras para duas mãos.
* Definir critérios completos do Build Score.
* Definir critérios de desempate do Auto-Equip.
* Definir interface dos dez espaços.
* Planejar migração de armor e accessory para slots específicos.

---

# Histórico de Alterações

* 2026-06-10: expansão dos espaços registrada.
* 2026-06-10: introduzidos Poder e Build Score.
* 2026-06-10: introduzidas Tags de Equipamento.
* 2026-06-10: reorganização completa do sistema de itens.
