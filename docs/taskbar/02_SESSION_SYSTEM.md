# Sistema de Sessão

## Objetivo

Definir como o TBH2 reconhece tempo de sessão, presença contínua e recompensas limitadas sem incentivar comportamento artificial ou compulsivo.

O Sistema de Sessão existe para reforçar a identidade de Taskbar Companion.

Ele deve fazer o jogador sentir que seu aventureiro está presente durante sua rotina, sem transformar o jogo em obrigação.

---

## Status

Draft

---

## Dependências

* Identidade de Taskbar
* Companion System
* Save System
* Progressão
* Loot e Economia

---

# Visão Geral

TBH2 é um jogo pensado para permanecer aberto durante o uso normal do computador.

O Sistema de Sessão registra períodos em que o jogo está ativo e utiliza essa informação para criar pequenos marcos de presença.

Esses marcos podem gerar:

* feedback visual;
* pequenas recompensas;
* eventos internos;
* sensação de continuidade.

O objetivo não é premiar tempo infinito.

O objetivo é valorizar sessões naturais de jogo.

---

# Filosofia do Sistema

A sessão deve reforçar a ideia de jornada contínua.

O jogador deve sentir:

> "Meu aventureiro esteve comigo durante esse período."

E não:

> "Preciso deixar o jogo aberto para não perder vantagem."

A presença deve ser agradável.

Nunca obrigatória.

---

# Definição de Sessão

Uma sessão começa quando:

* o jogo é aberto;
* o save é carregado;
* o loop principal inicia.

Uma sessão termina quando:

* o jogo é fechado;
* o processo é encerrado;
* o estado é salvo;
* o jogador sai voluntariamente.

---

# Tempo de Sessão

O tempo de sessão representa o período em que o TBH2 permaneceu ativo.

Esse tempo pode ser usado para:

* estatísticas;
* marcos visuais;
* pequenas recompensas;
* eventos de presença.

Exemplos:

* 15 minutos de jornada;
* 30 minutos de jornada;
* 1 hora de jornada;
* 2 horas de jornada.

---

# Marcos de Sessão

Marcos são eventos simples baseados em tempo ativo.

Exemplos:

## 15 Minutos

Mensagem possível:

> O aventureiro mantém o passo.

Recompensa:

* pequena quantidade de ouro;
* registro visual no feed.

---

## 30 Minutos

Mensagem possível:

> A estrada continua, mas o aventureiro parece mais confiante.

Recompensa:

* pequeno bônus de XP;
* chance de evento ambiental.

---

## 1 Hora

Mensagem possível:

> Uma longa jornada foi percorrida.

Recompensa:

* bônus limitado;
* possível recompensa de presença.

---

## 2 Horas

Mensagem possível:

> O aventureiro fez bom progresso nesta sessão.

Recompensa:

* recompensa de sessão consolidada.

---

# Limite de Recompensas

O sistema deve possuir limites claros.

Recompensas de sessão não devem crescer indefinidamente.

Exemplo:

* bônus máximo por dia;
* limite de marcos recompensados;
* redução após longas sessões;
* ausência de vantagem por manter o jogo aberto sem parar.

Objetivo:

Evitar exploração artificial.

---

# Recompensas Permitidas

Recompensas de sessão devem ser leves.

Exemplos aceitáveis:

* pequena quantidade de ouro;
* pequeno bônus de XP;
* evento visual;
* mensagem de jornada;
* registro no histórico;
* leve aumento temporário de moral.

Essas recompensas não devem substituir:

* loot;
* chefes;
* mapas;
* dificuldades;
* progressão principal.

---

# Recompensas Não Recomendadas

Evitar recompensas que criem obrigação.

Não utilizar:

* itens raros garantidos;
* progressão exclusiva por tempo aberto;
* penalidade por fechar o jogo;
* bônus acumulativo infinito;
* vantagem desproporcional por sessões longas.

O jogador não deve ser punido por sair.

---

# Sessões Curtas

O TBH2 deve funcionar bem em sessões curtas.

Mesmo com poucos minutos, o jogador deve perceber:

* movimento;
* encontros;
* progresso;
* possível recompensa.

Sessões curtas devem ser válidas.

---

# Sessões Longas

Sessões longas devem ser reconhecidas, mas não exploradas.

O sistema pode registrar:

* tempo total;
* eventos concluídos;
* mapas avançados;
* loot obtido;
* ouro ganho.

Porém os bônus adicionais devem possuir limite.

---

# Retorno ao Jogo

Ao retornar após fechar o jogo, o jogador pode receber um resumo.

Exemplo:

* tempo da última sessão;
* itens obtidos;
* níveis ganhos;
* mapas concluídos;
* ouro acumulado.

Esse resumo reforça a sensação de continuidade.

---

# Relação com Progressão

O Sistema de Sessão não deve ser a principal fonte de poder.

A progressão principal continua vindo de:

* combate;
* loot;
* equipamentos;
* mapas;
* chefes;
* dificuldades.

A sessão apenas complementa a experiência.

---

# Relação com Bem-Estar

O sistema deve respeitar o tempo do jogador.

Regras importantes:

* não punir ausência;
* não exigir presença contínua;
* não criar urgência artificial;
* não pressionar o jogador a manter o jogo aberto.

O jogador deve sentir companhia, não cobrança.

---

# Dados Locais Permitidos

O sistema pode registrar apenas dados internos do jogo.

Exemplos:

* session_start_time;
* session_duration;
* total_play_time;
* last_session_duration;
* daily_session_reward_claimed;
* session_milestones_claimed;
* last_opened_at.

O sistema não deve observar conteúdo externo do computador.

---

# Regras

* Sessões devem gerar presença, não obrigação.
* Recompensas devem possuir limite.
* Sessões curtas devem ser válidas.
* Sessões longas não devem gerar vantagem infinita.
* O jogador nunca deve ser punido por fechar o jogo.
* O sistema não deve monitorar aplicativos, sites ou arquivos.
* As recompensas de sessão não substituem loot, mapas ou chefes.
* O sistema deve reforçar a identidade de Companion.

---

# Fora do Escopo

Não implementar neste sistema:

* monitoramento de produtividade;
* leitura de aplicativos abertos;
* detecção de atividade do teclado;
* punição por inatividade;
* recompensas infinitas por tempo aberto;
* ranking por tempo de sessão;
* obrigação diária.

---

# Dados Planejados

SessionData:

* session_id;
* started_at;
* ended_at;
* duration_seconds;
* milestones_claimed;
* rewards_granted;
* maps_completed;
* enemies_defeated;
* items_found;
* gold_earned;
* xp_earned.

---

# Critérios de Sucesso

O Sistema de Sessão será considerado saudável quando:

* reforçar a sensação de jornada;
* funcionar bem em sessões curtas e longas;
* gerar pequenos momentos de satisfação;
* não criar obrigação;
* não substituir a progressão principal;
* respeitar a privacidade e o bem-estar do jogador.

---

# Pendências

* Definir duração dos marcos.
* Definir limite diário de recompensa.
* Definir se haverá resumo de sessão.
* Definir integração com feed de eventos.
* Definir se haverá estatísticas visíveis ao jogador.
* Definir impacto futuro de moral ou presença.
* Validar se o sistema será implementado antes ou depois do offline progress.

---

# Histórico de Alterações

* 2026-06-10: criado template modular.
* 2026-06-10: definida filosofia de presença sem obrigação.
* 2026-06-10: adicionados marcos de sessão e limites de recompensa.
* 2026-06-10: registrados limites de privacidade e bem-estar.
