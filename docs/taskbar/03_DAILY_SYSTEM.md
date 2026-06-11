# Sistema Diário

## Objetivo

Definir retornos diários, eventos por horário local e continuidade de presença sem criar punição por ausência.

O Sistema Diário existe para reforçar a identidade do TBH2 como Companion de Taskbar.

Ele deve valorizar o retorno do jogador sem transformar o jogo em obrigação.

---

## Status

Draft

---

## Dependências

* Identidade de Taskbar
* Sistema de Sessão
* Save System
* Progressão
* Loot e Economia

---

# Visão Geral

O Sistema Diário representa pequenas mudanças e recompensas associadas ao retorno do jogador em dias diferentes.

Ele pode utilizar:

* data local;
* horário local;
* último dia jogado;
* retorno após ausência;
* eventos internos do jogo.

O objetivo é criar sensação de continuidade.

Não criar cobrança.

---

# Filosofia do Sistema Diário

O jogador deve sentir:

> "Meu aventureiro continuou sua jornada."

E não:

> "Perdi algo porque não entrei ontem."

O TBH2 não deve punir ausência.

O retorno deve ser positivo, mesmo após vários dias sem abrir o jogo.

---

# Retorno Diário

Ao abrir o jogo em um novo dia, o sistema pode apresentar um pequeno resumo.

Exemplos:

* progresso recente;
* jornada atual;
* mapa atual;
* eventos encontrados;
* recompensas acumuladas;
* mensagem de retorno.

Mensagem possível:

> O aventureiro retoma a estrada.

---

# Dias Consecutivos

Dias consecutivos podem existir como registro.

Mas não devem ser usados como pressão.

Permitido:

* estatística de presença;
* pequena mensagem visual;
* marco simbólico;
* conquista opcional.

Evitar:

* perda de recompensa importante;
* punição por quebrar sequência;
* bônus infinito;
* vantagem obrigatória.

---

# Streak Saudável

Caso exista streak, ela deve seguir regras saudáveis.

Regras:

* quebrar streak não gera punição;
* recompensas são leves;
* sequência não deve conceder poder essencial;
* o jogador pode retornar normalmente após ausência.

Exemplo:

3 dias consecutivos:

* pequena quantidade de ouro;
* mensagem visual;
* registro no histórico.

7 dias consecutivos:

* recompensa cosmética futura;
* título simbólico;
* evento visual.

---

# Ausência do Jogador

Ausência não deve ser tratada como falha.

Ao retornar após vários dias, o jogo pode apresentar:

* resumo da última sessão;
* mensagem de boas-vindas;
* recompensa leve de retorno;
* continuidade da jornada.

Mensagem possível:

> A estrada esperou. O aventureiro está pronto para seguir.

---

# Horário Local

O horário local pode ser utilizado para variações leves.

Exemplos:

## Manhã

* iluminação mais clara;
* eventos de início de jornada;
* mensagens de partida.

## Tarde

* clima estável;
* exploração ativa;
* eventos comuns.

## Noite

* iluminação escura;
* chance de eventos atmosféricos;
* monstros visuais mais sombrios.

Essas variações devem ser principalmente visuais.

Não devem bloquear conteúdo importante.

---

# Eventos por Período

Eventos por período podem criar sensação de mundo vivo.

Exemplos:

* névoa pela manhã;
* pôr do sol no fim da tarde;
* corvos à noite;
* chuva ocasional;
* viajantes raros;
* fogueiras distantes.

Esses eventos devem reforçar atmosfera.

Não devem exigir ação imediata.

---

# Recompensas Diárias

Recompensas diárias devem ser limitadas e leves.

Permitido:

* pequena quantidade de ouro;
* pequeno bônus de XP;
* evento visual;
* mensagem de retorno;
* item comum ou mágico ocasional;
* bônus simbólico.

Evitar:

* item raro garantido diariamente;
* poder exclusivo;
* vantagem obrigatória;
* recompensas que forcem login diário.

---

# Limite de Recompensas

O sistema deve possuir limite diário.

Exemplo:

* uma recompensa diária por dia;
* marcos leves por retorno;
* sem acúmulo infinito;
* sem multiplicador permanente por sequência.

O objetivo é evitar exploração e pressão.

---

# Continuidade

O Sistema Diário deve reforçar a ideia de que o mundo continua existindo.

Mesmo que o jogador fique ausente, a experiência deve continuar acolhedora.

O jogo não deve usar frases de culpa.

Evitar mensagens como:

* Você perdeu recompensas.
* Sua sequência foi quebrada.
* Você ficou muito tempo ausente.
* Volte amanhã para não perder.

Preferir mensagens como:

* A jornada continua.
* O aventureiro retorna à estrada.
* Um novo dia começa.
* Há novos caminhos pela frente.

---

# Relação com Progressão

O Sistema Diário não deve ser fonte principal de evolução.

A progressão principal continua vindo de:

* mapas;
* combate;
* loot;
* equipamentos;
* chefes;
* dificuldades.

O diário apenas adiciona contexto, presença e pequenos incentivos.

---

# Relação com Bem-Estar

O sistema deve respeitar a rotina do jogador.

Regras importantes:

* não punir ausência;
* não criar urgência artificial;
* não exigir login diário;
* não bloquear conteúdo por horário;
* não transformar presença em obrigação.

O jogador deve querer voltar.

Não sentir que precisa voltar.

---

# Dados Locais Permitidos

O sistema pode registrar apenas dados internos e locais do jogo.

Exemplos:

* last_daily_login;
* current_daily_streak;
* best_daily_streak;
* daily_reward_claimed_at;
* last_return_summary_at;
* local_time_period;
* daily_events_seen.

O sistema não deve observar aplicativos, sites, arquivos ou atividade externa do usuário.

---

# Fora do Escopo

Não implementar:

* punição por ausência;
* perda permanente de recompensas;
* conteúdo essencial limitado por horário;
* streak obrigatória;
* ranking diário;
* monitoramento externo;
* notificações agressivas;
* mecânicas de pressão para retorno.

---

# Regras

* O retorno diário deve ser positivo.
* Ausência nunca deve gerar punição.
* Recompensas diárias devem ser leves.
* Streaks não devem conceder poder essencial.
* Horário local pode alterar atmosfera, não bloquear progresso.
* Eventos diários devem reforçar mundo vivo.
* O sistema não deve criar obrigação diária.
* O jogador deve retornar por curiosidade, não por medo de perder algo.

---

# Dados Planejados

DailyState:

* current_date;
* last_opened_date;
* last_daily_reward_date;
* current_streak;
* best_streak;
* return_days_elapsed;
* daily_reward_claimed;
* current_time_period;
* daily_event_seed;
* daily_events_seen.

---

# Critérios de Sucesso

O Sistema Diário será considerado bem-sucedido quando:

* fizer o mundo parecer contínuo;
* valorizar o retorno do jogador;
* não gerar pressão;
* não punir ausência;
* reforçar a identidade de Companion;
* funcionar bem mesmo para jogadores casuais;
* não substituir progressão, loot ou campanha.

---

# Pendências

* Definir se haverá streak.
* Definir recompensas diárias iniciais.
* Definir mensagens de retorno.
* Definir eventos por horário local.
* Definir resumo após ausência.
* Definir limite diário de recompensa.
* Validar integração com Sistema de Sessão.
* Validar impacto no bem-estar do jogador.

---

# Histórico de Alterações

* 2026-06-10: criado template modular.
* 2026-06-10: definida filosofia de retorno sem punição.
* 2026-06-10: adicionados limites para streaks e recompensas.
* 2026-06-10: registrado uso saudável de horário local e eventos diários.
