# Raridades

## Objetivo

Definir as categorias de raridade dos itens, sua apresentação visual, potencial de atributos e papel dentro da progressão do TBH2.

Raridade não representa apenas poder.

Ela representa complexidade, potencial e possibilidades de construção de build.

---

## Status

Draft

---

## Dependências

* Sistema de Itens
* Loot e Economia
* Afixos
* Build Score

---

# Filosofia das Raridades

Um item mais raro não deve ser automaticamente melhor.

A raridade determina:

* quantidade de atributos;
* complexidade dos efeitos;
* potencial de sinergia;
* possibilidade de criar builds.

O jogador deve avaliar:

> "Este item combina com meu personagem?"

e não apenas:

> "Este item possui uma cor mais rara."

---

# Estrutura das Raridades

A progressão inicial utiliza sete níveis de raridade.

---

## Comum

Cor:

Branco

Função:

Base da economia.

Características:

* atributos básicos;
* sem afixos especiais;
* utilizado para progressão inicial.

Exemplo:

Espada Curta
+20 Dano

---

## Mágico

Cor:

Azul

Função:

Primeira especialização.

Características:

* 1 a 2 afixos;
* atributos simples;
* melhorias diretas.

Exemplo:

Espada Curta do Guerreiro
+25 Dano
+5 STR

---

## Raro

Cor:

Amarelo

Função:

Principal raridade do Mid Game.

Características:

* múltiplos afixos;
* combinações variadas;
* grande diversidade.

Exemplo:

Espada Longa
+50 Dano
+12 STR
+6% Crítico

---

## Épico

Cor:

Roxo

Função:

Itens de alto valor.

Características:

* atributos elevados;
* sinergias mais fortes;
* maior Build Score potencial.

Exemplo:

Claymore Sombria
+90 Dano
+20 STR
+10% Crítico
+8% Sangramento

---

## Lendário

Cor:

Laranja

Função:

Modificar gameplay.

Características:

* efeito exclusivo;
* interação com habilidades;
* identidade própria.

Exemplo:

Lâmina do Carniceiro

Efeito:

Ataques críticos possuem chance de causar Sangramento Massivo.

---

## Set

Cor:

Verde

Função:

Construção de conjuntos.

Características:

* bônus por quantidade equipada;
* foco em identidade de build.

Exemplo:

Conjunto do Guardião

2 peças:
+10% Vida

4 peças:
+15% Armadura

6 peças:
Efeito exclusivo.

---

## Mítico

Cor:

Vermelho

Função:

Itens extremamente raros.

Características:

* modificadores únicos;
* impacto significativo;
* objetivos de Endgame.

Os Míticos devem ser memoráveis.

---

# Potencial por Raridade

A raridade influencia a quantidade de atributos possíveis.

| Raridade | Atributos | Efeito Especial   |
| -------- | --------- | ----------------- |
| Comum    | 0-1       | Não               |
| Mágico   | 1-2       | Não               |
| Raro     | 3-4       | Não               |
| Épico    | 4-5       | Opcional          |
| Lendário | 4-5       | Sim               |
| Set      | Variável  | Bônus de Conjunto |
| Mítico   | Variável  | Exclusivo         |

Os valores finais serão definidos em BALANCE_FORMULAS.md.

---

# Chances de Obtenção

Valores iniciais de referência.

| Raridade | Chance            |
| -------- | ----------------- |
| Comum    | 60%               |
| Mágico   | 25%               |
| Raro     | 10%               |
| Épico    | 4%                |
| Lendário | 1%                |
| Set      | Especial          |
| Mítico   | Extremamente Raro |

As chances podem ser modificadas por:

* dificuldade;
* eventos;
* chefes;
* bônus de sorte;
* progressão mundial.

---

# Poder vs Raridade

Poder e Raridade são conceitos independentes.

Exemplo:

Espada Rara Nível 50

Poder: 500

Espada Lendária Nível 30

Poder: 420

A espada rara pode ser numericamente superior.

A lendária pode oferecer efeitos únicos.

O jogador deve decidir qual possui maior valor para sua build.

---

# Build Score

Build Score representa o valor real do item para o personagem atual.

A raridade aumenta o potencial de Build Score.

Ela não garante um Build Score maior.

Isso evita que itens antigos se tornem instantaneamente inúteis.

---

# Filosofia de Progressão

A distribuição de raridades muda conforme o avanço do jogador.

---

## Early Game

Predominância:

* Comum
* Mágico

Objetivo:

Ensinar o sistema de equipamentos.

---

## Mid Game

Predominância:

* Mágico
* Raro

Objetivo:

Criar escolhas reais.

---

## Late Game

Predominância:

* Raro
* Épico

Objetivo:

Especialização.

---

## Endgame

Objetivo:

Buscar:

* Lendários;
* Sets;
* Míticos.

O foco deixa de ser encontrar qualquer upgrade.

O objetivo passa a ser encontrar o upgrade ideal.

---

# Apresentação Visual

Toda raridade deve possuir:

* cor própria;
* efeito visual próprio;
* destaque no loot feed;
* destaque no inventário.

Itens mais raros devem gerar expectativa antes mesmo de serem analisados.

---

# Regras

* Raridade não substitui Poder.
* Raridade não substitui Build Score.
* Lendários devem alterar gameplay.
* Sets devem incentivar builds específicas.
* Míticos devem ser extremamente raros.
* Itens raros podem permanecer relevantes durante longos períodos.

---

# Pendências

* Definir afixos por raridade.
* Definir efeitos lendários iniciais.
* Definir conjuntos iniciais.
* Definir critérios de geração mítica.
* Definir efeitos visuais de raridade.
* Integrar ao sistema de Auto-Equip.

---

# Histórico de Alterações

* 2026-06-10: criado template modular.
* 2026-06-10: definidas sete categorias de raridade.
* 2026-06-10: introduzida separação entre Poder e Raridade.
* 2026-06-10: introduzido conceito de Build Score.
* 2026-06-10: registrada expansão futura para Sets e Míticos.
