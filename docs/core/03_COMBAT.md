# Combate

## Objetivo

Definir a filosofia, funcionamento e evolução do sistema de combate do TBH2.

O combate é o principal mecanismo de transformação de tempo em progresso.

É através dele que o jogador obtém:

* experiência;
* ouro;
* equipamentos;
* progresso de mapas;
* avanço de dificuldades.

Todo sistema de progressão do jogo depende diretamente do combate.

O combate existe para validar a evolução do personagem.

---

## Status

In Progress

---

## Dependências

* Gameplay Central
* Progressão
* Sistema de Itens
* Atributos
* Classes
* Habilidades
* Sistema de Monstros
* Balance Formulas

---

# Filosofia de Combate

O combate do TBH2 é inspirado em:

* Diablo
* Path of Exile
* Last Epoch
* D&D

Adaptado para um formato Idle Companion.

O jogador não controla diretamente o combate.

O foco está na construção do personagem.

A principal pergunta do sistema não é:

> "Eu consigo executar melhor?"

A principal pergunta é:

> "Meu personagem está preparado para este desafio?"

O combate deve ser consequência das escolhas realizadas anteriormente.

---

# Filosofia de Build

O TBH2 não utiliza modos de combate selecionáveis.

Não existem estilos como:

* agressivo;
* balanceado;
* defensivo.

O comportamento do personagem é determinado por:

* equipamentos;
* atributos;
* habilidades;
* classe;
* efeitos especiais;
* sinergias.

Dois personagens da mesma classe podem possuir comportamentos completamente diferentes dependendo da build construída.

O estilo de combate emerge das escolhas do jogador.

---

# Pilares do Combate

Todo combate deve validar uma ou mais camadas de progressão.

---

## Nível

Representa experiência acumulada.

Impacto:

* crescimento constante;
* atributos básicos;
* acesso a conteúdos futuros.

---

## Equipamentos

Principal fonte de poder.

Impacto:

* dano;
* sobrevivência;
* especialização;
* identidade da build.

Equipamentos devem possuir mais impacto do que múltiplos níveis consecutivos.

---

## Atributos

Definem a direção do personagem.

Atributos primários:

* STR
* DEX
* INT
* CON

Os atributos convertem equipamentos em poder efetivo.

---

## Classe

Define identidade.

A classe influencia:

* equipamentos desejados;
* atributos prioritários;
* habilidades disponíveis;
* estilo geral de combate.

---

## Habilidades

Representam a expressão final da build.

Transformam atributos e equipamentos em ações visíveis durante o combate.

---

# Fluxo de Combate

Todo encontro segue o mesmo fluxo.

Exploração
↓
Encontro
↓
Combate
↓
Recompensa
↓
Progressão
↓
Exploração

O combate não é um sistema isolado.

Ele faz parte do ciclo principal do jogo.

---

# Objetivos do Combate

Todo encontro deve responder pelo menos uma das seguintes perguntas:

* O personagem está forte o suficiente?
* Os equipamentos são adequados?
* Os atributos estão corretos?
* A build está funcionando?
* O jogador pode avançar para a próxima região?

---

# Combate Atual

A versão atual utiliza:

* ataque automático;
* defesa básica;
* cálculo simples de dano;
* recompensa automática.

O combate é resolvido sem intervenção direta do jogador.

O resultado depende exclusivamente da força construída pelo personagem.

---

# Evolução Planejada

O combate continuará sendo automático durante todo o ciclo de vida do projeto.

Não existe intenção de transformar o TBH2 em um Action RPG.

O foco permanece em:

* progressão;
* equipamentos;
* builds;
* otimização;
* longo prazo.

---

## Fase 2

Adicionar:

* habilidades automáticas;
* cooldowns;
* prioridades de execução;
* efeitos visuais de habilidades.

---

## Fase 3

Adicionar:

* sinergias entre atributos;
* efeitos especiais;
* modificadores de equipamentos;
* interações entre habilidades.

---

## Fase 4

Adicionar:

* categorias avançadas de dano;
* categorias avançadas de defesa;
* efeitos de controle;
* resistências especializadas.

---

# Categorias de Dano

## Físico

Fonte principal:

* armas;
* STR;
* habilidades físicas.

Mitigação:

* Armor.

---

## Mágico

Fonte principal:

* INT;
* habilidades mágicas;
* efeitos especiais.

Mitigação:

* Spell Armor.

---

## Puro

Ignora mitigações tradicionais.

Utilização prevista:

* chefes;
* habilidades lendárias;
* mecânicas especiais.

Deve permanecer raro.

---

# Categorias Defensivas

## Armor

Reduz dano físico recebido.

Principal defesa de guerreiros e armaduras pesadas.

---

## Spell Armor

Reduz dano mágico recebido.

Principal defesa contra conjuradores.

---

## Evasion

Chance de evitar completamente um ataque.

Mais comum em builds de DEX.

Possui limite máximo para evitar abusos.

---

## Parry

Chance de bloquear ou reduzir um ataque.

Mais comum em armas marciais e escudos.

---

## Resistência a Controle

Reduz duração de efeitos negativos.

Exemplos:

* stun;
* slow;
* silence;
* fear.

---

# Ordem de Resolução

Fluxo planejado:

Ataque
↓
Verificação de Acerto
↓
Evasion
↓
Parry
↓
Crítico
↓
Categoria de Dano
↓
Mitigação
↓
Aplicação Final

Esta ordem poderá ser ajustada durante os testes de balanceamento.

---

# Filosofia de Balanceamento

O combate deve ser simples de compreender.

Difícil de otimizar.

O jogador deve entender claramente:

* por que venceu;
* por que perdeu;
* o que precisa melhorar.

Toda derrota deve indicar uma solução possível.

Exemplos:

* subir de nível;
* melhorar equipamentos;
* revisar atributos;
* melhorar a build;
* revisar habilidades.

Derrotas nunca devem parecer aleatórias.

---

# Critérios de Sucesso

O sistema de combate será considerado saudável quando:

* equipamentos forem relevantes;
* níveis possuírem impacto;
* classes apresentarem identidade própria;
* habilidades criarem diferenças perceptíveis;
* chefes representarem desafios reais;
* builds distintas produzirem resultados distintos;
* derrotas possuírem explicação clara;
* vitórias gerarem sensação de progresso.

---

# Regras

* O combate permanece automático.
* O jogador não controla ações individuais.
* Não existirão modos de combate selecionáveis.
* O estilo de combate é definido pela build.
* Equipamentos possuem prioridade sobre níveis como fonte de poder.
* Habilidades amplificam a build, não substituem equipamentos.
* Toda nova mecânica deve reforçar a progressão do personagem.

---

# Pendências

* Definir fórmulas finais de dano.
* Definir fórmulas de Armor e Spell Armor.
* Definir limites de Evasion.
* Definir limites de Parry.
* Definir limites de Crítico.
* Definir sistema de controle.
* Integrar habilidades ao fluxo de combate.

---

# Histórico de Alterações

* 2026-06-10: removidos modos de combate.
* 2026-06-10: introduzida Filosofia de Build.
* 2026-06-10: reorganização completa do sistema de combate.
* 2026-06-10: alinhamento com Progressão e Sistema de Itens.
