# TBH2 - TaskBar Hero 2

## Game Design Document Refinado

**Versão do documento:** 0.2  
**Versão-alvo inicial do jogo:** 0.1  
**Gênero:** Idle RPG de fantasia sombria  
**Plataforma:** Windows  
**Formato:** Taskbar Companion em janela lateral compacta  
**Referências:** Diablo, Warcraft, Dota, Dungeons & Dragons e Melvor Idle

---

## 1. Visão do Jogo

TBH2 é um Idle RPG que vive na lateral da área de trabalho. Enquanto o jogador
trabalha, estuda, conversa ou utiliza outras aplicações, um herói percorre mapas,
enfrenta inimigos, encontra equipamentos e avança por uma campanha persistente.

O jogo deve parecer uma pequena aventura em andamento, e não apenas um contador
de números. Sempre que olhar para a janela, o jogador deve entender:

- onde o herói está;
- contra quem está lutando;
- qual é a próxima meta;
- o que mudou desde a última vez que observou.

TBH2 não exige atenção contínua. Seu valor está em oferecer companhia, progresso
visível e momentos breves de recompensa ao longo do uso normal do computador.

### Frase de apresentação

> Um herói enfrenta uma campanha contínua na lateral da sua tela, evoluindo
> enquanto você faz outras coisas.

---

## 2. Fantasia Central

O jogador acompanha um aventureiro solitário que percorre terras corrompidas em
busca da origem de uma ameaça crescente. O herói age por conta própria, mas sua
jornada é moldada pelo poder acumulado, pelos equipamentos encontrados e, em
versões futuras, por sua classe e especialização.

A fantasia de progressão é passar de um viajante com equipamento improvisado a
um campeão capaz de derrotar chefes, concluir atos e retornar à campanha em
dificuldades cada vez mais perigosas.

O herói deve ser percebido como um companheiro persistente. Sua evolução continua
entre pequenas consultas do jogador e permanece registrada entre sessões.

---

## 3. Proposta de Valor

TBH2 combina:

- progressão constante de jogos idle;
- loot e crescimento de poder de RPGs de ação;
- campanha organizada em mapas, atos e dificuldades;
- leitura rápida em uma janela estreita;
- presença discreta durante o uso do computador.

Seu diferencial não é somente o combate automático. É a união entre uma campanha
de RPG compreensível e o papel de companheiro da área de trabalho.

---

## 4. Pilares de Design

### 4.1 Progresso com destino

O nível do herói continua importante, mas deixa de ser o único indicador de
avanço. Cada combate contribui para concluir um mapa, cada mapa aproxima o herói
do chefe e cada chefe abre uma nova etapa da campanha.

### 4.2 Presença discreta

O jogo deve permanecer aberto sem competir com a atividade principal do usuário.
Informações essenciais precisam ser entendidas de relance.

### 4.3 Combate automático legível

Ataques, dano, vida, vitória e derrota devem ser claros mesmo para quem observa
apenas por alguns segundos.

### 4.4 Recompensas com expectativa

Experiência garante crescimento previsível. Loot cria surpresa. Chefes e
conclusões de mapa criam momentos de conquista.

### 4.5 Metas em várias escalas

O jogador sempre deve ter uma meta próxima, uma meta de sessão e uma meta de
longo prazo.

### 4.6 Baixa punição

A derrota indica falta de poder, mas não remove progresso permanente. O herói
renasce e tenta novamente.

### 4.7 Expansão em camadas

Novos sistemas devem complementar o loop existente. Classes, eventos e recursos
de Taskbar serão adicionados gradualmente, sem tornar a experiência básica
dependente deles.

---

## 5. Estrutura de Progressão

A progressão geral segue três camadas:

**Mapa → Ato → Dificuldade**

O nível do herói permanece como progressão de poder, mas a campanha passa a
fornecer direção e objetivos.

### 5.1 Mapas

Cada ato possui 10 mapas sequenciais.

Um mapa representa uma etapa curta da jornada, com:

- nome e temática próprios;
- conjunto específico de inimigos;
- faixa de poder;
- quantidade definida de encontros;
- indicador de progresso;
- recompensa de conclusão.

Na estrutura inicial, um mapa é concluído após o herói vencer uma quantidade
determinada de inimigos. A referência inicial é **10 vitórias por mapa**, sujeita
a testes de ritmo.

Ao concluir o mapa:

- o progresso é salvo;
- o próximo mapa é desbloqueado;
- o jogador recebe uma mensagem de conquista;
- o herói avança automaticamente.

O jogador não precisa escolher manualmente cada mapa durante o fluxo normal.

### 5.2 Atos

Um ato reúne 10 mapas conectados por uma mesma região, ameaça e identidade
visual. Os nove primeiros mapas desenvolvem a região. O décimo culmina no chefe
do ato.

Estrutura planejada da campanha:

| Ato | Região | Tema |
|---|---|---|
| Ato I | Fronteira Esquecida | Estradas abandonadas, bosques e ruínas |
| Ato II | Terras da Cinza | Campos queimados, fortalezas e cultistas |
| Ato III | Abismo Carmesim | Corrupção demoníaca e origem da invasão |

Os nomes e conteúdos dos Atos II e III são direcionais e podem ser refinados
durante a produção.

### 5.3 Dificuldades

Após concluir todos os atos de uma dificuldade, o jogador desbloqueia a seguinte:

1. Normal
2. Veterano
3. Pesadelo
4. Infernal
5. Mítico

Cada nova dificuldade reinicia a progressão de mapas no Ato I, mas preserva:

- nível;
- experiência;
- equipamentos;
- estatísticas;
- marcos conquistados;
- dificuldades desbloqueadas.

A nova campanha apresenta inimigos mais fortes e recompensas melhores.

### 5.4 Função de cada camada

| Camada | Horizonte | Pergunta respondida |
|---|---|---|
| Combate | Segundos | Vou vencer este inimigo? |
| Mapa | Minutos | Quanto falta para avançar? |
| Ato | Sessões | Estou pronto para o chefe? |
| Dificuldade | Longo prazo | Até onde meu herói consegue chegar? |

---

## 6. Escopo Controlado da Versão 0.1

A v0.1 deve validar uma fatia vertical da campanha, não produzir todo o conteúdo
planejado.

### Incluído na v0.1

- um herói genérico persistente;
- combate automático;
- experiência e níveis;
- loot e equipamento automático;
- dificuldade Normal;
- Ato I completo;
- 10 mapas do Ato I;
- um chefe no final do ato;
- progresso por vitórias em cada mapa;
- marcos essenciais;
- interface lateral;
- salvamento e carregamento.

### Preparado, mas não necessariamente disponível na v0.1

- cadastro de múltiplos atos;
- modificadores de dificuldade;
- identidade de classe do herói;
- tipos especiais de encontro;
- novos espaços de equipamento;
- conteúdos desbloqueáveis.

### Fora do escopo da v0.1

- Atos II e III jogáveis;
- dificuldades acima de Normal;
- classes selecionáveis;
- habilidades;
- inventário manual;
- moedas e loja;
- eventos aleatórios;
- progressão offline;
- sistemas baseados no uso do computador;
- multiplayer e serviços online.

Essa divisão permite testar o ciclo completo de mapa e chefe sem exigir a
produção antecipada de toda a campanha.

---

## 7. Experiência da Versão Inicial

### Primeiros minutos

O jogador abre o jogo e encontra o herói no primeiro mapa da Fronteira
Esquecida. O combate começa automaticamente.

Nesse período, o jogador deve:

- compreender que o combate é automático;
- identificar o mapa atual;
- ver o contador de progresso avançar;
- receber experiência;
- entender que a morte não remove progresso permanente;
- antecipar o primeiro item.

### Primeira sessão

O jogador deve concluir pelo menos um mapa, alcançar um nível e observar uma
mudança de cenário ou conjunto de inimigos. O objetivo visível passa a ser chegar
ao Mapa 10 e enfrentar o chefe.

### Sessões seguintes

Ao retornar, o jogador encontra o herói no mapa alcançado anteriormente. A
retenção vem da combinação entre:

- proximidade do próximo mapa;
- possibilidade de encontrar equipamento melhor;
- preparação para o chefe;
- conclusão futura do ato.

---

## 8. Loop Principal

1. O jogo apresenta o mapa atual e seu progresso.
2. Um inimigo pertencente ao mapa aparece.
3. Herói e inimigo trocam ataques automaticamente.
4. Ao vencer, o herói recebe experiência e pode encontrar loot.
5. A vitória avança o progresso do mapa.
6. Ao completar a meta de vitórias, o próximo mapa é liberado.
7. No Mapa 10, o herói enfrenta o chefe do ato.
8. Ao derrotar o chefe, o ato é concluído.
9. O próximo ato ou dificuldade é desbloqueado quando houver conteúdo disponível.
10. Em caso de derrota, o herói renasce e repete o encontro atual.

### Ciclo emocional

**Observar → vencer → receber → avançar → preparar → superar**

O ciclo deve alternar recompensas pequenas e frequentes com marcos maiores e
menos frequentes.

---

## 9. Mapas do Ato I

### Ato I - Fronteira Esquecida

As antigas rotas do reino foram abandonadas após o desaparecimento da guarda da
fronteira. Goblins ocupam os caminhos, lobos caçam nos bosques e mortos se
levantam próximos às ruínas.

| Mapa | Nome | Temática | Inimigos predominantes |
|---:|---|---|---|
| 1 | Estrada Abandonada | Entrada da fronteira | Goblins |
| 2 | Bosque dos Sussurros | Mata fechada | Lobos |
| 3 | Acampamento Saqueado | Restos de viajantes | Goblins e Lobos |
| 4 | Colinas Cinzentas | Trilhas expostas | Lobos |
| 5 | Cemitério da Vigília | Túmulos antigos | Esqueletos |
| 6 | Ponte Quebrada | Passagem disputada | Goblins |
| 7 | Ruínas do Posto Norte | Fortificação caída | Esqueletos e Goblins |
| 8 | Trilha da Névoa | Caminho corrompido | Lobos e Esqueletos |
| 9 | Portões da Fortaleza | Entrada do reduto inimigo | Todos |
| 10 | Fortaleza Esquecida | Arena do chefe | Guarda do chefe e chefe |

Os mapas reutilizam os três inimigos iniciais em combinações diferentes. A
variedade da v0.1 vem da distribuição, do escalonamento e da ambientação, evitando
a criação de uma lista extensa de criaturas antes da validação do MVP.

---

## 10. Chefes

Chefes encerram atos e funcionam como testes de poder.

### Funções

- estabelecer uma meta clara;
- validar o crescimento do herói;
- criar um momento memorável;
- bloquear avanço prematuro;
- oferecer recompensa superior.

### Regras

- cada ato possui um chefe no Mapa 10;
- o chefe precisa ser derrotado para concluir o ato;
- perder não remove o progresso anterior;
- após a derrota, o herói renasce e tenta novamente;
- o chefe possui mais vida e ataque que inimigos comuns;
- a recompensa inclui experiência ampliada e chance melhor de loot.

### Chefe do Ato I: Capitão Ossonegro

Antigo comandante da fronteira, reanimado pela corrupção que tomou a fortaleza.

**Perfil de combate:** alta vida, ataque moderado e batalha mais longa que um
encontro comum.

O chefe não precisa ter habilidades especiais na v0.1. Uma barra de vida
diferenciada, nome próprio, retrato e ritmo mais longo já devem comunicar sua
importância.

### Escalonamento futuro

Chefes de dificuldades superiores podem receber atributos maiores e, em versões
posteriores, modificadores ou habilidades simples. Essas variações não fazem
parte do MVP.

---

## 11. Sistema de Dificuldade

As dificuldades prolongam a campanha sem exigir uma nova estrutura de mapas para
cada ciclo.

### Filosofia

Cada dificuldade representa uma nova volta pela campanha em um mundo mais
perigoso. O jogador retorna ao início com todo o poder conquistado e encontra
inimigos capazes de desafiar esse crescimento.

### Escala conceitual

| Dificuldade | Papel | Inimigos | Experiência | Loot |
|---|---|---|---|---|
| Normal | Apresentação da campanha | Base | Base | Base |
| Veterano | Primeiro teste de build | Aumentados | Melhorada | Melhorado |
| Pesadelo | Progressão avançada | Fortes | Alta | Maior chance de raridade |
| Infernal | Endgame inicial | Muito fortes | Muito alta | Recompensas superiores |
| Mítico | Desafio máximo planejado | Extremos | Máxima | Melhor tabela disponível |

Multiplicadores exatos serão definidos por testes. O GDD evita números prematuros
que possam comprometer o balanceamento antes de existir conteúdo suficiente.

### Regras de desbloqueio

- Normal está disponível desde o início.
- Veterano exige concluir todos os atos no Normal.
- Pesadelo exige concluir todos os atos no Veterano.
- Infernal exige concluir todos os atos no Pesadelo.
- Mítico exige concluir todos os atos no Infernal.

### Conteúdo futuro

Uma dificuldade pode futuramente desbloquear:

- novos itens;
- variações de inimigos;
- eventos;
- chefes aprimorados;
- materiais ou sistemas de progressão ainda não definidos.

Esses desbloqueios são possibilidades de expansão, não compromissos da v0.1.

---

## 12. Herói e Progressão de Poder

Na v0.1, o jogador utiliza um aventureiro generalista.

### Atributos

| Atributo | Função |
|---|---|
| Nível | Crescimento permanente do herói |
| Experiência | Progresso para o próximo nível |
| Vida Máxima | Resistência total |
| Ataque | Dano base causado |
| Defesa | Redução do dano recebido |

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

Essa fórmula permanece simples na v0.1. O avanço por nível fortalece o herói,
enquanto mapas e atos mostram onde esse poder está sendo aplicado.

---

## 13. Classes - Integração Planejada para a V0.2

A arquitetura conceitual do herói deve separar:

- atributos básicos;
- progressão de nível;
- identidade de classe;
- modificadores de classe;
- habilidades futuras.

Na v0.1, o campo de classe pode assumir o valor **Aventureiro**, sem alterar o
combate.

### Classes planejadas

| Classe | Identidade | Tendência futura |
|---|---|---|
| Guerreiro | Resistência e força física | Mais Vida e Defesa |
| Arqueiro | Velocidade e precisão | Ataques rápidos e crítico |
| Mago | Poder arcano | Alto dano e baixa resistência |
| Curandeiro | Sustentação | Cura e sobrevivência |

### Limites da v0.2

A primeira integração de classes deve começar com diferenças passivas e fáceis
de compreender. Árvores extensas, dezenas de habilidades e combinações complexas
não são necessárias para provar o sistema.

### Pontos de integração

As classes futuramente afetarão:

- atributos iniciais;
- crescimento por nível;
- identidade visual;
- equipamentos preferenciais;
- habilidades automáticas;
- desempenho contra diferentes desafios.

Mapas, atos, chefes e dificuldades devem funcionar independentemente da classe
escolhida.

---

## 14. Inimigos e Escalonamento

### Inimigos comuns da v0.1

#### Goblin

Perfil equilibrado. Funciona como referência básica de combate.

#### Lobo

Menos vida e mais ataque. Produz encontros curtos e perigosos.

#### Esqueleto

Mais vida e menos ataque. Produz encontros longos e estáveis.

### Fonte do escalonamento

O poder do inimigo deve considerar:

1. mapa atual;
2. ato atual;
3. dificuldade;
4. variação limitada em torno do poder esperado.

O mapa passa a ser a principal referência de desafio. O nível do herói não deve
ajustar totalmente o inimigo, pois isso eliminaria a sensação de ficar mais forte
para superar uma barreira.

### Princípio de balanceamento

Se o jogador estiver fraco, ele pode permanecer no encontro atual, acumular
experiência e obter loot até conseguir avançar. O jogo não exige seleção manual
de uma área de treinamento na v0.1.

---

## 15. Combate Automático

### Sequência

1. O herói ataca.
2. O inimigo perde vida.
3. Se sobreviver, o inimigo contra-ataca.
4. A Defesa reduz o dano recebido.
5. O processo continua até a derrota de um participante.

Todo ataque deve causar pelo menos 1 ponto de dano.

### Vitória comum

- concede experiência;
- pode conceder loot;
- aumenta o progresso do mapa;
- gera um novo inimigo.

### Derrota

- aumenta a estatística de mortes;
- não remove nível, experiência, loot ou progresso já consolidado;
- restaura a vida do herói;
- reinicia o encontro atual.

### Ritmo

A referência inicial é aproximadamente um ataque por segundo. Chefes podem ter
combates mais longos, mas não devem paralisar o loop por períodos frustrantes.

---

## 16. Loot e Equipamentos

### Probabilidades básicas

| Resultado | Chance |
|---|---:|
| Nenhum item | 70% |
| Comum | 20% |
| Raro | 8% |
| Épico | 2% |

Chefes podem usar uma tabela com chance de item superior, definida durante o
balanceamento.

### Equipamentos da v0.1

| Item | Raridade | Espaço | Bônus |
|---|---|---|---:|
| Espada Enferrujada | Comum | Arma | +2 Ataque |
| Escudo de Madeira | Comum | Defesa | +1 Defesa |
| Machado do Caçador | Raro | Arma | +5 Ataque |
| Armadura de Couro | Raro | Defesa | +4 Defesa |
| Lâmina Carmesim | Épico | Arma | +10 Ataque |
| Armadura do Guardião | Épico | Defesa | +8 Defesa |

### Equipamento automático

- itens melhores substituem automaticamente os atuais;
- itens iguais ou inferiores são descartados;
- não existe inventário na v0.1;
- a comparação ocorre apenas entre itens do mesmo espaço.

Esse sistema preserva a natureza idle e evita gerenciamento prematuro.

### Dificuldade e loot

Dificuldades superiores devem melhorar a recompensa sem tornar inútil todo item
anterior de forma imediata. A progressão pode usar aumento de chance, versões
mais poderosas ou novos itens, conforme definido em versões futuras.

---

## 17. Motivação e Retenção

A retenção deve nascer de metas visíveis, não de punições ou obrigações diárias
na versão inicial.

### Metas de curto prazo

- vencer o inimigo atual;
- completar a próxima vitória do mapa;
- alcançar o próximo nível;
- encontrar um item melhor;
- concluir o mapa atual.

### Metas de médio prazo

- encontrar o primeiro item raro;
- chegar ao Mapa 10;
- derrotar o primeiro chefe;
- concluir o primeiro ato.

### Metas de longo prazo

- concluir todos os atos;
- completar a primeira dificuldade;
- alcançar Veterano, Pesadelo, Infernal e Mítico;
- aperfeiçoar o herói para desafios superiores.

### Marcos de progressão

| Marco | Significado | Apresentação |
|---|---|---|
| Primeiro item raro | Primeira recompensa especial | Destaque no log e registro |
| Primeiro chefe derrotado | Primeiro teste de poder superado | Mensagem de conquista |
| Primeiro ato concluído | Primeiro arco encerrado | Tela ou painel de conclusão |
| Primeira dificuldade concluída | Domínio da campanha base | Destaque persistente |

Os marcos devem ser permanentes e aparecer no perfil ou histórico do herói. Na
v0.1, apenas os três primeiros precisam estar ativos, pois existe somente um ato
e a dificuldade Normal ainda não representa a campanha completa.

### Regras de retenção saudável

- não punir o jogador por fechar o jogo;
- não exigir cliques repetitivos;
- não usar notificações constantes;
- mostrar sempre a próxima meta;
- celebrar eventos raros sem interromper o fluxo;
- evitar recompensas diárias obrigatórias no MVP.

---

## 18. Eventos Aleatórios - V0.3

Eventos aleatórios adicionam variedade entre combates sem substituir o loop
principal.

### Exemplos

- **Mercador viajante:** apresenta uma oportunidade simples de troca.
- **Baú abandonado:** concede uma recompensa imediata.
- **Emboscada:** inicia um encontro mais perigoso.
- **Altar misterioso:** aplica um bônus temporário.
- **Portal demoníaco:** abre uma sequência curta de inimigos especiais.

### Princípios

- eventos devem ser curtos;
- o combate idle não deve ficar bloqueado esperando uma decisão;
- escolhas, quando existirem, precisam ter resposta automática após um tempo;
- recompensas não podem invalidar o loot normal;
- frequência deve ser baixa o bastante para preservar a surpresa.

### Integração

Eventos ocupam o mesmo fluxo dos encontros, mas possuem um tipo próprio. Mapas
podem definir quais eventos são possíveis e dificuldades podem alterar sua
frequência ou recompensa.

Eventos não fazem parte da v0.1 nem da v0.2.

---

## 19. Identidade Exclusiva de Taskbar - V0.4

Esta camada deve reforçar que TBH2 é um companheiro do computador, não apenas um
Idle RPG exibido em uma janela pequena.

### Tempo de sessão

O jogo registra quanto tempo o herói permaneceu em aventura durante a sessão.
Esse tempo pode alimentar estatísticas e marcos, sem incentivar o usuário a
manter o computador ligado desnecessariamente.

### Dias consecutivos

O herói reconhece retornos em dias seguidos. A sequência deve funcionar como
registro de companhia, não como punição. Perder um dia não deve apagar benefícios
permanentes nem causar ansiedade.

### Moral do aventureiro

Uma representação leve do estado do herói, influenciada por vitórias, derrotas e
tempo de jornada. A moral pode alterar pequenas falas ou elementos visuais antes
de afetar atributos.

### Eventos por horário

Determinados textos, cenários ou encontros podem variar entre manhã, tarde e
noite. O sistema deve usar apenas o horário local necessário e não coletar dados
externos.

### Bônus por presença contínua

Pequenos marcos de sessão podem reconhecer períodos de companhia. Os bônus devem
ser limitados e não transformar longas sessões em requisito de progressão.

### Princípios de privacidade e bem-estar

- não monitorar aplicações abertas;
- não registrar conteúdo digitado ou atividade pessoal;
- não recompensar inatividade artificial ilimitada;
- não penalizar pausas ou dias ausentes;
- explicar com clareza qualquer dado local utilizado.

Esses sistemas pertencem à v0.4 e exigem validação separada antes de afetarem a
economia do jogo.

---

## 20. Interface

### Formato

Janela lateral de aproximadamente 300 × 500 pixels.

### Informações prioritárias

1. dificuldade, ato e mapa;
2. progresso do mapa;
3. herói e inimigo atual;
4. barras de vida;
5. experiência e próximo nível;
6. recompensa ou evento recente;
7. equipamentos.

### Cabeçalho de campanha

Exemplo:

`Normal · Ato I · Mapa 4/10`

Abaixo:

`Progresso do mapa: 6/10 inimigos`

Essa informação substitui a sensação de progressão sem destino do modelo baseado
apenas em nível.

### Chefe

Ao chegar ao chefe, a interface deve:

- destacar o nome próprio;
- usar uma barra de vida diferenciada;
- comunicar que o avanço depende da vitória;
- mostrar claramente novas tentativas após derrotas.

### Registro de eventos

O registro exibe apenas acontecimentos recentes:

- ataques e dano;
- vitórias e derrotas;
- experiência;
- conclusão de mapa;
- loot;
- level up;
- marcos;
- chefe derrotado.

Eventos comuns devem ser discretos. Loot raro, chefes e marcos recebem maior
destaque.

---

## 21. Direção Visual e Sonora

### Visual

Fantasia sombria estilizada, com formas fortes e leitura clara em tamanho
reduzido.

Cada mapa pode variar:

- cor de fundo;
- ícone;
- nome;
- composição de inimigos.

Não é necessário produzir um cenário ilustrado exclusivo para todos os mapas na
v0.1. Paletas, ícones e pequenos elementos já podem comunicar mudança de região.

### Cores funcionais

- vermelho: vida e dano;
- azul: experiência;
- dourado: mapa concluído e level up;
- branco ou cinza: item comum;
- azul intenso: item raro;
- roxo: item épico;
- cor exclusiva: chefe.

### Áudio

O áudio é opcional no MVP. Sons futuros devem ser curtos e discretos para:

- golpe;
- vitória;
- derrota;
- level up;
- item raro;
- conclusão de mapa;
- chefe derrotado.

O jogo deve permanecer totalmente compreensível sem som.

---

## 22. Persistência

### Dados do herói

- nome;
- classe ou arquétipo;
- nível e experiência;
- Vida, Ataque e Defesa;
- equipamentos;
- estatísticas.

### Dados da campanha

- dificuldade atual;
- maior dificuldade desbloqueada;
- ato atual;
- mapa atual;
- progresso do mapa;
- atos concluídos;
- chefes derrotados;
- marcos alcançados.

### Retorno ao jogo

A batalha individual não precisa ser restaurada. O herói retorna ao mapa e
progresso consolidados.

### Progresso offline

Não faz parte da v0.1. Sua inclusão futura exige limites claros, pois afeta
experiência, loot, duração dos mapas e valor da presença contínua.

---

## 23. Balanceamento Inicial

### Metas de ritmo

- primeira vitória em menos de um minuto;
- primeiro level up nos primeiros minutos;
- primeiro mapa concluído em uma sessão curta;
- primeiro item comum cedo na maioria das jornadas;
- primeiro item raro como marco significativo;
- chefe alcançado após várias sessões curtas ou uma sessão prolongada;
- chefe difícil o bastante para validar crescimento, sem exigir espera excessiva.

### Curva dos mapas

- Mapas 1 a 3: apresentação e vitórias frequentes.
- Mapas 4 a 6: necessidade perceptível de níveis e equipamento.
- Mapas 7 a 9: preparação para o chefe.
- Mapa 10: teste de poder.

### Pontos de atenção

- inimigos totalmente ajustados ao nível anulam o crescimento;
- defesa excessiva pode prolongar combates;
- mapas longos demais enfraquecem metas curtas;
- mapas curtos demais banalizam o avanço;
- chefe impossível interrompe o fluxo idle;
- chefe fácil demais perde sua função;
- loot limitado perde valor após a obtenção dos melhores itens.

Os valores finais devem ser derivados de telemetria local de testes e observação,
não apenas das fórmulas iniciais.

---

## 24. Critérios de Sucesso da V0.1

A versão inicial será considerada bem-sucedida quando:

- o jogador entender o combate sem tutorial extenso;
- a próxima meta estiver sempre clara;
- concluir um mapa parecer um avanço real;
- o chefe criar expectativa e funcionar como teste de poder;
- nível e equipamento ajudarem a superar barreiras;
- a janela puder permanecer aberta sem incomodar;
- retornar ao jogo transmitir continuidade;
- o jogador demonstrar interesse em alcançar o próximo mapa ou ato.

### Perguntas para testes

- Você entendeu onde estava na campanha?
- Ficou claro como concluir o mapa?
- O avanço entre mapas pareceu significativo?
- O chefe pareceu diferente de um inimigo comum?
- Você entendeu como ficar mais forte após uma derrota?
- O loot gerou expectativa?
- A janela atrapalhou outras atividades?
- Você deixaria o jogo aberto durante o uso normal do computador?
- Qual foi a meta que mais motivou sua continuidade?

---

## 25. Riscos de Design

### Campanha automática demais

O jogador pode sentir pouca autoria. Classes e eventos futuros devem introduzir
decisões leves sem exigir atenção constante.

### Conteúdo insuficiente

Dez mapas com três inimigos podem parecer repetitivos. A v0.1 deve compensar com
ritmo, progressão visível, variação temática e o objetivo do chefe.

### Barreiras de poder frustrantes

Um chefe pode interromper a campanha por tempo demais. A derrota precisa indicar
que experiência e loot continuam fortalecendo o herói.

### Dificuldades repetitivas

Somente aumentar números não sustentará cinco ciclos no produto final.
Dificuldades superiores precisarão gradualmente de recompensas e variações, mas
isso não deve inflar o MVP.

### Escopo futuro antecipado

Classes, eventos e sistemas de Taskbar não devem ser parcialmente implementados
antes de o loop de campanha estar validado.

### Notificações excessivas

O jogo acompanha o usuário durante outras tarefas. Apenas marcos relevantes devem
pedir atenção.

---

## 26. Roadmap de Design

### V0.1 - Campanha vertical

- Ato I com 10 mapas;
- três inimigos comuns;
- um chefe;
- dificuldade Normal;
- progressão, loot e equipamento automático;
- marcos iniciais;
- persistência da campanha.

### V0.2 - Classes e expansão de conteúdo

- Guerreiro, Arqueiro, Mago e Curandeiro;
- diferenças passivas iniciais;
- expansão de inimigos e equipamentos;
- preparação ou inclusão dos atos seguintes conforme resultados da v0.1.

### V0.3 - Eventos aleatórios

- Mercador viajante;
- Baú abandonado;
- Emboscada;
- Altar misterioso;
- Portal demoníaco.

### V0.4 - Identidade Exclusiva de Taskbar

- tempo de sessão;
- dias consecutivos sem punição;
- moral do aventureiro;
- eventos por horário;
- bônus limitados por presença.

### Após a V0.4

- campanha completa;
- dificuldades superiores;
- variações de chefes;
- habilidades automáticas;
- expansão de loot;
- progressão offline, somente após análise da economia.

O roadmap é uma direção de design. Cada versão depende da validação da anterior.

---

## 27. Resumo da Experiência

TBH2 acompanha um herói que percorre automaticamente uma campanha organizada em
mapas, atos e dificuldades. Combates fornecem experiência e loot; mapas criam
metas curtas; chefes encerram atos; dificuldades oferecem objetivos duradouros.

A v0.1 preserva a simplicidade do conceito original ao entregar somente uma
fatia vertical: o Ato I, seus 10 mapas, três tipos de inimigos e um chefe. Essa
estrutura já permite testar progressão, retenção e clareza sem exigir todo o
conteúdo planejado.

Versões futuras adicionam classes, eventos aleatórios e mecânicas próprias de um
companheiro da Taskbar. Todas as expansões devem respeitar a promessa central:
TBH2 acompanha o usuário durante o dia, sem exigir que o usuário acompanhe o jogo
o tempo todo.

