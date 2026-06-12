# Sistema de Atributos e Progressão

## Objetivo

Definir a base de atributos primários do herói e como eles se convertem em estatísticas de combate ao longo da progressão do nível 1 ao 100.

Este documento descreve a proposta inicial de escalonamento para:

* dano físico;
* dano mágico;
* velocidade de ataque;
* armadura;
* bloqueio/aparo;
* evasão.

As fórmulas abaixo servem como base de balanceamento e podem ser ajustadas após testes de combate.

---

## Status

Planned - Fase 2

---

## Atributos Primários

O herói possui quatro atributos principais:

| Atributo     | Código | Função Principal                                        |
| ------------ | -----: | ------------------------------------------------------- |
| Força        |    STR | Dano físico, armas pesadas e poder bruto                |
| Agilidade    |    DEX | Velocidade de ataque, crítico, evasão e precisão        |
| Constituição |    CON | Vida, armadura, resistência e sobrevivência             |
| Inteligência |    INT | Dano mágico, cura, efeitos mágicos e redução de recarga |

---

## Filosofia de Progressão

O personagem evolui através de três fontes principais:

Nível + Classe + Equipamentos = Atributos Efetivos

Os atributos primários devem ser persistidos no save.

As estatísticas derivadas, como dano, armadura, velocidade de ataque e evasão, devem ser recalculadas sempre que houver alteração de:

* nível;
* classe;
* equipamento;
* bônus temporário;
* passiva;
* buff;
* debuff.

---

## Ordem de Composição

A ordem planejada para cálculo dos atributos é:

atributo_efetivo = floor((base_classe + ganho_por_nivel + bonus_flat_item) * (1 + bonus_percentual))

Onde:

| Campo              | Descrição                                                  |
| ------------------ | ---------------------------------------------------------- |
| `base_classe`      | Valor inicial do atributo conforme a classe                |
| `ganho_por_nivel`  | Crescimento automático do atributo entre os níveis 1 e 100 |
| `bonus_flat_item`  | Bônus fixo vindo de equipamentos                           |
| `bonus_percentual` | Bônus percentual vindo de itens, passivas ou buffs         |

---

# Progressão por Nível

## Regra Geral

O herói evolui do nível 1 ao 100.

A cada nível, a classe determina o crescimento principal dos atributos.

Exemplo de crescimento por classe:

| Classe    | STR | DEX | CON | INT |
| --------- | --: | --: | --: | --: |
| Guerreiro |  +3 |  +1 |  +2 |  +0 |
| Arqueiro  |  +1 |  +3 |  +2 |  +0 |
| Mago      |  +0 |  +1 |  +1 |  +3 |

Fórmula:

atributo_por_nivel = (nivel - 1) * crescimento_classe

Exemplo:

STR_guerreiro_lvl_50 = STR_base + ((50 - 1) * 3)

---

# Escalonamento por Equipamentos

Equipamentos devem ser a principal fonte de crescimento avançado no mid game e end game.

A progressão natural por nível mantém o personagem funcional.

Os itens permitem especialização, otimização e criação de builds.

## Fórmula Base de Atributo em Item

atributo_item = floor(item_level * multiplicador_raridade * peso_do_slot)

## Multiplicador por Raridade

| Raridade | Multiplicador |
| -------- | ------------: |
| Comum    |          0.80 |
| Mágico   |          1.00 |
| Raro     |          1.25 |
| Épico    |          1.60 |
| Lendário |          2.10 |
| Mítico   |          2.80 |

## Peso por Slot

| Slot           | Peso |
| -------------- | ---: |
| Arma principal | 2.00 |
| Peitoral       | 1.50 |
| Elmo           | 1.00 |
| Luvas          | 0.80 |
| Botas          | 0.80 |
| Anel           | 0.60 |
| Amuleto        | 0.90 |

Exemplo:

item_level = 40
raridade = Épico
slot = Peitoral

atributo_item = floor(40 * 1.60 * 1.50)
atributo_item = 96

Neste exemplo, o item poderia gerar até 96 pontos distribuídos entre atributos principais, conforme sua regra de geração.

---

# Estatísticas Derivadas

## 1. Dano Físico

O dano físico representa ataques com armas, golpes corpo a corpo, flechas e habilidades físicas.

### Atributos que influenciam

| Atributo    | Influência                                           |
| ----------- | ---------------------------------------------------- |
| STR         | Principal fonte de dano físico                       |
| DEX         | Fonte secundária para armas leves e ataques precisos |
| Equipamento | Fonte principal de dano bruto                        |

### Poder Físico

poder_fisico = (STR * 2.00) + (DEX * 0.50) + bonus_poder_fisico_item

### Dano Físico Base

dano_fisico = floor((dano_arma + poder_fisico) * multiplicador_habilidade)

Exemplo:

STR = 80
DEX = 40
dano_arma = 50
multiplicador_habilidade = 1.00

poder_fisico = (80 * 2.00) + (40 * 0.50)
poder_fisico = 180

dano_fisico = floor((50 + 180) * 1.00)
dano_fisico = 230

---

## 2. Dano Mágico

O dano mágico representa feitiços, efeitos elementais, curas ofensivas e habilidades baseadas em energia mágica.

### Atributos que influenciam

| Atributo    | Influência                                                                  |
| ----------- | --------------------------------------------------------------------------- |
| INT         | Principal fonte de dano mágico                                              |
| Equipamento | Fonte de poder mágico, cajados, grimórios e focos                           |
| DEX         | Pode influenciar conjuração futura, mas não aumenta dano mágico diretamente |

### Poder Mágico

poder_magico = (INT * 2.20) + bonus_poder_magico_item

### Dano Mágico Base

dano_magico = floor((dano_magico_arma + poder_magico) * multiplicador_habilidade)

Exemplo:

INT = 90
dano_magico_arma = 45
multiplicador_habilidade = 1.20

poder_magico = 90 * 2.20
poder_magico = 198

dano_magico = floor((45 + 198) * 1.20)
dano_magico = 291

---

## 3. Velocidade de Ataque

A velocidade de ataque define quantas ações ofensivas o personagem consegue executar por segundo.

### Atributo Principal

| Atributo | Influência                                                       |
| -------- | ---------------------------------------------------------------- |
| DEX      | Aumenta velocidade de ataque com ganho reduzido em valores altos |

### Fórmula

bonus_attack_speed = min(0.75, DEX / (DEX + 500))

ataques_por_segundo = ataque_base_arma * (1 + bonus_attack_speed)

### Limite

bonus_attack_speed_maximo = 75%

Exemplo:

DEX = 100
ataque_base_arma = 1.20

bonus_attack_speed = 100 / (100 + 500)
bonus_attack_speed = 0.1666

ataques_por_segundo = 1.20 * (1 + 0.1666)
ataques_por_segundo = 1.39

---

## 4. Armadura

A armadura reduz dano físico recebido.

Por padrão, armadura não reduz dano mágico. Resistência mágica pode ser criada futuramente como estatística separada.

### Atributos que influenciam

| Atributo    | Influência                                |
| ----------- | ----------------------------------------- |
| CON         | Principal fonte defensiva                 |
| STR         | Fonte secundária para personagens físicos |
| Equipamento | Fonte principal no mid game e end game    |

### Fórmula

armor = floor((CON * 1.50) + (STR * 0.50) + armor_item)

### Redução de Dano Físico

reducao_dano_fisico = armor / (armor + (nivel_inimigo * 50))

### Limite

reducao_dano_fisico_maxima = 75%

Exemplo:

CON = 80
STR = 60
armor_item = 120
nivel_inimigo = 50

armor = floor((80 * 1.50) + (60 * 0.50) + 120)
armor = 270

reducao_dano_fisico = 270 / (270 + (50 * 50))
reducao_dano_fisico = 9.74%

---

## 5. Parry / Aparo

Parry representa a chance de aparar um ataque físico recebido.

Quando ativado, reduz parcialmente o dano recebido.

### Atributos que influenciam

| Atributo    | Influência                         |
| ----------- | ---------------------------------- |
| STR         | Capacidade de segurar impacto      |
| DEX         | Reflexo para aparar no tempo certo |
| Equipamento | Pode adicionar rating de parry     |

### Fórmula de Rating

parry_rating = (STR * 0.35) + (DEX * 0.65) + parry_item

### Chance de Parry

chance_parry = min(0.40, parry_rating / (parry_rating + 350))

### Efeito

dano_recebido_com_parry = dano_recebido * 0.50

### Limite

chance_parry_maxima = 40%

Exemplo:

STR = 70
DEX = 90
parry_item = 30

parry_rating = (70 * 0.35) + (90 * 0.65) + 30
parry_rating = 113

chance_parry = 113 / (113 + 350)
chance_parry = 24.4%

---

## 6. Evasão

Evasão representa a chance de evitar completamente um ataque recebido.

Deve ser forte em personagens ágeis, mas limitada para evitar invulnerabilidade.

### Atributo Principal

| Atributo    | Influência                      |
| ----------- | ------------------------------- |
| DEX         | Principal fonte de evasão       |
| Equipamento | Pode adicionar rating de evasão |

### Fórmula de Rating

evasao_rating = DEX + evasao_item

### Chance de Evasão

chance_evasao = min(0.45, evasao_rating / (evasao_rating + 400))

### Efeito

se evasao_ativada:
    dano_recebido = 0

### Limite

chance_evasao_maxima = 45%

Exemplo:

DEX = 120
evasao_item = 40

evasao_rating = 120 + 40
evasao_rating = 160

chance_evasao = 160 / (160 + 400)
chance_evasao = 28.5%

---

# Separação entre Dano Físico e Dano Mágico

## Dano Físico

Usado por:

* ataques básicos;
* armas corpo a corpo;
* arcos;
* lanças;
* machados;
* espadas;
* habilidades marciais.

Escala principalmente com:

STR + DEX + dano_arma + poder_fisico_item

É reduzido por:

armor

Pode ser evitado por:

evasao

Pode ser reduzido por:

parry

---

## Dano Mágico

Usado por:

* magias;
* habilidades elementais;
* explosões arcanas;
* efeitos sobrenaturais;
* habilidades de cura ofensiva.

Escala principalmente com:

INT + dano_magico_arma + poder_magico_item

Por padrão, não é reduzido por armor.

Futuramente pode ser reduzido por:

resistencia_magica

---

# Exemplo Prático

## Guerreiro Nível 20

### Base da Classe

STR = 12
DEX = 8
CON = 11
INT = 5

### Crescimento por Nível

Guerreiro:
STR +3
DEX +1
CON +2
INT +0

### Cálculo no Nível 20

STR = 12 + ((20 - 1) * 3) = 69
DEX = 8 + ((20 - 1) * 1) = 27
CON = 11 + ((20 - 1) * 2) = 49
INT = 5 + ((20 - 1) * 0) = 5

### Equipamentos

bonus_STR_item = 20
bonus_CON_item = 10
armor_item = 45
dano_arma = 35

### Atributos Efetivos

STR = 89
DEX = 27
CON = 59
INT = 5

### Dano Físico

poder_fisico = (89 * 2.00) + (27 * 0.50)
poder_fisico = 191.5

dano_fisico = floor(35 + 191.5)
dano_fisico = 226

### Attack Speed

bonus_attack_speed = 27 / (27 + 500)
bonus_attack_speed = 5.1%

### Armor

armor = floor((59 * 1.50) + (89 * 0.50) + 45)
armor = 178


### Parry


parry_rating = (89 * 0.35) + (27 * 0.65)
parry_rating = 48.7

chance_parry = 48.7 / (48.7 + 350)
chance_parry = 12.2%


### Evasão

evasao_rating = 27

chance_evasao = 27 / (27 + 400)
chance_evasao = 6.3%

---

# Regras de Balanceamento

* Atributos primários devem ser simples de entender.
* Estatísticas derivadas devem usar fórmulas centralizadas.
* Equipamentos devem escalar mais no end game do que o crescimento natural por nível.
* Dano físico e dano mágico devem ter fórmulas separadas.
* Armor deve reduzir apenas dano físico.
* Evasão deve evitar dano completamente, mas ter limite rígido.
* Parry deve reduzir dano parcialmente, mas não anular o ataque.
* Attack speed deve ter ganho reduzido em valores altos.
* Nenhuma chance defensiva deve permitir invulnerabilidade permanente.

---

# Pendências

* Definir valores base oficiais por classe.
* Definir crescimento final por classe.
* Criar resistência mágica como estatística futura.
* Definir se crítico será derivado de DEX, item ou ambos.
* Definir se cura escalará apenas com INT ou também com CON.
* Criar testes de balanceamento para níveis 1, 25, 50, 75 e 100.
* Validar impacto dos equipamentos lendários e míticos no nível 100.