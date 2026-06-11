# Armas

## Objetivo

Definir as famílias de armas, suas características, escalonamento e identidade dentro do sistema de combate do TBH2.

As armas representam a principal fonte ofensiva do personagem.

Seu papel não é apenas fornecer dano.

As armas ajudam a definir o estilo de jogo, a identidade da build e a forma como os atributos são convertidos em poder.

---

## Status

Draft

---

## Dependências

* Sistema de Itens
* Atributos
* Combate
* Classes
* Balance Formulas

---

# Filosofia das Armas

Armas não devem ser apenas números diferentes.

Cada família deve possuir vantagens e desvantagens claras.

O jogador deve escolher armas por:

* estilo de jogo;
* sinergia;
* build;
* atributos.

E não apenas pelo maior dano bruto.

---

# Estrutura de Armas

As armas são divididas em famílias.

Cada família possui:

* dano base;
* velocidade de ataque;
* escalonamento;
* identidade própria.

---

# Famílias de Armas

## Espadas

Identidade:

Equilíbrio.

Características:

* dano médio;
* velocidade média;
* boa compatibilidade com múltiplas builds.

Escalonamento:

* STR
* DEX

Classes:

* Guerreiro
* Arqueiro
* Paladino (futuro)

---

## Machados

Identidade:

Força bruta.

Características:

* dano elevado;
* ataques mais lentos;
* maior potencial crítico.

Escalonamento:

* STR

Classes:

* Guerreiro

---

## Martelos

Identidade:

Impacto.

Características:

* dano alto;
* velocidade baixa;
* foco em controle e atordoamento.

Escalonamento:

* STR
* CON

Classes:

* Guerreiro
* Curandeiro de batalha (futuro)

---

## Adagas

Identidade:

Precisão.

Características:

* dano menor;
* velocidade elevada;
* foco em crítico.

Escalonamento:

* DEX

Classes:

* Arqueiro
* Assassino (futuro)

---

## Arcos

Identidade:

Combate à distância.

Características:

* dano consistente;
* alta precisão;
* foco em crítico.

Escalonamento:

* DEX

Classes:

* Arqueiro

---

## Cajados

Identidade:

Canalização mágica.

Características:

* dano mágico;
* amplificação de habilidades;
* foco em INT.

Escalonamento:

* INT

Classes:

* Mago
* Curandeiro

---

## Varinhas

Identidade:

Velocidade mágica.

Características:

* dano menor;
* conjuração rápida;
* foco em habilidades frequentes.

Escalonamento:

* INT

Classes:

* Mago

---

# Armas de Uma Mão

Permitem utilização de Weapon 2.

Exemplos:

* espada curta;
* machado leve;
* adaga;
* varinha.

Vantagem:

Maior flexibilidade.

---

# Armas de Duas Mãos

Ocupam Weapon e Weapon 2 simultaneamente.

Exemplos:

* claymore;
* martelo de guerra;
* arco longo;
* cajado arcano.

Vantagem:

Maior poder ofensivo.

Desvantagem:

Perda do segundo espaço de equipamento.

---

# Progressão de Poder

Toda arma possui:

* nível do item;
* raridade;
* atributos;
* afixos;
* Build Score.

O dano base cresce principalmente através do nível do item.

A raridade amplia as possibilidades de atributos.

---

# Escalonamento por Atributo

## STR

Aumenta:

* dano físico;
* dano crítico físico.

---

## DEX

Aumenta:

* precisão;
* velocidade de ataque;
* chance crítica.

---

## INT

Aumenta:

* dano mágico;
* cura;
* efeitos de habilidades.

---

## CON

Aumenta:

* vida;
* resistência;
* efeitos defensivos.

Algumas armas podem utilizar escalonamento híbrido.

---

# Poder

O Poder da arma representa uma avaliação simplificada de sua qualidade.

Ele considera:

* dano;
* raridade;
* atributos;
* afixos.

O Poder não substitui o Build Score.

---

# Build Score

Build Score representa o valor real da arma para o personagem atual.

Exemplo:

Espada A

* Poder: 500

Espada B

* Poder: 520

Se a build utiliza crítico e a Espada A possui sinergias críticas superiores, ela pode possuir Build Score maior.

O Auto-Equip deve utilizar Build Score sempre que disponível.

---

# Regras

* Toda arma deve pertencer a uma família.
* Toda família deve possuir identidade própria.
* Não criar armas que diferem apenas por números.
* Armas de duas mãos ocupam dois espaços.
* Build Score possui prioridade sobre Poder.
* Novas famílias exigem justificativa de gameplay.

---

# Pendências

* Definir catálogo inicial de armas.
* Definir afixos específicos por família.
* Definir compatibilidade completa de classes.
* Definir animações específicas por família.
* Definir efeitos lendários exclusivos.

---

# Histórico de Alterações

* 2026-06-10: criado template modular.
* 2026-06-10: definidas famílias principais.
* 2026-06-10: introduzido escalonamento por atributos.
* 2026-06-10: introduzido conceito de armas de uma e duas mãos.
