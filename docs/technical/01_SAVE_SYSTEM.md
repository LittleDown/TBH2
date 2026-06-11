# Sistema de Save

## Objetivo

Definir o sistema de persistência do TBH2, incluindo salvamento, carregamento, compatibilidade entre versões, migrações e recuperação de progresso.

O Save System é responsável por garantir que a jornada do jogador seja preservada com segurança.

Ele deve proteger:

* progresso do herói;
* equipamentos;
* inventário;
* ouro;
* experiência;
* mapa atual;
* ato atual;
* dificuldade atual;
* progresso de campanha;
* estados futuros de sessão, diário e companion.

---

## Status

Draft

---

## Dependências

* Modelo de Dados
* Progressão
* Sistema de Herói
* Sistema de Itens
* Loot e Economia
* Estrutura do Mundo
* Sistema de Sessão
* Sistema Diário
* Companion System

---

# Visão Geral

O Sistema de Save deve armazenar o estado persistente do jogo de forma simples, segura e compatível com versões futuras.

Como o TBH2 é um Idle RPG Companion, o jogador pode manter o jogo aberto por longos períodos.

Por isso, o save deve ocorrer automaticamente e em momentos críticos.

O jogador não deve precisar se preocupar em salvar manualmente.

---

# Responsabilidades do Save

O Save System deve:

* salvar progresso automaticamente;
* carregar saves existentes;
* criar novo save quando necessário;
* aplicar valores padrão para campos ausentes;
* migrar saves antigos;
* proteger contra corrupção de arquivo;
* manter backup recente;
* evitar perda de progresso em caso de erro.

---

# Formato

## Formato Inicial

O formato inicial recomendado é JSON local.

Motivos:

* simples de debugar;
* fácil de versionar;
* fácil de migrar;
* compatível com MVP;
* legível durante desenvolvimento.

---

## Arquivo Principal

Nome sugerido:

```text
save_data.json
```

---

## Arquivo de Backup

Nome sugerido:

```text
save_data.backup.json
```

O backup deve representar o último save válido conhecido.

---

# Versionamento

Todo save deve possuir versão.

Exemplo:

```text
save_version: 1
```

A versão do save é usada para:

* detectar saves antigos;
* aplicar migrações;
* adicionar novos campos;
* manter compatibilidade.

---

# Ciclo de Salvamento

O jogo deve salvar automaticamente em eventos importantes.

## Eventos de Save

Salvar ao:

* iniciar novo personagem;
* ganhar nível;
* obter item relevante;
* equipar item;
* vender item;
* alterar atributos;
* alterar habilidades;
* concluir combate;
* avançar mapa;
* derrotar chefe;
* mudar ato;
* mudar dificuldade;
* fechar o jogo.

---

# Autosave

O jogo também pode possuir autosave por intervalo.

Intervalo inicial sugerido:

```text
30 segundos
```

Esse valor pode ser ajustado depois.

O autosave não deve causar travamentos perceptíveis na interface.

---

# Salvamento Atômico

O save deve ser atômico.

O jogo não deve sobrescrever diretamente o arquivo principal sem segurança.

Fluxo recomendado:

1. Gerar novo estado de save.
2. Validar dados.
3. Escrever em arquivo temporário.
4. Confirmar escrita.
5. Substituir arquivo principal.
6. Atualizar backup do último save válido.

Exemplo de arquivo temporário:

```text
save_data.tmp.json
```

Objetivo:

Evitar corrupção caso o jogo feche durante a escrita.

---

# Carregamento

Ao iniciar, o jogo deve seguir a ordem:

1. Procurar save principal.
2. Validar estrutura.
3. Verificar versão.
4. Aplicar migrações se necessário.
5. Aplicar defaults para campos ausentes.
6. Carregar jogo.

Caso o save principal esteja inválido, tentar carregar o backup.

---

# Novo Save

Se nenhum save válido existir, o jogo deve criar um novo estado inicial.

O novo save deve conter:

* herói inicial;
* nível inicial;
* experiência inicial;
* ouro inicial;
* inventário inicial;
* equipamento inicial;
* mapa inicial;
* ato inicial;
* dificuldade inicial;
* versão atual do save.

---

# Defaults

Campos ausentes não devem quebrar o carregamento.

Quando um campo não existir em um save antigo, o sistema deve aplicar valor padrão.

Exemplos:

```text
difficulty = "normal"
current_act = 1
current_map = 1
gold = 0
inventory = []
```

Defaults devem ser centralizados.

Evitar espalhar valores padrão em múltiplos pontos do código.

---

# Migrações

Migrações são transformações aplicadas em saves antigos.

Exemplo:

```text
save_version 1
↓
save_version 2
```

Uma migração pode:

* adicionar campos;
* renomear campos;
* remover campos obsoletos;
* converter estruturas antigas;
* normalizar dados.

---

## Regra de Migração

Migrações devem ser incrementais.

Exemplo:

```text
v1 -> v2
v2 -> v3
v3 -> v4
```

Evitar migração direta genérica sem histórico.

Isso facilita manutenção.

---

# Compatibilidade

O Save System deve ser tolerante a mudanças futuras.

Sistemas planejados que podem exigir novos campos:

* classes;
* habilidades;
* raças;
* companion;
* moral;
* sessão;
* sistema diário;
* dungeons;
* party companions;
* dificuldades avançadas.

Esses sistemas não devem quebrar saves antigos.

---

# Recuperação de Erros

Se o save principal estiver corrompido:

1. registrar erro;
2. tentar carregar backup;
3. se backup for válido, restaurar backup;
4. se backup também falhar, criar novo save apenas após confirmação ou fallback seguro.

Durante desenvolvimento, o erro deve ser visível no console/log.

No produto final, o erro deve ser apresentado de forma simples.

---

# Validação

Antes de salvar ou carregar, o sistema deve validar campos essenciais.

Campos mínimos:

* save_version;
* hero;
* progression;
* inventory;
* equipment;
* current_act;
* current_map;
* difficulty.

Se algum campo crítico estiver ausente, aplicar defaults quando possível.

Se não for possível recuperar, usar backup.

---

# O que Deve Ser Salvo

O save deve armazenar estado persistente.

Exemplos:

* dados do herói;
* classe;
* nível;
* experiência;
* atributos;
* equipamentos;
* inventário;
* ouro;
* progresso de mapa;
* progresso de ato;
* dificuldade;
* chefes derrotados;
* configurações básicas;
* dados de sessão;
* dados diários;
* estado do companion.

---

# O que Não Deve Ser Salvo

Evitar salvar estado temporário desnecessário.

Exemplos:

* frame atual de animação;
* posição exata de partículas;
* efeitos visuais temporários;
* timers internos descartáveis;
* estados de UI não essenciais.

Esses dados podem ser reconstruídos ao carregar o jogo.

---

# Relação com Offline Progress

O Save System deve preparar espaço para progresso offline futuro.

Dados possíveis:

* last_saved_at;
* last_opened_at;
* offline_progress_enabled;
* offline_rewards_pending.

O cálculo de progresso offline deve ser documentado separadamente.

---

# Relação com Configurações

Configurações podem ser separadas do save principal.

Exemplo:

```text
settings.json
```

Configurações possíveis:

* volume;
* tamanho da janela;
* posição da janela;
* modo compacto;
* sempre visível;
* idioma;
* preferências de notificação.

Separar configurações do progresso evita perda de personagem por erro em preferência visual.

---

# Segurança

O save local não precisa impedir edição manual durante o desenvolvimento.

Porém deve evitar corrupção acidental.

Prioridades:

* atomicidade;
* backup;
* validação;
* migração;
* defaults seguros.

Anticheat não faz parte do escopo atual.

---

# Regras

* Todo save deve possuir versão.
* O jogo deve salvar automaticamente.
* O save deve ser atômico.
* O sistema deve manter backup válido.
* Campos ausentes devem receber defaults quando possível.
* Saves antigos devem ser migrados.
* Save corrompido não deve apagar progresso imediatamente.
* Estado temporário de UI não deve ser salvo no save principal.
* Configurações podem ficar separadas do progresso.
* O jogador não deve perder progresso por erro simples de compatibilidade.

---

# Fora do Escopo

Não implementar neste sistema inicial:

* cloud save;
* sincronização entre dispositivos;
* anticheat;
* criptografia obrigatória;
* multiplayer persistence;
* rollback avançado;
* múltiplos perfis complexos.

Esses recursos podem ser avaliados futuramente.

---

# Dados Planejados

Referenciar o esquema oficial em:

```text
02_DATA_MODEL.md
```

Este documento não deve duplicar todo o modelo de dados.

Ele define regras de persistência.

O esquema detalhado deve permanecer no Modelo de Dados.

Campos técnicos mínimos esperados:

```text
save_version
created_at
updated_at
last_saved_at
hero
progression
inventory
equipment
world
settings_reference
session_state
daily_state
companion_state
```

---

# Critérios de Sucesso

O Sistema de Save será considerado bem-sucedido quando:

* o jogador não perder progresso em uso normal;
* saves antigos continuarem carregando após atualizações;
* novos campos puderem ser adicionados com segurança;
* erros de arquivo puderem ser recuperados por backup;
* o sistema for simples de debugar durante o desenvolvimento;
* o save não travar a experiência de Taskbar.

---

# Pendências

* Definir versão inicial do save.
* Definir caminho oficial do arquivo.
* Definir formato final do SaveData.
* Definir defaults globais.
* Definir primeira camada de migração.
* Definir frequência de autosave.
* Definir política de backup.
* Definir separação entre save e settings.
* Definir integração futura com offline progress.

---

# Histórico de Alterações

* 2026-06-10: criado template modular.
* 2026-06-10: definido JSON local como formato inicial recomendado.
* 2026-06-10: adicionadas regras de versionamento, migração e backup.
* 2026-06-10: definida filosofia de recuperação e compatibilidade.
* 2026-06-11: schema elevado para v4 com migração automática de `class_id = "warrior"`.
