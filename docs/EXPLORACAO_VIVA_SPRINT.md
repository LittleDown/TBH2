# Sprint UX/Visual 01 — Exploração Viva

## Objetivo

Fazer a Estrada Abandonada transmitir sensação de jornada contínua sem alterar sistemas de RPG.

Esta sprint tem foco exclusivamente visual e experiencial.

Não deve alterar:

* combate;
* XP;
* ouro;
* loot;
* equipamentos;
* mapas;
* save;
* fórmulas;
* progressão.

O objetivo é melhorar a percepção de movimento, presença e deslocamento durante a exploração.

---

## Status

Concluída — Sprint Visual

---

## Contexto

O TBH2 depende da sensação de que o aventureiro está sempre em jornada.

Como o jogo ocupa uma janela compacta de Taskbar, a exploração precisa ser legível mesmo em atenção periférica.

A Estrada Abandonada foi escolhida como primeiro mapa para validar o contrato visual de exploração viva.

---

# Escopo da Sprint

A sprint aplicou uma composição visual completa inicialmente apenas ao mapa:

```text
Estrada Abandonada
```

Os demais mapas mantêm seus ambientes anteriores até receberem sprints visuais próprias.

---

# Implementação Visual

## Herói

O herói permanece fixo próximo a 30% da largura da cena.

Durante a exploração:

* executa caminhada contínua;
* permanece visualmente ativo;
* transmite deslocamento sem mover sua posição principal.

Ao iniciar encontro:

* interrompe caminhada;
* assume pose idle;
* aguarda aproximação do inimigo.

---

## Inimigo

O inimigo entra pela direita durante o estado de encontro.

A entrada do inimigo reforça a transição entre:

```text
exploração
↓
encontro
↓
combate
```

O cenário desacelera enquanto o inimigo se aproxima.

---

## Movimento do Mundo

Durante exploração, o mundo se move.

Durante combate, o mundo para.

Essa regra reforça a leitura visual:

* mundo em movimento = jornada;
* mundo desacelerando = perigo próximo;
* mundo parado = combate;
* mundo retomando = jornada continua.

---

# Estados Visuais

## Explore

Estado de exploração contínua.

Características:

* herói caminhando;
* mundo em movimento;
* parallax ativo;
* elementos decorativos reciclados.

---

## Encounter

Estado de transição.

Características:

* inimigo entra pela direita;
* mundo desacelera;
* herói para de caminhar;
* tensão visual aumenta.

---

## Fight

Estado de combate.

Características:

* cenário parado;
* foco no herói e inimigo;
* ataques, impactos e dano flutuante visíveis.

---

## Reward

Estado de recompensa.

Características:

* cenário ainda parado;
* recompensa apresentada;
* vitória comunicada visualmente;
* preparação para retorno à exploração.

---

## Return to Explore

Estado de retomada.

Características:

* mundo acelera gradualmente;
* herói volta a caminhar;
* exploração contínua é restaurada.

---

# Desaceleração e Retomada

## Desaceleração

Ao iniciar encontro, a velocidade do mundo reduz de:

```text
100% → 0%
```

Duração:

```text
0,75 segundo
```

Objetivo:

Comunicar que algo interrompeu a jornada.

---

## Retomada

Após a recompensa, a velocidade do mundo aumenta de:

```text
0% → 100%
```

Objetivo:

Comunicar que o aventureiro voltou à estrada.

---

# Parallax

A Estrada Abandonada utiliza três camadas visuais.

## Fundo

Velocidade relativa:

```text
20%
```

Elementos:

* montanhas;
* castelo distante;
* céu;
* silhuetas longínquas.

Função:

Criar profundidade.

---

## Ambiente

Velocidade relativa:

```text
50%
```

Elementos:

* árvores;
* cercas;
* estruturas médias;
* elementos de estrada.

Função:

Representar o espaço principal da jornada.

---

## Primeiro Plano

Velocidade relativa:

```text
100%
```

Elementos:

* pedras;
* vegetação;
* placas;
* rastros;
* vestígios.

Função:

Reforçar movimento e velocidade.

---

# Decoração Procedural

Foram adicionados elementos decorativos determinísticos e reutilizados por wrapping.

Objetivo:

Criar variação visual sem gerar custo excessivo.

Elementos utilizados:

* árvores;
* cercas;
* pedras;
* vegetação;
* placas;
* rastros;
* fogueira;
* espada;
* carroça;
* bandeira.

---

# Suspense Ambiental

A Estrada Abandonada recebeu elementos para sugerir história sem texto explicativo.

Exemplos:

* rastros no caminho;
* fogueira apagada;
* espada cravada;
* carroça abandonada;
* bandeira rasgada;
* vestígios de passagem.

Esses elementos não alteram recompensas ou progressão.

Eles existem para reforçar atmosfera.

---

# Eventos Ambientais

Foram adicionados eventos ocasionais leves:

* corvos;
* folhas;
* poeira.

Função:

Dar vida ao ambiente sem competir com combate ou interface.

Eventos ambientais não exigem ação do jogador.

---

# Contrato Visual Validado

Esta sprint validou o seguinte contrato:

```text
Herói fixo
+
Mundo em movimento
+
Parallax em camadas
+
Desaceleração no encontro
+
Cenário parado no combate
+
Retomada após recompensa
```

Esse contrato pode ser reutilizado em outros mapas.

---

# Validação

Foram validados:

* desaceleração;
* parada do cenário;
* retomada da exploração;
* ciclo completo pelo `after()` do Tkinter;
* inspeção visual dos estados;
* ausência de alteração em fórmulas de RPG.

---

# Testes

Foram criados ou mantidos testes para garantir:

* desaceleração correta;
* parada durante combate;
* retomada após recompensa;
* estabilidade do ciclo visual;
* preservação do funcionamento do loop principal.

---

# Limitações

A sprint ainda possui limitações visuais:

* decoração desenhada com placeholders do Canvas;
* ausência de sprites próprios para árvores, pedras e placas;
* ausência de tiles finais;
* ausência de transição climática;
* ausência de iluminação dinâmica;
* ausência de áudio ambiente;
* demais mapas ainda não usam parallax de três camadas.

---

# Riscos Identificados

## Duplicação de Lógica

Aplicar parallax em outros mapas copiando código pode gerar manutenção difícil.

Solução recomendada:

Criar contrato único de camadas visuais reutilizáveis.

---

## Poluição Visual

Adicionar muitos elementos pode prejudicar a leitura da janela compacta.

Solução recomendada:

Manter prioridade em silhueta, contraste e clareza.

---

## Confusão com Gameplay

Elementos narrativos podem parecer interativos ou recompensáveis.

Solução recomendada:

Elementos ambientais devem ser claramente decorativos.

---

# Regras

* Sprint visual não altera sistemas de RPG.
* O herói permanece fixo durante exploração.
* O mundo transmite movimento.
* O cenário para durante combate.
* Parallax deve respeitar camadas.
* Elementos ambientais não alteram loot, XP ou ouro.
* Cada mapa deve receber kit visual próprio.
* Não duplicar regras de movimento em cada mapa.
* A legibilidade da janela compacta tem prioridade sobre detalhe visual.

---

# Próxima Sprint Visual Recomendada

## Sprint UX/Visual 02 — Kits de Bioma

Objetivo:

Criar kits visuais por bioma e aplicar o mesmo contrato de camadas aos mapas seguintes.

Escopo recomendado:

* definir estrutura de `VisualKit`;
* criar kit para Bosque dos Sussurros;
* criar kit para Acampamento Saqueado;
* reutilizar contrato de parallax;
* manter controlador de jornada único;
* não alterar combate, loot, XP, ouro, equipamentos ou save.

---

# Critérios de Sucesso

A sprint será considerada bem-sucedida quando:

* a Estrada Abandonada parecer uma jornada contínua;
* o jogador perceber movimento sem o herói sair da posição principal;
* encontro, combate e recompensa forem visualmente distinguíveis;
* a exploração retomar naturalmente após vitória;
* o sistema puder ser reaplicado a outros mapas sem duplicação;
* a identidade de Taskbar Companion for reforçada.

---

# Histórico de Alterações

* 2026-06-10: Sprint UX/Visual 01 registrada.
* 2026-06-10: Estrada Abandonada recebeu parallax em três camadas.
* 2026-06-10: desaceleração e retomada visual documentadas.
* 2026-06-10: contrato visual de exploração viva definido.
