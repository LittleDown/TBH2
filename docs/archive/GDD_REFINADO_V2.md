# TBH2 - TaskBar Hero 2

## Game Design Document Refinado para Implementação

**Versão do documento:** 0.3  
**Versão-alvo inicial do jogo:** 0.1  
**Gênero:** Idle RPG de fantasia sombria  
**Plataforma:** Windows  
**Formato:** Taskbar Companion em janela lateral compacta  
**Referências:** Diablo, Warcraft, Dota, Dungeons & Dragons e Melvor Idle

---

## 1. Visão do Jogo

TBH2 é um Idle RPG que acompanha o usuário durante o uso normal do computador.
Em uma pequena janela lateral, um herói percorre mapas, combate inimigos, acumula
ouro, encontra equipamentos e avança por uma campanha persistente.

O jogador não controla golpes individuais. Sua participação acontece por
decisões ocasionais e duradouras, como escolher uma estratégia de combate,
acompanhar a evolução do equipamento e preparar o herói para chefes e
dificuldades superiores.

Sempre que olhar para o jogo, o jogador deve entender:

- onde o herói está;
- qual inimigo está enfrentando;
- quanto falta para concluir o mapa;
- qual estratégia está ativa;
- qual foi a recompensa mais recente;
- qual é a próxima meta relevante.

### Promessa central

> Uma campanha de RPG persistente acontece na lateral da sua tela, com progresso
> automático e decisões leves que respeitam sua atenção.

---

## 2. Fantasia Central

O jogador acompanha um aventureiro que atravessa terras corrompidas em busca da
origem de uma invasão. O herói luta por conta própria, mas sua jornada é orientada
por escolhas de postura, crescimento, equipamento e, em versões futuras, classe.

A fantasia de progressão parte de um viajante com equipamento improvisado e
avança até um campeão capaz de superar chefes, concluir atos e retornar à
campanha em dificuldades mais perigosas.

O herói deve parecer um companheiro persistente, não uma unidade que aguarda
comandos constantes.

---

## 3. Pilares de Design

### 3.1 Progresso com destino

O nível mede poder, enquanto mapas, atos e dificuldades mostram onde esse poder
está sendo aplicado.

### 3.2 Agência de baixa frequência

As decisões do jogador devem ser simples, compreensíveis e permanecer ativas até
que ele deseje alterá-las. Nenhuma decisão deve exigir atenção a cada combate.

### 3.3 Presença discreta

O jogo deve permanecer aberto sem competir com a tarefa principal do usuário.

### 3.4 Recompensas sustentáveis

Experiência oferece crescimento previsível, ouro constrói valor acumulado e loot
gera surpresa durante toda a campanha.

### 3.5 Metas em várias escalas

Combates, mapas, atos e dificuldades fornecem objetivos de segundos, minutos,
sessões e longo prazo.

### 3.6 Baixa punição

A derrota bloqueia temporariamente o avanço, mas não remove progresso permanente.

### 3.7 Expansão em camadas

Classes, habilidades, eventos e sistemas de Taskbar devem se integrar ao núcleo
sem exigir sua reconstrução.

---

## 4. Estrutura de Progressão

A campanha segue:

**Mapa → Ato → Dificuldade**

### 4.1 Mapas

Cada ato possui 10 mapas sequenciais. Cada mapa define:

- nome e temática;
- inimigos disponíveis;
- faixa de desafio;
- quantidade de vitórias necessária;
- escala de experiência, ouro e loot;
- chefe, quando aplicável.

A referência inicial é **10 vitórias por mapa**.

Ao concluir um mapa:

- o progresso é salvo;
- o próximo mapa é desbloqueado;
- o herói avança automaticamente;
- o evento é destacado na interface.

### 4.2 Atos

Os nove primeiros mapas desenvolvem uma região. O décimo contém o chefe que
precisa ser derrotado para concluir o ato.

| Ato | Região | Tema |
|---|---|---|
| Ato I | Fronteira Esquecida | Estradas, bosques e ruínas |
| Ato II | Terras da Cinza | Campos queimados e fortalezas |
| Ato III | Abismo Carmesim | Corrupção demoníaca |

Somente o Ato I integra o conteúdo obrigatório da v0.1.

### 4.3 Dificuldades

1. Normal
2. Veterano
3. Pesadelo
4. Infernal
5. Mítico

Concluir todos os atos desbloqueia a dificuldade seguinte. O herói preserva
nível, experiência, ouro, equipamentos, estatísticas e marcos.

Cada dificuldade aumenta:

- atributos dos inimigos;
- experiência recebida;
- ouro recebido;
- potencial de Poder dos itens;
- conteúdos disponíveis em versões futuras.

Os multiplicadores exatos serão definidos por balanceamento.

### 4.4 Horizontes de objetivo

| Camada | Horizonte | Objetivo |
|---|---|---|
| Combate | Segundos | Derrotar o inimigo atual |
| Mapa | Minutos | Completar a meta de vitórias |
| Ato | Sessões | Preparar-se e derrotar o chefe |
| Dificuldade | Longo prazo | Dominar toda a campanha |

---

## 5. Escopo da V0.1

### Incluído

- herói genérico persistente;
- combate automático;
- estratégias Agressiva, Balanceada e Defensiva;
- experiência e níveis;
- ouro persistente;
- loot escalável por Poder;
- equipamento automático;
- dificuldade Normal;
- Ato I com 10 mapas;
- três inimigos comuns;
- um chefe;
- marcos iniciais;
- interface lateral;
- salvamento e carregamento.

### Preparado conceitualmente

- classes;
- estatísticas secundárias;
- habilidades automáticas;
- múltiplos atos;
- dificuldades superiores;
- mercadores, eventos, melhorias e serviços;
- novos tipos e espaços de equipamento.

### Fora do escopo

- inventário manual;
- compra e venda;
- uso prático do ouro;
- habilidades ativas;
- árvore de talentos;
- atributos secundários ativos;
- eventos aleatórios;
- progressão offline;
- multiplayer.

O ouro já é obtido e salvo na v0.1, mesmo sem possuir um gasto disponível.

---

## 6. Loop Principal

1. O jogo apresenta dificuldade, ato, mapa e progresso.
2. Um inimigo do mapa aparece.
3. A estratégia escolhida modifica Ataque e Defesa do herói.
4. O combate acontece automaticamente.
5. A vitória concede experiência, ouro e uma chance de loot.
6. O melhor item encontrado é equipado automaticamente.
7. A vitória avança o mapa.
8. A meta do mapa libera a etapa seguinte.
9. O Mapa 10 termina com o chefe do ato.
10. A derrota faz o herói renascer e repetir o encontro atual.

### Ciclo emocional

**Observar → decidir → vencer → receber → melhorar → avançar → superar**

---

## 7. Estratégias de Combate

Estratégias são a principal forma de agência da v0.1. Elas permitem que o jogador
adapte o herói sem controlar ataques ou interromper o fluxo idle.

### 7.1 Opções

| Estratégia | Ataque | Defesa | Uso esperado |
|---|---:|---:|---|
| Agressivo | +20% | -20% | Acelerar encontros que o herói já suporta |
| Balanceado | Sem alteração | Sem alteração | Opção padrão e previsível |
| Defensivo | -20% | +20% | Sobreviver a inimigos ou chefes perigosos |

### 7.2 Regras

- Balanceado é a estratégia inicial.
- A escolha permanece ativa entre combates, mapas e sessões.
- A estratégia pode ser alterada a qualquer momento.
- A troca não pausa nem reinicia o combate.
- O novo modificador passa a valer no próximo ataque aplicável.
- A estratégia não possui custo, recarga ou duração.
- Os valores finais devem respeitar um mínimo de 1 para Ataque e Defesa.

### 7.3 Cálculo conceitual

1. Calcular os atributos totais do herói com nível e equipamento.
2. Aplicar o modificador da estratégia.
3. Usar os valores resultantes no combate.

Exemplo:

`Ataque efetivo = Ataque total × modificador da estratégia`

O arredondamento deve ser consistente. A referência inicial é arredondar para o
inteiro mais próximo após a aplicação do modificador.

### 7.4 Integração com classes

Todas as classes futuras usam as mesmas três estratégias. Os modificadores são
aplicados depois dos atributos e bônus da classe, evitando regras exclusivas.

Uma classe pode se beneficiar mais de determinada postura, mas nenhuma estratégia
deve ser bloqueada.

### 7.5 Interface

A troca deve ocupar um controle compacto, como três botões ou um seletor:

`Agressivo | Balanceado | Defensivo`

A estratégia ativa precisa estar visível sem abrir menus.

### 7.6 Objetivo de design

A escolha deve responder a situações claras:

- “Quero derrotar inimigos fáceis mais rápido.”
- “Quero um comportamento neutro.”
- “Preciso sobreviver ao chefe.”

Ela não pretende formar um sistema tático complexo.

---

## 8. Herói e Progressão de Poder

### Atributos primários

| Atributo | Função |
|---|---|
| Nível | Crescimento permanente |
| Experiência | Progresso para o próximo nível |
| Vida Máxima | Resistência total |
| Ataque | Dano base |
| Defesa | Redução de dano |

### Valores iniciais

| Atributo | Valor |
|---|---:|
| Nível | 1 |
| Experiência | 0 |
| Vida Máxima | 100 |
| Ataque | 10 |
| Defesa | 5 |

### Crescimento por nível

- Vida Máxima: +20.
- Ataque: +3.
- Defesa: +2.
- Vida restaurada ao novo máximo.

### Experiência necessária

`Experiência necessária = nível atual × 100`

O nível fortalece o herói. A campanha determina o desafio e evita que inimigos se
ajustem completamente ao poder atual.

---

## 9. Classes - V0.2

Na v0.1, o herói utiliza a classe neutra **Aventureiro**.

| Classe futura | Identidade inicial |
|---|---|
| Guerreiro | Vida e Defesa |
| Arqueiro | Velocidade e precisão |
| Mago | Dano elevado |
| Curandeiro | Cura e sustentação |

A identidade de classe deve ser separada de:

- nível;
- equipamento;
- estratégia;
- progressão da campanha.

As classes futuramente poderão alterar atributos iniciais, crescimento,
estatísticas secundárias e habilidades automáticas. As três estratégias de
combate continuam disponíveis para todas.

A primeira implementação de classes deve usar diferenças passivas simples. Não
haverá árvore de talentos na v0.2.

---

## 10. Estatísticas Secundárias - Preparação Futura

As estatísticas secundárias ampliam a diversidade de classes e itens, mas não
ficam ativas na v0.1.

| Estatística | Função futura |
|---|---|
| Velocidade de Ataque | Reduz o intervalo entre ataques |
| Chance Crítica | Probabilidade de causar dano ampliado |
| Precisão | Probabilidade de acertar ataques |
| Esquiva | Probabilidade de evitar dano |
| Regeneração | Recuperação periódica de vida |

### Princípios

- atributos ausentes equivalem a zero, salvo Precisão quando for ativada;
- itens podem armazenar uma coleção opcional de bônus secundários;
- classes podem fornecer valores básicos;
- estratégias não modificam estatísticas secundárias na primeira integração;
- o painel principal não deve exibir todas permanentemente;
- nenhuma delas é necessária para calcular o combate da v0.1.

Quando ativadas, devem entrar gradualmente. Não é necessário liberar as cinco ao
mesmo tempo.

---

## 11. Inimigos, Mapas e Chefes

### Inimigos iniciais

- **Goblin:** perfil equilibrado.
- **Lobo:** menos vida e mais ataque.
- **Esqueleto:** mais vida e menos ataque.

O poder do inimigo considera mapa, ato e dificuldade. O nível do herói pode
participar de limites de segurança, mas não deve escalar o encontro de forma
total, pois o jogador precisa sentir que ficou mais forte.

### Ato I - Fronteira Esquecida

| Mapa | Nome | Inimigos |
|---:|---|---|
| 1 | Estrada Abandonada | Goblins |
| 2 | Bosque dos Sussurros | Lobos |
| 3 | Acampamento Saqueado | Goblins e Lobos |
| 4 | Colinas Cinzentas | Lobos |
| 5 | Cemitério da Vigília | Esqueletos |
| 6 | Ponte Quebrada | Goblins |
| 7 | Ruínas do Posto Norte | Esqueletos e Goblins |
| 8 | Trilha da Névoa | Lobos e Esqueletos |
| 9 | Portões da Fortaleza | Todos |
| 10 | Fortaleza Esquecida | Chefe |

### Chefe do Ato I

**Capitão Ossonegro:** antigo comandante reanimado pela corrupção.

O chefe possui mais vida, concede experiência e ouro superiores e usa uma chance
melhor de loot. Ele deve ser derrotado para concluir o ato.

Na v0.1, não precisa possuir habilidades especiais.

---

## 12. Economia - Ouro

Ouro é o recurso econômico permanente do TBH2.

### 12.1 Obtenção

- todo inimigo derrotado concede ouro;
- mapas avançados concedem valores maiores;
- chefes concedem uma recompensa superior;
- dificuldades futuras aplicam multiplicadores;
- eventos poderão conceder ou consumir ouro.

### 12.2 Escala conceitual

`Ouro recebido = valor base do inimigo × mapa × ato × dificuldade`

A fórmula representa os fatores necessários, não números finais. O nível do herói
não deve aumentar diretamente o ouro de um mesmo encontro para evitar exploração
por permanência em mapas fáceis.

### 12.3 Regras da v0.1

- ouro é obtido automaticamente;
- o saldo é persistente;
- ouro não ocupa espaço;
- não existe limite inicial;
- nenhuma compra é necessária;
- a interface exibe o saldo e o ganho recente;
- não há perda de ouro por morte.

### 12.4 Usos futuros

Ouro será preparado para:

- mercadores;
- eventos aleatórios;
- melhorias;
- serviços.

Exemplos de serviços futuros incluem substituir uma oferta, recuperar o herói ou
realizar uma melhoria simples. Nenhum uso será implementado antes de existir uma
decisão econômica clara.

### 12.5 Princípios econômicos

- o ouro deve ter uma única unidade, sem moedas paralelas no MVP;
- fontes e gastos precisam crescer em escalas compatíveis;
- preços futuros devem considerar dificuldade e progresso;
- acumular ouro na v0.1 não pode bloquear a evolução posterior;
- a economia não deve exigir cliques frequentes.

Como o ouro ainda não possui gasto, seus valores na v0.1 são provisórios e podem
ser normalizados antes da introdução dos mercadores.

---

## 13. Loot Escalável

O loot não será uma lista de recompensas com bônus fixos. Cada equipamento será
uma instância gerada a partir de uma base e de um valor de Poder.

### 13.1 Estrutura de um item

Cada item contém:

- identificador único;
- item base;
- espaço de equipamento;
- raridade;
- nível do item;
- Poder;
- bônus primário;
- bônus secundários opcionais futuros;
- origem: mapa, ato, dificuldade e inimigo;
- nível de aprimoramento visual opcional.

### 13.2 Item base

O item base define:

- nome;
- espaço;
- atributo principal;
- identidade visual;
- faixa básica de poder.

Exemplos:

| Item base | Espaço | Atributo principal |
|---|---|---|
| Espada Enferrujada | Arma | Ataque |
| Machado do Caçador | Arma | Ataque |
| Lâmina Carmesim | Arma | Ataque |
| Escudo de Madeira | Defesa | Defesa |
| Armadura de Couro | Defesa | Defesa |
| Armadura do Guardião | Defesa | Defesa |

Os nomes existentes tornam-se famílias de item, não recompensas de força única.

### 13.3 Poder

Poder é a medida resumida da qualidade de um item. Ele permite comparação rápida
e equipamento automático.

Exemplos:

- `Espada Enferrujada [Poder 12]`
- `Espada Enferrujada [Poder 18]`
- `Espada Enferrujada [Poder 25]`

A apresentação `+1`, `+2` e `+3` pode existir visualmente no futuro, mas não deve
substituir o Poder interno, pois diferentes dificuldades exigem uma escala maior.

### 13.4 Geração de Poder

O Poder potencial considera:

1. valor base do tipo de item;
2. mapa;
3. ato;
4. dificuldade;
5. nível de referência;
6. raridade;
7. pequena variação aleatória.

Modelo conceitual:

`Poder = base + mapa + ato + dificuldade + nível + raridade + variação`

Os pesos serão definidos por balanceamento. A variação deve ser limitada para que
um mapa inicial não produza itens superiores ao conteúdo muito avançado.

### 13.5 Relação com nível

O nível usado na geração deve ser limitado pela faixa do mapa. Isso permite que o
loot acompanhe o herói sem transformar mapas antigos na melhor fonte de itens.

Conceito:

`nível de referência = menor valor entre nível do herói e limite do mapa`

### 13.6 Raridade

| Raridade | Chance básica | Função |
|---|---:|---|
| Comum | 20% | Progressão frequente |
| Raro | 8% | Salto perceptível |
| Épico | 2% | Recompensa excepcional |
| Nenhum item | 70% | Preserva expectativa |

A raridade aumenta o potencial de Poder e, futuramente, a quantidade ou qualidade
de estatísticas secundárias.

### 13.7 Conversão de Poder em atributos

O Poder não concede bônus por si só. O item base converte Poder em seu atributo
principal.

Exemplos:

- armas convertem Poder em Ataque;
- armaduras e escudos convertem Poder em Defesa.

As taxas de conversão podem variar por família, mas itens do mesmo espaço devem
ser comparáveis.

### 13.8 Equipamento automático

Na v0.1:

- o item encontrado é comparado ao item equipado no mesmo espaço;
- maior Poder é equipado;
- menor Poder é descartado;
- em empate, vence o maior bônus primário;
- persistindo o empate, o item atual é mantido;
- não existe inventário.

A interface deve informar:

`Espada Enferrujada, Poder 18: equipada (+3 Poder)`

### 13.9 Escalabilidade

Esse modelo permite que o mesmo item base continue aparecendo com força adequada
em novos mapas, atos e dificuldades. Novos itens base ampliam variedade visual e
temática, sem serem necessários para sustentar numericamente a progressão.

### 13.10 Proteções de balanceamento

- limites mínimos e máximos por mapa;
- chefes com piso de Poder superior;
- variação aleatória controlada;
- mapas antigos limitados por sua faixa;
- dificuldade como multiplicador relevante;
- registro da origem para ajustes e testes.

---

## 14. Habilidades Automáticas - V0.3

Habilidades reforçarão a identidade das classes sem criar uma barra manual.

### Princípios

- ativação totalmente automática;
- nenhuma habilidade exige clique;
- condições e recargas simples;
- feedback visual curto;
- compatibilidade com todas as estratégias;
- quantidade pequena por classe;
- combate compreensível sem acompanhar cada ativação.

### Exemplos

| Classe | Habilidade | Comportamento conceitual |
|---|---|---|
| Guerreiro | Golpe Poderoso | Ataque mais forte após certo número de golpes |
| Arqueiro | Tiro Preciso | Ataque periódico com maior precisão ou crítico |
| Mago | Explosão Arcana | Grande dano após uma recarga |
| Curandeiro | Prece de Cura | Recupera vida automaticamente quando necessário |

### Integração

A estratégia modifica os atributos usados pela habilidade quando aplicável, mas
não muda sua lógica de ativação.

Na primeira implementação, cada classe deve possuir no máximo uma habilidade
característica. Não haverá árvore de talentos, barra de mana complexa ou rotação
manual.

Eventos aleatórios e habilidades pertencem à v0.3, mas são sistemas separados.

---

## 15. Motivação e Retenção

### Curto prazo

- vencer o combate;
- receber ouro;
- aumentar o progresso do mapa;
- encontrar um item de Poder maior;
- testar outra estratégia.

### Médio prazo

- concluir o mapa;
- obter o primeiro item raro;
- aumentar o saldo de ouro;
- alcançar o chefe;
- ajustar a estratégia para derrotá-lo.

### Longo prazo

- concluir o ato;
- concluir dificuldades;
- formar uma classe;
- buscar itens de Poder superior;
- desbloquear novos conteúdos.

### Marcos

| Marco | Apresentação |
|---|---|
| Primeiro item raro | Destaque e registro permanente |
| Primeiro chefe derrotado | Mensagem de conquista |
| Primeiro ato concluído | Painel de conclusão |
| Primeira dificuldade concluída | Marco persistente |
| Primeiro saldo relevante de ouro | Futuro, quando houver gastos |

Retenção deve vir da clareza do próximo objetivo, não de punições por ausência.

---

## 16. Interface de Taskbar

### Formato

Janela aproximada de 300 × 500 pixels.

### Prioridade visual

1. dificuldade, ato e mapa;
2. progresso do mapa;
3. herói e inimigo;
4. barras de vida;
5. estratégia ativa;
6. experiência;
7. ouro;
8. loot e eventos recentes;
9. equipamento.

### Estratégia

O seletor permanece disponível no painel principal. A troca não abre uma janela
separada.

### Ouro

O saldo usa uma linha ou ícone compacto. Ganhos recentes podem aparecer no log:

`Goblin derrotado: +7 XP, +3 Ouro`

### Itens

O equipamento mostra nome, raridade, Poder e bônus principal. Detalhes futuros
ficam em tooltip ou painel secundário, evitando poluição visual.

### Chefes e marcos

Chefes recebem barra diferenciada. Conclusões e itens raros recebem destaque
temporário, sem interromper o combate.

---

## 17. Persistência e Modelo Conceitual

### Herói

- nome;
- classe;
- nível e experiência;
- atributos primários;
- estatísticas secundárias opcionais;
- estratégia ativa;
- ouro;
- equipamentos;
- habilidades futuras;
- estatísticas gerais.

### Item

- identificador;
- base;
- espaço;
- raridade;
- Poder;
- nível do item;
- bônus primário;
- bônus secundários;
- origem.

### Campanha

- dificuldade;
- ato;
- mapa;
- progresso do mapa;
- desbloqueios;
- chefes derrotados;
- marcos.

### Compatibilidade futura

Novos campos devem possuir valores padrão. Saves antigos não podem depender da
existência de estatísticas secundárias ou habilidades.

O ouro e a estratégia devem ser persistidos desde a v0.1.

---

## 18. Balanceamento

### Estratégias

- Agressivo precisa acelerar vitórias, mas aumentar risco.
- Defensivo precisa melhorar sobrevivência, mas prolongar a batalha.
- Balanceado não pode parecer uma escolha incorreta.
- nenhuma postura deve dominar todos os conteúdos.

### Ouro

- inimigos comuns fornecem ganhos pequenos e frequentes;
- chefes fornecem ganhos reconhecíveis;
- mapas antigos não devem ser a melhor fonte permanente;
- valores iniciais podem ser reajustados antes de existirem gastos.

### Loot

- melhorias pequenas devem continuar possíveis;
- raridade e Poder precisam ser relacionados, mas não idênticos;
- um raro deve normalmente superar um comum da mesma faixa;
- um item de mapa muito avançado pode superar uma raridade maior antiga;
- chefes devem ter piso de recompensa, não garantia do melhor item.

### Ritmo

- primeira vitória em menos de um minuto;
- primeiro mapa em uma sessão curta;
- primeiro item comum cedo;
- primeiro item raro como marco;
- chefe alcançável após progressão perceptível;
- estratégia útil durante a preparação e tentativa do chefe.

---

## 19. Riscos e Controles

### Estratégia dominante

Se Agressivo sempre vencer mais rápido sem risco real, as outras opções perdem
valor. Os chefes e mapas avançados devem exigir sobrevivência suficiente.

### Ouro sem uso

Acumular uma moeda sem função pode parecer vazio. A interface deve tratá-la como
recurso em preparação, sem conceder destaque excessivo na v0.1.

### Inflação futura

Ouro e Poder podem crescer além de escalas legíveis. Formatação abreviada e
curvas controladas serão necessárias em dificuldades avançadas.

### Loot sem identidade

Variações numéricas não substituem novas famílias visuais. O Poder sustenta a
escala, mas novos atos ainda devem introduzir itens temáticos.

### Excesso de atributos

As cinco estatísticas secundárias são um limite de direção, não uma obrigação de
lançamento conjunto.

### Interface sobrecarregada

Estratégia, ouro e Poder precisam usar componentes compactos. Informações
detalhadas devem permanecer fora do painel principal.

---

## 20. Roadmap

### V0.1 - Núcleo com agência e economia

- Ato I e 10 mapas;
- chefe do ato;
- dificuldade Normal;
- estratégias de combate;
- ouro acumulável;
- loot gerado por base e Poder;
- equipamento automático;
- persistência completa.

### V0.2 - Classes

- Guerreiro, Arqueiro, Mago e Curandeiro;
- diferenças passivas;
- preparação gradual de estatísticas secundárias;
- novos itens base.

### V0.3 - Habilidades e eventos

- uma habilidade automática por classe;
- Mercador viajante;
- Baú abandonado;
- Emboscada;
- Altar misterioso;
- Portal demoníaco;
- primeiros usos práticos de ouro.

### V0.4 - Identidade Exclusiva de Taskbar

- tempo de sessão;
- dias consecutivos sem punição;
- moral do aventureiro;
- eventos por horário;
- bônus limitados por presença.

Cada versão depende da validação da anterior.

---

## 21. Critérios de Sucesso da V0.1

- o jogador entende o avanço de mapa;
- a próxima meta está sempre clara;
- as estratégias produzem diferenças perceptíveis;
- trocar de estratégia é simples e não interrompe o combate;
- ouro é recebido e preservado corretamente;
- itens continuam podendo melhorar ao longo dos mapas;
- Poder torna a comparação compreensível;
- equipamento automático não exige inventário;
- o chefe funciona como teste de crescimento e estratégia;
- a janela permanece legível e discreta.

### Perguntas para teste

- Você entendeu o efeito das três estratégias?
- Em qual situação decidiu trocar de estratégia?
- O ouro pareceu uma recompensa relevante mesmo sem uso imediato?
- Ficou claro por que um item era melhor?
- O Poder facilitou a comparação?
- Você sentiu expectativa por uma melhoria de equipamento?
- O chefe incentivou mudança de estratégia ou busca por mais poder?
- A interface continuou confortável ao lado de outras aplicações?

---

## 22. Resumo da Experiência

TBH2 apresenta uma campanha automática organizada em mapas, atos e dificuldades.
O herói luta sozinho, mas o jogador escolhe uma estratégia persistente que altera
seu equilíbrio entre Ataque e Defesa.

Cada vitória concede experiência e ouro, além da possibilidade de encontrar uma
nova instância de equipamento. Itens são formados por uma base temática e um
Poder escalável conforme mapa, ato, dificuldade e nível de referência. Isso
mantém o loot relevante sem exigir um inventário complexo.

A v0.1 continua sendo um MVP: um herói genérico, um ato, três inimigos, um chefe,
três estratégias, uma moeda acumulável e equipamento automático. Estatísticas
secundárias, classes completas, habilidades e usos econômicos permanecem
preparados para expansões posteriores.

O resultado mantém a natureza idle do projeto e acrescenta três fundamentos para
sua longevidade: escolha ocasional, economia persistente e loot sustentável.

