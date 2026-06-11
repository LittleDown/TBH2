# Sistema de Companion

## Objetivo

Definir o sistema de personalidade, moral e feedback do herói como companheiro de jornada no TBH2.

O Companion existe para reforçar a identidade de Taskbar do projeto.

Ele deve fazer o jogador sentir que existe um aventureiro presente, viajando e evoluindo ao lado dele, sem transformar o jogo em chat, assistente ou sistema narrativo invasivo.

---

## Status

Draft

---

## Dependências

* Identidade de Taskbar
* Sistema de Herói
* UI e UX
* Sistema de Sessão
* Sistema Diário
* Progressão
* Combate

---

# Visão Geral

O herói do TBH2 não é apenas uma ficha de atributos.

Ele é o centro visual e emocional da jornada.

O Sistema de Companion define como esse herói expressa presença através de:

* pequenas mensagens;
* estados de moral;
* reações a eventos;
* feedback visual;
* comentários contextuais;
* sinais discretos de progresso.

O objetivo é criar vínculo sem exigir atenção constante.

---

# Filosofia do Companion

O Companion deve funcionar como uma presença silenciosa e viva.

O jogador deve sentir:

> "Meu aventureiro está em jornada."

E não:

> "O jogo está tentando conversar comigo o tempo todo."

O Companion deve reforçar:

* continuidade;
* presença;
* personalidade;
* progresso;
* vínculo com o personagem.

Mas nunca deve interromper o fluxo principal do jogo.

---

# O que o Companion Não É

O Companion não é:

* chatbot;
* assistente pessoal;
* narrador constante;
* sistema de produtividade;
* ferramenta emocional;
* substituto de gameplay;
* fonte principal de recompensas.

Ele é uma camada leve de presença e feedback.

---

# Personalidade

A personalidade define o tom geral do herói.

Ela pode variar de acordo com:

* classe;
* raça futura;
* eventos da jornada;
* moral;
* vitórias;
* derrotas;
* tempo de sessão.

A personalidade deve ser simples, curta e compatível com a interface compacta.

---

## Exemplos de Tons

### Guerreiro

Tom:

* direto;
* determinado;
* resistente.

Exemplos:

> A estrada não vai ceder. Eu também não.

> Mais um inimigo caiu.

---

### Arqueiro

Tom:

* atento;
* preciso;
* observador.

Exemplos:

> Há movimento entre as árvores.

> Um bom disparo muda tudo.

---

### Mago

Tom:

* analítico;
* curioso;
* arcano.

Exemplos:

> Há energia estranha neste lugar.

> O mundo guarda padrões invisíveis.

---

### Curandeiro

Tom:

* calmo;
* protetor;
* resiliente.

Exemplos:

> Ainda há forças para seguir.

> Nem toda vitória precisa ser rápida.

---

# Moral

Moral representa o estado geral do herói durante a jornada.

Ela não deve ser um sistema pesado.

A moral deve ser usada principalmente para:

* variação de mensagens;
* pequenos feedbacks visuais;
* sensação de presença;
* eventos leves.

---

## Estados de Moral

### Estável

Estado padrão.

O herói segue a jornada normalmente.

---

### Confiante

Ativado após:

* sequência de vitórias;
* item relevante encontrado;
* chefe derrotado;
* avanço de mapa.

Efeito:

* mensagens mais positivas;
* postura visual mais firme;
* possível brilho leve no feed.

---

### Cansado

Ativado após:

* muitas derrotas;
* sessão muito longa;
* falhas repetidas contra chefe.

Efeito:

* mensagens mais contidas;
* sugestão leve de fortalecimento;
* sem punição severa.

---

### Ferido

Ativado após derrota significativa.

Efeito:

* feedback visual discreto;
* mensagem curta;
* incentivo a revisar equipamentos ou progressão.

---

# Limites da Moral

A moral não deve punir o jogador de forma agressiva.

Evitar:

* redução forte de atributos;
* bloqueio de conteúdo;
* perda de itens;
* perda de progresso;
* mensagens de culpa.

Permitido:

* pequenas variações narrativas;
* leve bônus temporário futuro;
* feedback visual;
* mudanças sutis de tom.

---

# Mensagens Contextuais

Mensagens contextuais são frases curtas exibidas em momentos relevantes.

Devem ser:

* breves;
* raras;
* úteis;
* não intrusivas.

---

## Eventos que Podem Gerar Mensagens

* início de sessão;
* retorno diário;
* avanço de mapa;
* novo ato desbloqueado;
* item raro encontrado;
* derrota contra chefe;
* vitória contra chefe;
* level up;
* mudança de dificuldade;
* longa sessão.

---

# Exemplos de Mensagens

## Início de Sessão

> A jornada continua.

> A estrada nos espera.

---

## Avanço de Mapa

> Este lugar parece diferente.

> Estamos mais longe do que antes.

---

## Item Encontrado

> Isto pode ser útil.

> Um achado raro na estrada.

---

## Derrota

> Ainda não estamos prontos.

> Talvez seja hora de rever o equipamento.

---

## Vitória Contra Chefe

> Este lugar foi vencido.

> A estrada adiante está aberta.

---

# Feedback Não Intrusivo

O Companion deve se comunicar mais por presença do que por texto.

Feedbacks recomendados:

* postura do herói;
* animação curta;
* expressão visual;
* brilho leve;
* ícone de moral;
* feed discreto;
* pequenas falas ocasionais.

O texto deve ser apoio.

Não o centro da experiência.

---

# Frequência de Mensagens

Mensagens não devem aparecer a todo momento.

Regra inicial sugerida:

* eventos comuns: pouca ou nenhuma mensagem;
* eventos importantes: mensagem curta;
* eventos raros: destaque maior;
* chefes: mensagem especial;
* retorno diário: uma mensagem.

O excesso de mensagens reduz o valor do Companion.

---

# Relação com Gameplay

O Companion não altera o controle do jogador.

O jogador continua atuando como preparador da build.

O Companion pode sugerir estados gerais, mas não deve dar comandos diretos constantes.

Exemplo aceitável:

> Talvez seja hora de fortalecer o equipamento.

Evitar:

> Troque sua espada agora.

---

# Relação com Progressão

O Companion pode reagir a progresso.

Exemplos:

* novo nível;
* novo mapa;
* novo ato;
* nova dificuldade;
* item importante;
* chefe derrotado.

Essas reações reforçam a jornada, mas não substituem sistemas principais.

---

# Relação com Taskbar

Por ser um jogo de Taskbar, o Companion deve funcionar em atenção periférica.

O jogador deve conseguir perceber o estado do herói sem ler textos longos.

Prioridades:

* clareza visual;
* mensagens curtas;
* eventos discretos;
* baixa interrupção.

---

# Privacidade

O Companion não deve observar o usuário.

Ele reage apenas a eventos internos do jogo.

Não utilizar:

* aplicativos abertos;
* textos digitados;
* sites acessados;
* arquivos locais;
* atividade externa do computador.

A personalidade do herói nasce da jornada dentro do TBH2.

Não do comportamento real do usuário fora do jogo.

---

# Dados Planejados

CompanionState:

* hero_id;
* personality_type;
* morale_state;
* last_message_id;
* last_message_at;
* recent_events;
* boss_defeats;
* map_progress;
* session_duration;
* daily_return_state;
* defeat_count_recent;
* victory_count_recent.

---

# Regras

* O Companion deve reforçar presença, não conversa constante.
* Mensagens devem ser curtas.
* Feedback visual tem prioridade sobre texto.
* Moral não deve punir severamente.
* O sistema não deve observar dados externos do computador.
* O Companion deve reagir apenas a eventos internos do jogo.
* O herói deve parecer vivo, mas não invasivo.
* O sistema deve respeitar a baixa frequência de interação do TBH2.

---

# Fora do Escopo

Não implementar neste sistema:

* chatbot livre;
* diálogo aberto;
* leitura de comportamento externo;
* personalidade baseada em dados pessoais;
* mensagens longas constantes;
* cobrança por ausência;
* punição pesada de moral;
* dependência obrigatória de Companion para progredir.

---

# Critérios de Sucesso

O Sistema de Companion será considerado bem-sucedido quando:

* o herói parecer presente;
* o jogador sentir vínculo com o aventureiro;
* as mensagens não atrapalharem;
* a moral adicionar atmosfera sem punição;
* o sistema reforçar a identidade de Taskbar;
* o jogo continuar funcionando bem em atenção periférica.

---

# Pendências

* Definir personalidades iniciais por classe.
* Definir estados finais de moral.
* Definir lista inicial de mensagens.
* Definir frequência máxima de mensagens.
* Definir feedback visual por estado.
* Definir integração com sessão e sistema diário.
* Definir se moral terá efeitos mecânicos leves.
* Validar legibilidade das mensagens na janela compacta.

---

# Histórico de Alterações

* 2026-06-10: criado template modular.
* 2026-06-10: Companion definido como presença do herói.
* 2026-06-10: moral documentada como sistema leve.
* 2026-06-10: limites contra comportamento invasivo registrados.
