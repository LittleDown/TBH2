# Combate

## Objetivo

Definir a filosofia, funcionamento, limites e evolução do sistema de combate do TBH2.

O combate é o mecanismo que transforma tempo em progresso.

É por meio dele que o jogador obtém:

* experiência;
* ouro;
* equipamentos;
* progresso de mapa;
* avanço de campanha;
* preparação para chefes e dificuldades superiores.

O combate existe para validar a evolução do personagem.

A pergunta central do sistema é:

> "Meu herói está preparado para este desafio?"

---

## Status

In Progress

---

## Dependências

* [Gameplay central](01_CORE_GAMEPLAY.md)
* [Progressão](02_PROGRESSION.md)
* [Loot e economia](04_LOOT_ECONOMY.md)
* [Sistema de itens](../items/01_ITEM_SYSTEM.md)
* [Sistema de herói](../heroes/01_HERO_SYSTEM.md)
* [Atributos](../heroes/03_ATTRIBUTES.md)
* [Classes](../heroes/02_CLASSES.md)
* [Habilidades](../heroes/04_SKILLS.md)
* [Sistema de monstros](../monsters/01_MONSTER_SYSTEM.md)
* [Chefes](../monsters/04_BOSSES.md)
* [Fórmulas de balanceamento](../technical/03_BALANCE_FORMULAS.md)

---

# Escopo deste Documento

Este documento define:

* filosofia do combate;
* papel do jogador;
* fluxo de combate;
* tipos de resultado;
* categorias conceituais de dano;
* categorias conceituais de defesa;
* ordem planejada de resolução;
* relação do combate com build;
* critérios de sucesso;
* limites do sistema.

---

# Fora do Escopo

Este documento não deve definir:

* valores finais de dano;
* fórmulas finais de HP;
* multiplicadores de armor;
* valores de crítico;
* cooldowns finais de habilidades;
* lista completa de habilidades;
* lista de monstros;
* estatísticas finais de inimigos;
* tabelas de loot;
* recompensas finais.

Esses assuntos pertencem aos documentos proprietários de cada domínio.

---

# Visão Geral

O combate do TBH2 é automático.

O jogador não executa ataques manualmente.

O jogador não controla movimentação, defesa, esquiva ou uso direto de habilidades durante o combate.

O papel do jogador é preparar o herói antes do encontro.

A preparação acontece por meio de:

* equipamentos;
* atributos;
* classe;
* habilidades futuras;
* raridades;
* efeitos especiais;
* sinergias;
* Power;
* Build Score.

O combate testa essa preparação.

---

# Filosofia de Combate

O TBH2 é inspirado em ARPGs como Diablo, Path of Exile e Last Epoch, mas adaptado para um formato Idle Companion.

A execução não deve ser o foco.

A construção do personagem deve ser o foco.

O combate deve ser:

* automático;
* claro;
* legível;
* recompensador;
* simples de entender;
* difícil de otimizar.

O jogador deve entender por que venceu ou perdeu.

Derrotas não devem parecer aleatórias.

---

# Build Acima de Modo Manual

O TBH2 não utiliza modos de combate selecionáveis.

Não existem estilos como:

* agressivo;
* balanceado;
* defensivo.

Esses modos pertencem ao legado técnico e não representam a direção futura do projeto.

O estilo de combate emerge da build.

Exemplos:

* uma build com arma pesada, STR e armadura alta tende a parecer agressiva e resistente;
* uma build com DEX, evasão e velocidade tende a parecer rápida;
* uma build com INT e habilidades mágicas tende a parecer explosiva;
* uma build com CON, cura e defesa tende a parecer sustentável.

Regra central:

> O jogador não escolhe um modo agressivo.
> O jogador constrói uma build agressiva.

---

# Papel do Jogador

O jogador atua como preparador de build.

Decisões relevantes:

* escolher equipamentos;
* comparar itens;
* distribuir atributos;
* escolher classe;
* configurar habilidades futuras;
* preparar o herói para chefes;
* decidir quando avançar ou farmar.

O jogador não deve precisar executar ações repetitivas durante o combate.

A preparação é mais importante que a execução.

---

# Fluxo de Combate

Todo encontro segue o fluxo principal do jogo:

```text
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
```

O combate não é um sistema isolado.

Ele faz parte do ciclo central do TBH2.

---

# Estados do Combate

## Antes do Combate

O jogo seleciona um encontro com base em:

* ato atual;
* mapa atual;
* dificuldade atual;
* pool de monstros da região;
* tipo de encontro;
* progresso de campanha.

O inimigo não deve ser gerado apenas pelo nível do herói.

---

## Início do Combate

Ao iniciar combate:

* a exploração é interrompida;
* o inimigo entra em cena;
* o herói assume postura de combate;
* o estado visual muda para combate;
* o sistema inicia o ciclo automático de ações.

---

## Durante o Combate

Durante o combate:

* herói e inimigo executam ações automaticamente;
* dano é calculado;
* vida é atualizada;
* eventos visuais são emitidos;
* habilidades futuras podem ser ativadas automaticamente;
* o combate continua até vitória ou derrota.

---

## Vitória

A vitória acontece quando o inimigo é derrotado.

Consequências possíveis:

* XP concedida;
* ouro concedido;
* loot gerado;
* progresso de mapa atualizado;
* evento visual de vitória;
* possível avanço de mapa;
* possível derrota de chefe;
* possível desbloqueio de ato ou dificuldade.

A entrega das recompensas pertence ao sistema de recompensas, não ao cálculo de dano.

---

## Derrota

A derrota acontece quando o herói perde toda a vida.

Consequências esperadas:

* combate encerrado;
* avanço bloqueado;
* herói retorna a estado seguro;
* vida é restaurada conforme regra de balanceamento;
* chefe ou mapa permanece como obstáculo;
* jogador deve fortalecer a build.

A derrota não deve apagar progresso principal.

Ela deve comunicar:

> "Ainda não estamos prontos."

---

# Fontes de Poder Validadas pelo Combate

O combate deve validar diferentes camadas de progressão.

---

## Nível

Representa experiência acumulada.

Função:

* crescimento base;
* referência de maturidade;
* acesso futuro a conteúdos.

Nível não deve ser a principal fonte de poder.

---

## Equipamentos

Principal fonte de poder.

Função:

* dano;
* sobrevivência;
* especialização;
* sinergia;
* identidade de build.

Equipamentos devem ter impacto perceptível no resultado do combate.

---

## Atributos

Fonte de especialização.

Atributos primários:

* STR;
* DEX;
* INT;
* CON.

Função:

* transformar itens em poder efetivo;
* reforçar identidade da classe;
* direcionar builds.

---

## Classe

Fonte de identidade.

Função:

* orientar atributos desejados;
* orientar equipamentos desejados;
* definir habilidades disponíveis;
* criar estilo geral de combate.

---

## Habilidades

Fonte de expressão da build.

Função:

* transformar atributos e equipamentos em ações visíveis;
* criar diferenças entre classes;
* reforçar sinergias;
* adicionar decisões automáticas configuráveis.

Habilidades não devem substituir equipamentos como principal fonte de poder.

---

# Combate Atual

A versão atual utiliza:

* ataque automático;
* defesa básica;
* cálculo simples de dano;
* recompensa automática;
* vitória e derrota;
* retorno à exploração.

Este estado é suficiente para validar o loop técnico.

Ainda não representa o sistema final de combate.

---

# Evolução Planejada

O combate continuará automático durante todo o ciclo de vida do projeto.

Não existe intenção de transformar o TBH2 em Action RPG.

---

## Etapa 1 — Consolidação

Objetivo:

Validar o combate atual.

Escopo:

* remover estratégias legadas;
* estabilizar vitória e derrota;
* validar tempo médio de combate;
* validar impacto de equipamentos;
* validar chefe do Ato I;
* separar combate de recompensa, loot e progressão.

---

## Etapa 2 — Habilidades Automáticas

Objetivo:

Adicionar expressão de classe sem exigir microgerenciamento.

Escopo:

* habilidades automáticas;
* cooldowns;
* prioridade de execução;
* ativação e desativação individual;
* efeitos visuais simples.

Detalhes pertencem ao documento:

* [Habilidades](../heroes/04_SKILLS.md)

---

## Etapa 3 — Sinergias de Build

Objetivo:

Fazer atributos, equipamentos e habilidades trabalharem juntos.

Escopo:

* sinergias entre atributos;
* modificadores de equipamentos;
* efeitos especiais;
* interações entre habilidades;
* Build Score mais relevante.

---

## Etapa 4 — Combate Avançado

Objetivo:

Adicionar categorias avançadas de dano e defesa.

Escopo:

* dano físico;
* dano mágico;
* dano puro;
* Armor;
* Spell Armor;
* Evasion;
* Parry;
* crítico;
* velocidade de ataque;
* regeneração;
* cura;
* resistência a controle.

Fórmulas pertencem ao documento:

* [Fórmulas de balanceamento](../technical/03_BALANCE_FORMULAS.md)

---

# Categorias de Dano

As categorias abaixo são conceituais.

Os valores e fórmulas pertencem ao documento de balanceamento.

---

## Dano Físico

Fontes principais:

* armas físicas;
* STR;
* habilidades físicas;
* monstros físicos.

Mitigação:

* Armor.

---

## Dano Mágico

Fontes principais:

* INT;
* habilidades mágicas;
* efeitos especiais;
* conjuradores.

Mitigação:

* Spell Armor.

---

## Dano Puro

Dano que ignora mitigações tradicionais.

Uso previsto:

* chefes;
* habilidades lendárias;
* mecânicas especiais.

Regra:

Dano puro deve ser raro.

---

# Categorias Defensivas

As categorias abaixo são conceituais.

Os valores e fórmulas pertencem ao documento de balanceamento.

---

## Armor

Reduz dano físico recebido.

Mais relevante para:

* guerreiros;
* armaduras pesadas;
* builds de sobrevivência física.

---

## Spell Armor

Reduz dano mágico recebido.

Mais relevante contra:

* conjuradores;
* chefes mágicos;
* efeitos arcanos.

---

## Evasion

Chance de evitar completamente um ataque.

Mais comum em:

* builds de DEX;
* armaduras leves;
* personagens ágeis.

Deve possuir limite máximo.

---

## Parry

Chance de bloquear ou reduzir um ataque.

Mais comum em:

* armas marciais;
* escudos;
* classes físicas.

Deve ser diferente de Evasion.

---

## Resistência a Controle

Reduz impacto de efeitos negativos.

Exemplos:

* stun;
* slow;
* silence;
* fear.

Sistema futuro.

---

# Ordem de Resolução

Ordem planejada:

```text
Ação iniciada
↓
Verificação de acerto
↓
Evasion
↓
Parry
↓
Crítico
↓
Categoria de dano
↓
Mitigação
↓
Aplicação final
↓
Eventos de combate
```

Esta ordem poderá ser ajustada durante testes.

Mudanças nessa ordem devem ser registradas neste documento e refletidas no documento de balanceamento.

---

# Eventos de Combate

O combate deve emitir eventos claros para a aplicação e a interface.

Eventos possíveis:

* EncounterStarted;
* CombatStarted;
* HeroAttacked;
* MonsterAttacked;
* DamageApplied;
* CriticalHit;
* AttackEvaded;
* AttackParried;
* SkillUsed;
* MonsterDefeated;
* HeroDefeated;
* BossDefeated;
* CombatEnded.

A interface deve transformar eventos em feedback visual.

O domínio não deve depender de texto pronto de UI.

---

# Relação com Recompensas

O combate determina vitória ou derrota.

O sistema de recompensas transforma vitória em:

* XP;
* ouro;
* loot;
* progresso.

O combate não deve concentrar sozinho:

* geração de loot;
* avanço de mapa;
* desbloqueio de ato;
* save.

Essas responsabilidades pertencem a sistemas próprios.

---

# Relação com Monstros

Monstros definem o desafio imediato.

O combate deve considerar:

* categoria do monstro;
* arquétipo;
* nível do mapa;
* dificuldade;
* modificadores;
* chefe ou elite.

Detalhes pertencem ao documento:

* [Sistema de monstros](../monsters/01_MONSTER_SYSTEM.md)

---

# Relação com Chefes

Chefes são testes maiores de combate.

Eles devem validar:

* dano;
* sobrevivência;
* consistência da build;
* qualidade dos equipamentos;
* preparação do jogador.

Chefes bloqueiam avanço.

Detalhes pertencem ao documento:

* [Chefes](../monsters/04_BOSSES.md)

---

# Relação com Balanceamento

Este documento define intenção, fluxo e ordem conceitual.

O documento de balanceamento define fórmulas.

Não definir aqui:

* dano final;
* curvas de HP;
* multiplicadores de dificuldade;
* chances finais de crítico;
* limites exatos de Evasion;
* limites exatos de Parry;
* mitigação final de Armor.

---

# Filosofia de Balanceamento do Combate

O combate deve ser simples de compreender e difícil de otimizar.

O jogador deve entender:

* por que venceu;
* por que perdeu;
* o que precisa melhorar.

Toda derrota deve indicar uma solução possível.

Exemplos:

* subir de nível;
* melhorar arma;
* melhorar armadura;
* trocar acessórios;
* revisar atributos;
* melhorar habilidades;
* farmar mapas anteriores;
* reduzir dificuldade futura, quando aplicável.

Derrotas não devem parecer aleatórias.

---

# Critérios de Sucesso

O sistema de combate será considerado saudável quando:

* equipamentos forem relevantes;
* níveis possuírem impacto;
* atributos alterarem decisões;
* classes apresentarem identidade;
* habilidades criarem diferenças perceptíveis;
* chefes representarem desafios reais;
* builds distintas produzirem resultados distintos;
* derrotas tiverem explicação clara;
* vitórias gerarem sensação de progresso;
* a tela permanecer legível em janela compacta.

---

# Regras

* O combate permanece automático.
* O jogador não controla ações individuais.
* Não existem modos de combate selecionáveis.
* O estilo de combate é definido pela build.
* Equipamentos possuem prioridade sobre níveis como fonte de poder.
* Habilidades amplificam a build, não substituem equipamentos.
* Derrotas devem indicar necessidade de melhoria.
* O combate não deve concentrar sozinho loot, progressão e save.
* Toda nova mecânica deve reforçar a progressão do personagem.
* A legibilidade em Taskbar tem prioridade sobre excesso de efeitos.

---

# Dados

Reservado para contratos conceituais do combate.

Fórmulas e constantes pertencem ao documento de balanceamento.

---

# Pendências

* Validar tempo médio de combate comum.
* Validar tempo médio de combate elite.
* Validar tempo médio de chefe.
* Definir fórmulas finais de dano no documento de balanceamento.
* Definir limites de Evasion no documento de balanceamento.
* Definir limites de Parry no documento de balanceamento.
* Definir limites de crítico no documento de balanceamento.
* Integrar habilidades automáticas em fase futura.

---

# Histórico de Alterações

* 2026-06-10: removidos modos de combate.
* 2026-06-10: introduzida filosofia de build.
* 2026-06-11: estratégia legada removida e combate separado de recompensa e progressão.
* 2026-06-11: apresentação ranged do Arqueiro adicionada sem mover cálculo de dano para o projétil.
* 2026-06-10: reorganização completa do sistema de combate.
* 2026-06-10: alinhamento com Progressão e Sistema de Itens.
* 2026-06-10: documento reestruturado para separar combate, fórmulas, habilidades, monstros e recompensas.
