# Identidade de Taskbar

## Objetivo

Definir o diferencial do TBH2 como um RPG Idle Companion executado na área de trabalho.

O objetivo deste documento é estabelecer como o jogo deve se comportar, quais limites deve respeitar e quais experiências tornam o TBH2 diferente de outros Idle RPGs.

TBH2 não é apenas um jogo em janela pequena.

TBH2 é um companheiro visual de jornada.

---

## Status

Draft

---

## Dependências

* Visão do Projeto
* Gameplay Central
* UI e UX
* Companion System
* Save System

---

# Visão Geral

TBH2 foi projetado para permanecer aberto enquanto o usuário utiliza o computador.

O jogo ocupa um espaço pequeno, discreto e contínuo.

A experiência desejada é:

> "Meu aventureiro continua sua jornada enquanto eu trabalho, estudo ou uso o computador."

A identidade de Taskbar deve reforçar:

* presença discreta;
* baixa interrupção;
* progresso contínuo;
* sensação de companhia;
* observação periférica.

---

# Diferencial do TBH2

A maioria dos Idle RPGs existe como:

* tela principal;
* aba de navegador;
* aplicativo mobile;
* menu de números.

TBH2 deve existir como:

* janela lateral;
* companion de desktop;
* pequena jornada visual;
* presença contínua na rotina do usuário.

O diferencial não é apenas o formato.

O diferencial é a sensação de que existe um mundo acontecendo ao lado do usuário.

---

# Princípios da Identidade Taskbar

## 1. Presença Discreta

O jogo deve permanecer visível sem atrapalhar.

A janela deve ser compacta, legível e estável.

O jogador deve conseguir manter o TBH2 aberto durante outras atividades.

---

## 2. Atenção Periférica

O jogador não deve precisar observar o jogo constantemente.

A interface deve comunicar progresso mesmo com olhares rápidos.

Exemplos:

* herói caminhando;
* inimigo encontrado;
* item raro obtido;
* chefe iniciado;
* nível alcançado.

---

## 3. Jornada Contínua

A tela deve sempre transmitir movimento.

Mesmo quando o jogador não interage, o herói deve parecer ativo.

A exploração contínua é parte central da identidade do projeto.

---

## 4. Baixa Frequência de Interação

O jogador toma decisões importantes em momentos específicos.

Exemplos:

* trocar equipamentos;
* revisar atributos;
* configurar habilidades;
* enfrentar chefes;
* observar recompensas.

O jogo não deve exigir cliques repetitivos.

---

## 5. Progressão Silenciosa

O progresso deve acontecer sem interromper o usuário.

O jogo pode informar eventos importantes, mas não deve exigir atenção imediata.

O TBH2 deve respeitar o foco do usuário.

---

# Limites de Atenção

O TBH2 deve evitar:

* pop-ups frequentes;
* alertas sonoros excessivos;
* notificações invasivas;
* animações que escondem informações importantes;
* eventos que exigem ação imediata.

Eventos importantes devem ser apresentados de forma clara, mas discreta.

Exemplos aceitáveis:

* brilho no loot feed;
* destaque visual de item raro;
* animação breve de level up;
* aviso visual de chefe.

---

# Integração com o Uso do Computador

A integração com o uso do computador deve ser simples, local e opcional.

Possibilidades futuras:

* bônus por sessão ativa;
* streak diário;
* recompensas por retorno;
* eventos por horário do dia;
* descanso do aventureiro após longos períodos.

Essas mecânicas devem reforçar a identidade de Companion.

Não devem transformar o jogo em ferramenta de produtividade.

---

# Privacidade

O TBH2 não deve observar conteúdo do usuário.

O jogo não deve ler:

* janelas abertas;
* textos digitados;
* sites acessados;
* arquivos pessoais;
* aplicativos em uso;
* conversas;
* dados sensíveis.

Qualquer integração com o sistema deve ser local, limitada e transparente.

---

# Sinais Locais Permitidos

Sinais aceitáveis para futuras mecânicas:

* tempo de sessão do jogo;
* horário local;
* dias consecutivos jogados;
* tempo desde a última abertura;
* progresso salvo;
* eventos internos do jogo.

Esses sinais são suficientes para criar sistemas de presença sem invadir privacidade.

---

# Bem-Estar

O TBH2 deve respeitar o tempo do usuário.

O jogo não deve incentivar comportamento compulsivo.

A progressão deve funcionar mesmo com baixa interação.

O jogador deve sentir:

> "O jogo continua comigo."

E não:

> "Preciso ficar preso ao jogo."

---

# Comportamento Esperado da Janela

A janela deve ser:

* compacta;
* estável;
* legível;
* reposicionável;
* visualmente agradável;
* compatível com uso prolongado.

Tamanho base recomendado:

360x600

O layout deve considerar que o jogador pode manter a janela aberta ao lado de outras aplicações.

---

# Relação com UI e UX

A identidade de Taskbar influencia diretamente a interface.

Prioridades:

* exploração visível;
* informações essenciais sempre acessíveis;
* menus compactos;
* feedback discreto;
* navegação simples.

A interface deve evitar excesso de painéis simultâneos.

O mundo deve continuar sendo o elemento principal.

---

# Relação com Gameplay

A identidade de Taskbar reforça o modelo Idle Companion.

O jogador não controla ações individuais.

O jogador prepara o personagem.

O jogo executa a jornada.

O resultado depende de:

* equipamentos;
* atributos;
* habilidades;
* classe;
* progressão.

---

# Regras

* O jogo deve funcionar bem em atenção periférica.
* O jogo não deve exigir microgerenciamento constante.
* A janela não deve atrapalhar o uso normal do computador.
* O mundo deve permanecer visualmente ativo.
* Notificações devem ser discretas.
* Integrações com o computador devem ser opcionais.
* O jogo não deve acessar dados sensíveis.
* A privacidade do usuário deve ser preservada.
* Toda mecânica de Taskbar deve reforçar a sensação de jornada contínua.

---

# Fora do Escopo

Não implementar:

* leitura de aplicativos abertos;
* monitoramento de produtividade;
* rastreamento de navegação;
* análise de textos digitados;
* coleta de arquivos locais;
* notificações agressivas;
* mecânicas que punem ausência.

---

# Dados Planejados

Possíveis dados internos:

* session_time;
* last_opened_at;
* current_streak;
* total_play_time;
* current_map;
* current_act;
* current_difficulty;
* recent_events;
* idle_rewards_pending.

Esses dados pertencem ao jogo e não dependem de monitoramento externo.

---

# Critérios de Sucesso

A identidade de Taskbar será considerada bem-sucedida quando o jogador:

* mantiver o jogo aberto por longos períodos;
* conseguir acompanhar progresso com olhares rápidos;
* sentir que o aventureiro está sempre em jornada;
* não se sentir interrompido;
* retornar ao jogo por curiosidade e progresso;
* perceber o TBH2 como companhia visual, não como obrigação.

---

# Pendências

* Definir comportamento da janela sempre visível.
* Definir opções de transparência ou modo compacto.
* Definir se haverá notificações internas.
* Definir sistema de streak diário.
* Definir possíveis bônus por sessão.
* Validar legibilidade em monitores diferentes.
* Validar consumo de CPU durante longas sessões.

---

# Histórico de Alterações

* 2026-06-10: criado template modular.
* 2026-06-10: identidade de Taskbar definida como Companion RPG.
* 2026-06-10: limites de privacidade documentados.
* 2026-06-10: princípios de atenção periférica e presença discreta definidos.
