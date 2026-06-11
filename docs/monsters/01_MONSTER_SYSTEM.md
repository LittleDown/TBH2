# Sistema de Monstros

## Objetivo

Definir o modelo compartilhado de inimigos, suas categorias, atributos, escalonamento e recompensas.

Os monstros são a principal fonte de combate do TBH2.

Eles existem para desafiar o personagem, validar a progressão e sustentar o ciclo de loot.

---

## Status

Draft

---

## Dependências

* Combate
* Progressão
* Sistema de Itens
* Loot e Economia
* Estrutura do Mundo
* Balance Formulas

---

# Filosofia dos Monstros

Os monstros não existem apenas para fornecer experiência.

Eles existem para criar variedade.

Cada encontro deve gerar pelo menos uma das seguintes sensações:

* velocidade;
* pressão;
* resistência;
* perigo;
* recompensa.

O jogador deve reconhecer diferentes tipos de inimigos visualmente.

---

# Estrutura Geral

Todo inimigo pertence a uma categoria.

Categorias determinam:

* dificuldade;
* recompensas;
* frequência;
* comportamento.

---

# Categorias de Monstros

## Comum

Categoria mais frequente.

Função:

Sustentar a progressão básica.

Características:

* atributos equilibrados;
* baixa complexidade;
* recompensas básicas.

Exemplos:

* ratos;
* lobos;
* esqueletos;
* saqueadores.

---

## Campeão

Versão fortalecida de um monstro comum.

Características:

* mais vida;
* mais dano;
* modificadores especiais.

Função:

Aumentar a variedade dos encontros.

---

## Elite

Monstros perigosos.

Características:

* atributos elevados;
* habilidades especiais;
* maior recompensa.

Função:

Testar a build do jogador.

---

## Chefe

Principal desafio de um mapa ou região.

Características:

* grande quantidade de vida;
* múltiplas habilidades;
* recompensas importantes.

Função:

Validar progresso.

---

# Arquétipos de Combate

Além da categoria, cada monstro possui um arquétipo.

---

## Brutamonte

Características:

* muita vida;
* alto dano;
* baixa velocidade.

Objetivo:

Pressão.

---

## Assassino

Características:

* pouca vida;
* alto dano;
* alta velocidade.

Objetivo:

Explosão.

---

## Tanque

Características:

* defesa elevada;
* dano reduzido.

Objetivo:

Resistência.

---

## Conjurador

Características:

* dano mágico;
* habilidades especiais.

Objetivo:

Variar ameaças.

---

## Invocador

Características:

* gera criaturas auxiliares.

Objetivo:

Aumentar a pressão do combate.

---

# Escalonamento

Todo monstro escala através de:

* nível da área;
* mapa;
* ato;
* dificuldade.

O sistema evita a criação manual de centenas de versões do mesmo inimigo.

---

# Nível do Monstro

O nível do monstro é definido pelo mapa.

Exemplo:

Mapa 1

Nível 1

---

Mapa 10

Nível 10

---

Mapa 30

Nível 30

---

O monstro utiliza esse nível para calcular:

* vida;
* dano;
* defesa;
* experiência concedida.

---

# Escalonamento por Dificuldade

Cada dificuldade aumenta:

* vida;
* dano;
* recompensa.

Exemplo:

Normal
100%

Veterano
150%

Pesadelo
250%

Infernal
400%

Valores finais serão definidos em Balance Formulas.

---

# Atributos

Todo monstro possui:

* Vida
* Ataque
* Armor
* Spell Armor

Monstros avançados podem possuir:

* Crítico
* Evasion
* Parry
* Resistências

---

# Comportamento

O combate continua sendo automático.

O comportamento dos monstros é representado através de atributos e habilidades.

Não existe IA complexa.

A identidade dos monstros surge através de:

* arquétipos;
* habilidades;
* estatísticas.

---

# Habilidades de Monstros

Sistema planejado para fases futuras.

Exemplos:

* ataque em área;
* veneno;
* sangramento;
* regeneração;
* invocação;
* atordoamento.

Essas habilidades devem reforçar o arquétipo do inimigo.

---

# Recompensas

Todo monstro concede:

* experiência;
* ouro;
* chance de loot.

A quantidade depende de:

* categoria;
* nível;
* dificuldade.

---

# Filosofia de Loot

Monstros mais perigosos devem oferecer melhores recompensas.

Exemplo:

Comum

1x recompensa

---

Campeão

2x recompensa

---

Elite

4x recompensa

---

Chefe

10x recompensa

Valores finais serão definidos durante o balanceamento.

---

# Distribuição por Mapa

Todo mapa deve possuir uma combinação de:

* inimigos comuns;
* campeões;
* elites.

Chefes aparecem apenas em encontros específicos.

O objetivo é criar variedade sem excesso de complexidade.

---

# Relação com o Mundo

Cada região possui monstros próprios.

Exemplo:

Ato I

* lobos;
* esqueletos;
* saqueadores.

---

Ato II

* escorpiões;
* serpentes;
* guardiões imperiais.

---

Ato III

* criaturas corrompidas;
* plantas agressivas;
* predadores da selva.

Os monstros ajudam a construir a identidade visual e narrativa de cada ato.

---

# Filosofia de Balanceamento

O jogador deve conseguir identificar rapidamente:

* quais monstros são perigosos;
* quais monstros são resistentes;
* quais monstros possuem recompensas maiores.

A dificuldade deve vir de diferenças claras.

Não apenas de números maiores.

---

# Regras

* Todo monstro pertence a uma categoria.
* Todo monstro possui um arquétipo.
* Cada ato deve possuir identidade própria.
* Elites devem ser reconhecíveis visualmente.
* Chefes representam marcos de progressão.
* Monstros não devem depender de IA complexa.
* O sistema deve favorecer clareza e escalabilidade.

---

# Dados Planejados

Monster ID
Nome
Categoria
Arquétipo
Nível
Vida
Ataque
Armor
Spell Armor
Habilidades
Tabela de Loot
Experiência
Ouro

---

# Pendências

* Definir fórmulas de escalonamento.
* Definir habilidades iniciais.
* Definir elites por ato.
* Definir recompensas por categoria.
* Definir sistema de modificadores especiais.
* Definir integração com dungeons.

---

# Histórico de Alterações

* 2026-06-10: categorias de monstros definidas.
* 2026-06-10: arquétipos de combate introduzidos.
* 2026-06-10: sistema de escalonamento registrado.
* 2026-06-10: alinhamento completo com combate e progressão.
