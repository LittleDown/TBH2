# Loot e Economia

## Objetivo

Definir a geração de loot, economia, ouro, progressão de equipamentos e sistemas automáticos de gerenciamento de itens do TBH2.

O loot é o principal motor de progressão do jogo.

O jogador não deve ficar forte apenas por subir de nível.

O verdadeiro crescimento de poder deve vir dos equipamentos encontrados ao longo da jornada.

---

# Status

Draft

---

# Filosofia de Loot

Inspirado em:

* Diablo
* Path of Exile
* Last Epoch

O loot deve gerar expectativa.

Ao derrotar um inimigo, o jogador deve sentir:

> "Talvez o próximo item seja exatamente o que eu preciso."

O loot é a principal recompensa do combate.

---

# Filosofia de Economia

A economia existe para sustentar a progressão.

O ouro deve possuir valor em todas as etapas do jogo.

O jogador nunca deve atingir um ponto onde acumular ouro deixa de ser relevante.

Todo sistema econômico deve possuir:

* fontes de geração;
* fontes de consumo;
* progressão contínua.

---

# Estrutura de Loot

Todo inimigo possui uma tabela de loot baseada em:

* tipo do inimigo;
* nível do inimigo;
* raridade do inimigo;
* região atual;
* dificuldade atual;
* modificadores temporários.

---

# Geração de Loot

A geração ocorre em múltiplas etapas.

---

## Etapa 1 - Quantidade de Itens

O sistema define quantos itens serão gerados.

Exemplo inicial:

| Tipo  | Quantidade |
| ----- | ---------- |
| Comum | 0 - 2      |
| Elite | 1 - 4      |
| Boss  | 4 - 8      |

Os valores finais serão definidos em BALANCE_FORMULAS.md.

---

## Etapa 2 - Escolha do Slot

O sistema seleciona o tipo do item.

Exemplos:

* Arma Principal
* Arma Secundária
* Capacete
* Peitoral
* Luvas
* Cinto
* Botas
* Anel
* Amuleto

---

## Etapa 3 - Escolha da Raridade

O sistema sorteia a raridade.

Exemplo inicial:

| Raridade | Chance |
| -------- | ------ |
| Comum    | 60%    |
| Mágico   | 25%    |
| Raro     | 10%    |
| Épico    | 4%     |
| Lendário | 1%     |

As chances podem ser modificadas por:

* dificuldade;
* eventos;
* chefes;
* bônus temporários.

---

## Etapa 4 - Escolha do Item Base

Exemplo:

Espadas:

* Espada Curta
* Espada Longa
* Sabre
* Claymore

Capacetes:

* Capuz
* Elmo de Couro
* Elmo de Ferro

O item base define estatísticas mínimas.

---

## Etapa 5 - Geração de Atributos

Atributos são adicionados conforme a raridade.

Exemplo:

Espada Rara

* +35 Dano
* +12% Velocidade de Ataque
* +8% Chance Crítica

---

## Etapa 6 - Escalonamento

O item recebe modificadores baseados em:

* nível do item;
* tier da área;
* dificuldade;
* progressão mundial.

---

# Sistema de Raridades

## Comum

Cor:

Branco

Características:

* estatísticas básicas;
* sem modificadores especiais.

---

## Mágico

Cor:

Azul

Características:

* poucos atributos adicionais.

---

## Raro

Cor:

Amarelo

Características:

* múltiplos atributos.

---

## Épico

Cor:

Roxo

Características:

* atributos elevados;
* possibilidade de sinergias.

---

## Lendário

Cor:

Laranja

Características:

* efeito especial único;
* modificador exclusivo.

---

## Set

Cor:

Verde

Características:

* bônus por quantidade equipada.

---

## Mítico

Cor:

Vermelho

Características:

* itens extremamente raros;
* definem builds.

---

# Escalonamento de Equipamentos

O poder dos itens cresce através de três fatores.

---

## Nível do Item

Exemplo:

Espada Nível 10

20 Dano

Espada Nível 50

120 Dano

---

## Raridade

Exemplo:

Comum

1 atributo

Raro

3 atributos

Épico

4 atributos

Lendário

5 atributos + efeito especial

---

## Tier Mundial

Tier 1

100%

Tier 2

150%

Tier 3

220%

Tier 4

350%

---

# Ouro

## Fontes de Ouro

* monstros;
* elites;
* chefes;
* venda de equipamentos;
* eventos;
* missões;
* conquistas;
* marcos de progressão.

---

## Filosofia de Ouro

O ouro deve acompanhar o crescimento do jogador.

O objetivo não é enriquecer indefinidamente.

O objetivo é alimentar novos sistemas de progressão.

---

# Consumo de Ouro

Ouro deve sair constantemente da economia.

Principais usos:

* melhoria de equipamentos;
* encantamentos;
* reroll de atributos;
* craft;
* remoção de gemas;
* reset de talentos;
* serviços especiais.

Sem consumo constante a moeda perde valor.

---

# Sistema de Build Score

O poder de um item não é definido apenas por seu valor bruto.

O sistema utiliza um Build Score.

O Build Score considera:

* dano;
* vida;
* defesa;
* atributos;
* sinergias;
* efeitos especiais.

O objetivo é avaliar o impacto real do item na build atual.

---

# Build Tags

Todo item pode possuir tags.

Exemplos:

* Guerreiro
* Arqueiro
* Mago
* Curandeiro

Especializações:

* Crítico
* Sangramento
* Fogo
* Gelo
* Tanque
* Invocação

As tags permitem que o sistema identifique sinergias.

---

# Sistema de Auto-Equip

O Auto-Equip deve ser opcional.

Seu objetivo é reduzir microgerenciamento sem remover escolhas do jogador.

---

## Regras

Equipar automaticamente quando:

* ganho superior ao limite configurado;
* sinergia positiva com a build.

Nunca equipar automaticamente quando:

* reduzir sinergias importantes;
* quebrar conjuntos ativos;
* substituir itens favoritados;
* reduzir o Build Score.

---

## Avaliação

O sistema calcula:

Score Total =
Dano +
Vida +
Defesa +
Atributos +
Sinergias +
Bônus de Classe

Se o novo item superar o item atual dentro dos critérios configurados, ele pode ser equipado automaticamente.

---

# Critérios de Sucesso

O sistema de loot será considerado saudável quando:

* encontrar itens for empolgante;
* equipamentos tiverem impacto real;
* o jogador desejar continuar farmando;
* ouro possuir valor constante;
* Auto-Equip tomar decisões coerentes;
* diferentes builds valorizarem itens diferentes.

O loot existe para transformar combate em progressão.

Sem loot relevante, a progressão perde significado.
