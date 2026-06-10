# TBH2 - TaskBar Hero 2

## Game Design Document - Versão Inicial

**Versão do documento:** 0.1  
**Gênero:** Idle RPG, fantasia sombria e progressão automática  
**Plataforma inicial:** Windows  
**Formato:** Jogo compacto para permanecer aberto ao lado de outras aplicações  
**Público inicial:** Jogadores que gostam de RPG, evolução de personagem, loot e jogos idle  
**Referências de fantasia:** Warcraft, Diablo, Dota e Dungeons & Dragons

---

## 1. Visão Geral

TBH2 é um Idle RPG de fantasia criado para acompanhar o jogador durante o uso
normal do computador. Em uma pequena janela lateral, um herói explora regiões
perigosas, enfrenta criaturas, ganha experiência e encontra equipamentos sem
exigir atenção constante.

O jogo deve transmitir a sensação de que existe uma pequena aventura acontecendo
continuamente na área de trabalho. O jogador pode observar o combate por alguns
instantes, conferir uma conquista, comparar o progresso ou simplesmente deixar o
herói continuar sua jornada.

A experiência não é construída em torno de reflexos ou comandos frequentes. Seu
prazer vem da progressão visível, da expectativa pelo próximo item e da
curiosidade sobre até onde o herói conseguirá chegar.

### Frase de apresentação

> Um herói vive uma aventura contínua na lateral da sua tela, lutando, evoluindo
> e encontrando equipamentos enquanto você faz outras coisas.

---

## 2. Fantasia Central

O jogador acompanha um aventureiro solitário em uma jornada por terras tomadas
por monstros. Esse herói não espera ordens para cada golpe: ele possui vontade
própria, enfrenta os perigos que encontra e se torna progressivamente mais
poderoso.

A fantasia desejada é a de manter um pequeno companheiro de aventuras sempre
presente. O jogador não controla diretamente cada ação, mas influencia a jornada
por meio do crescimento do personagem e, em versões futuras, por decisões de
especialização, equipamento e destino.

O herói deve passar de um aventureiro vulnerável, equipado com objetos
improvisados, para uma figura lendária capaz de enfrentar ameaças cada vez mais
perigosas.

---

## 3. Proposta de Valor

TBH2 procura combinar quatro experiências:

- A progressão constante dos jogos idle.
- A fantasia de poder e o loot dos RPGs de ação.
- A leitura rápida de uma interface de barra lateral.
- A companhia discreta de um jogo que pode permanecer aberto durante o dia.

O diferencial principal não é apenas possuir combate automático. É apresentar
uma aventura persistente em um espaço pequeno, com acontecimentos fáceis de
entender em poucos segundos.

---

## 4. Pilares de Design

### 4.1 Progressão sempre perceptível

Cada sessão deve produzir algum avanço. O jogador precisa identificar rapidamente
o que mudou: mais níveis, atributos melhores, inimigos derrotados ou um novo
equipamento.

### 4.2 Presença discreta

O jogo deve permanecer visível sem disputar atenção com o trabalho, estudo ou
entretenimento principal do usuário. Informações importantes precisam caber em
uma janela estreita e ser compreendidas de relance.

### 4.3 Combate legível

Mesmo sendo automático, o combate deve comunicar claramente quem atacou, quanto
dano foi causado, quanta vida resta e qual foi o resultado da batalha.

### 4.4 Recompensas com expectativa

Cada inimigo derrotado representa uma pequena chance de encontrar algo valioso.
Itens raros devem ser pouco frequentes o suficiente para gerar entusiasmo, sem
impedir o avanço normal do jogador.

### 4.5 Baixa punição

Na versão inicial, perder uma batalha não deve destruir progresso. A morte serve
como indicação de dificuldade, não como castigo. O herói renasce e continua sua
jornada.

### 4.6 Crescimento fácil de entender

Os sistemas iniciais devem ser transparentes. Níveis aumentam atributos, inimigos
mais fortes concedem mais experiência e itens melhores elevam o poder do herói.

---

## 5. Objetivos da Versão 0.1

A versão 0.1 deve provar que o ciclo central é agradável mesmo com pouca
interação. Ela precisa responder às seguintes perguntas:

- É interessante acompanhar o herói lutando sozinho?
- A progressão pode ser entendida em poucos segundos?
- Receber níveis e equipamentos gera vontade de continuar?
- A janela pequena funciona bem ao lado de outras aplicações?
- O jogador sente que sua aventura continua de uma sessão para outra?

O objetivo não é oferecer uma campanha extensa ou grande variedade de escolhas.
O objetivo é validar a identidade e o ritmo fundamentais do jogo.

---

## 6. Experiência Pretendida

### Primeiros minutos

O jogador abre o jogo, conhece seu herói e vê um inimigo surgir. O primeiro
combate começa imediatamente. Ataques alternados reduzem as barras de vida até
que um dos participantes caia.

Nos primeiros minutos, o jogador deve:

- Entender que o combate é automático.
- Ver a experiência aumentar.
- Derrotar diferentes tipos de inimigos.
- Perceber que o herói pode morrer sem perder progresso.
- Receber ou antecipar o primeiro equipamento.

### Primeira sessão

Ao longo da primeira sessão, o jogador acompanha vários combates, alcança pelo
menos um novo nível e começa a formar um conjunto de equipamentos. O avanço deve
ser rápido o suficiente para demonstrar todos os sistemas principais.

### Sessões seguintes

Ao retornar, o jogador encontra o mesmo herói e o progresso preservado. A
principal motivação é continuar fortalecendo o personagem e observar a evolução
dos números, equipamentos e desafios.

---

## 7. Ciclo Principal

1. Um inimigo adequado ao nível do herói aparece.
2. Herói e inimigo trocam ataques automaticamente.
3. A batalha continua até a derrota de um dos dois.
4. Ao vencer, o herói recebe experiência.
5. Existe uma chance de encontrar equipamento.
6. Equipamentos superiores são utilizados automaticamente.
7. Ao acumular experiência suficiente, o herói sobe de nível.
8. Um novo inimigo aparece e o ciclo recomeça.
9. Se o herói morrer, ele recupera toda a vida e inicia uma nova batalha.
10. O progresso é preservado para a próxima sessão.

### Ciclo emocional

O ciclo mecânico deve produzir a seguinte sequência:

**Expectativa → confronto → resultado → recompensa → crescimento → novo desafio**

---

## 8. O Herói

O herói representa toda a progressão do jogador na versão inicial.

### Identidade

O nome inicial sugerido é **Aventureiro**, podendo ser personalizado em uma
versão posterior. A versão 0.1 apresenta um único arquétipo generalista, sem
classes ou árvore de habilidades.

### Atributos

| Atributo | Função |
|---|---|
| Nível | Representa o estágio geral de evolução |
| Experiência | Progresso necessário para alcançar o próximo nível |
| Vida Máxima | Quantidade de dano que o herói suporta |
| Ataque | Dano base causado aos inimigos |
| Defesa | Reduz o dano recebido |

### Valores iniciais

| Atributo | Valor |
|---|---:|
| Nível | 1 |
| Experiência | 0 |
| Vida Máxima | 100 |
| Ataque | 10 |
| Defesa | 5 |

### Crescimento por nível

Sempre que o herói sobe de nível:

- Vida Máxima aumenta em 20.
- Ataque aumenta em 3.
- Defesa aumenta em 2.
- A vida atual é restaurada ao novo máximo.

### Experiência necessária

A experiência necessária para cada avanço é:

`Experiência necessária = nível atual × 100`

| Nível atual | Experiência necessária |
|---|---:|
| 1 | 100 |
| 2 | 200 |
| 3 | 300 |
| 4 | 400 |
| 5 | 500 |

Essa progressão é deliberadamente simples para tornar o sistema previsível
durante a validação inicial.

---

## 9. Inimigos

Os inimigos são encontros curtos e recorrentes. Cada criatura deve possuir uma
identidade reconhecível mesmo que a representação visual inicial seja limitada.

### Tipos iniciais

#### Goblin

Criatura oportunista e comum nas rotas abandonadas. É o inimigo mais equilibrado
e funciona como referência básica para os demais encontros.

**Perfil:** vida e ataque equilibrados.

#### Lobo

Predador veloz das regiões selvagens. Possui menor resistência, mas causa mais
dano e cria combates curtos e perigosos.

**Perfil:** vida menor e ataque maior.

#### Esqueleto

Restos reanimados de guerreiros esquecidos. É mais resistente, porém ataca com
menos força.

**Perfil:** vida maior e ataque menor.

### Nível dos inimigos

O nível de cada novo inimigo varia em torno do nível atual do herói:

`Nível do inimigo = nível do herói -1, igual ou +1`

O nível mínimo de qualquer inimigo é 1.

### Função da variação

- Inimigos abaixo do nível do herói oferecem vitórias confortáveis.
- Inimigos do mesmo nível representam o confronto padrão.
- Inimigos acima do nível do herói criam tensão e risco de derrota.

### Recompensa

Todo inimigo derrotado concede experiência. A recompensa deve crescer de acordo
com seu nível e perfil, permitindo que desafios maiores acelerem a progressão.

---

## 10. Sistema de Combate

O combate é automático e alternado.

### Sequência

1. O herói realiza um ataque.
2. O inimigo perde vida.
3. Se o inimigo sobreviver, ele contra-ataca.
4. O herói perde vida após a aplicação de sua defesa.
5. A sequência se repete até que alguém seja derrotado.

### Cálculo inicial de dano

O ataque do herói usa seu atributo de Ataque mais bônus de equipamento.

O dano recebido pelo herói é reduzido por sua Defesa. Todo ataque bem-sucedido
deve causar pelo menos 1 ponto de dano, evitando batalhas sem conclusão.

Na versão 0.1, os inimigos não possuem Defesa. Essa simplificação facilita a
leitura e o balanceamento inicial.

### Ritmo

Os golpes devem acontecer em intervalos regulares, rápidos o suficiente para que
as barras se movimentem com frequência, mas lentos o bastante para que o jogador
compreenda cada evento.

O ritmo desejado é de aproximadamente um ataque por segundo, sujeito a ajustes
após testes.

### Vitória

Quando um inimigo chega a zero de vida:

- A batalha termina imediatamente.
- O contador de inimigos derrotados aumenta.
- O herói recebe experiência.
- O jogo verifica a obtenção de loot.
- Um novo inimigo é apresentado.

### Derrota

Quando o herói chega a zero de vida:

- A batalha atual é perdida.
- O contador de mortes aumenta.
- Nenhuma experiência ou equipamento é removido.
- O herói renasce com vida cheia.
- Um novo inimigo é apresentado.

Não existem penalidades adicionais na versão 0.1.

---

## 11. Sistema de Loot

O loot é a principal fonte de surpresa da versão inicial. Após cada vitória, o
jogo realiza uma tentativa de recompensa.

### Probabilidades

| Resultado | Chance |
|---|---:|
| Nenhum item | 70% |
| Item Comum | 20% |
| Item Raro | 8% |
| Item Épico | 2% |

### Filosofia de raridade

- **Comum:** melhoria simples encontrada com frequência.
- **Raro:** salto relevante de poder e momento de destaque.
- **Épico:** recompensa excepcional, visualmente marcante e memorável.

### Equipamentos iniciais

| Item | Raridade | Espaço | Bônus |
|---|---|---|---:|
| Espada Enferrujada | Comum | Arma | +2 Ataque |
| Escudo de Madeira | Comum | Armadura | +1 Defesa |
| Machado do Caçador | Raro | Arma | +5 Ataque |
| Armadura de Couro | Raro | Armadura | +4 Defesa |
| Lâmina Carmesim | Épico | Arma | +10 Ataque |
| Armadura do Guardião | Épico | Armadura | +8 Defesa |

O Escudo de Madeira ocupa o espaço defensivo de Armadura na versão inicial. No
futuro, escudos poderão receber um espaço próprio.

### Equipamento automático

O jogo compara cada item encontrado com o item atualmente utilizado no mesmo
espaço.

- Se o novo item oferecer um bônus maior, ele é equipado.
- Se for igual ou inferior, o equipamento atual é mantido.
- A versão 0.1 não possui inventário, venda ou desmontagem.

Essa automação mantém o jogo funcional sem exigir gerenciamento constante.

### Comunicação da recompensa

Itens devem aparecer no registro de combate com nome e raridade. Recompensas
raras e épicas precisam receber maior destaque por cor, som ou animação quando
esses recursos estiverem disponíveis.

---

## 12. Progressão

### Progressão de curto prazo

O jogador acompanha barras de vida e experiência, vitórias individuais e
possíveis recompensas.

### Progressão de médio prazo

O herói acumula níveis, aumenta seus atributos e substitui equipamentos comuns
por itens raros ou épicos.

### Progressão de longo prazo

A versão 0.1 não possui um final formal. O avanço continua enquanto o crescimento
dos inimigos permitir combates funcionais.

Esse modelo é suficiente para o protótipo, mas não constitui sozinho uma
progressão sustentável para versões futuras. Regiões, chefes, classes,
habilidades e sistemas de prestígio serão candidatos naturais para expandir o
jogo.

---

## 13. Mundo e Ambientação

### Premissa

As antigas rotas do reino foram tomadas por criaturas depois do desaparecimento
da ordem que as protegia. O herói atravessa esses caminhos em busca da origem da
corrupção, enfrentando tudo o que encontra.

Na versão inicial, essa premissa funciona como contexto, não como campanha
narrativa completa.

### Região inicial sugerida: Fronteira Esquecida

Uma área de florestas secas, estradas abandonadas e ruínas de antigos postos de
vigia. A região comporta naturalmente os três inimigos iniciais:

- Goblins saqueiam viajantes e acampamentos.
- Lobos caçam nas trilhas e bosques.
- Esqueletos despertam próximos às ruínas.

### Tom

O mundo combina aventura heroica com fantasia sombria leve. A atmosfera pode ser
perigosa e melancólica, mas o jogo não deve se tornar opressivo. A progressão
constante preserva uma sensação de esperança e conquista.

---

## 14. Narrativa na Versão Inicial

A narrativa deve ser ambiental e mínima. O espaço reduzido da interface não
favorece longos diálogos durante o ciclo principal.

A história pode ser comunicada por:

- Nomes de regiões.
- Nomes e descrições curtas de inimigos.
- Nomes dos equipamentos.
- Mensagens ocasionais no registro de eventos.
- Marcos alcançados pelo herói.

Não haverá diálogos, missões ramificadas ou cenas narrativas na versão 0.1.

---

## 15. Interface e Experiência do Usuário

### Formato

A janela inicial possui aproximadamente 300 × 500 pixels e deve funcionar como
um painel lateral.

### Hierarquia de informações

#### Área do herói

- Nome.
- Nível.
- Vida atual e máxima.
- Barra de vida.
- Experiência atual e necessária.
- Barra de experiência.
- Ataque e Defesa.

#### Área do inimigo

- Nome.
- Nível.
- Vida atual e máxima.
- Barra de vida.

#### Área de equipamento

- Arma atual.
- Bônus de Ataque.
- Armadura atual.
- Bônus de Defesa.

#### Registro de combate

- Ataques realizados.
- Dano causado.
- Vitórias e derrotas.
- Experiência recebida.
- Level ups.
- Itens encontrados e equipados.

### Prioridade visual

O olhar do jogador deve encontrar, nesta ordem:

1. Situação atual da batalha.
2. Vida do herói e do inimigo.
3. Progresso para o próximo nível.
4. Recompensas recentes.
5. Equipamentos e estatísticas acumuladas.

### Cores sugeridas

- Vermelho: vida e dano.
- Azul: experiência e progressão.
- Roxo: inimigos e ameaças.
- Branco ou cinza: itens comuns.
- Azul intenso: itens raros.
- Roxo ou magenta: itens épicos.
- Dourado: level up e eventos especiais.

### Princípios de usabilidade

- Nenhuma ação frequente deve ser obrigatória.
- Textos devem permanecer legíveis em uma janela pequena.
- Mudanças importantes precisam ser reconhecíveis sem leitura detalhada.
- O registro deve mostrar apenas os acontecimentos recentes.
- O jogo deve continuar compreensível com o som desativado.

---

## 16. Direção Visual

### Estilo sugerido

Fantasia sombria estilizada, com formas fortes e leitura clara. O visual deve
evitar excesso de detalhes que desapareçam na pequena janela.

### Representação inicial

A primeira versão pode funcionar com retratos, ícones ou silhuetas estáticas do
herói e dos inimigos. Animações simples de impacto, brilho ou movimento de barra
já podem transmitir atividade.

### Objetivos visuais

- Distinguir imediatamente herói, inimigo e recompensa.
- Manter contraste adequado.
- Fazer itens raros parecerem especiais.
- Evitar poluição visual.
- Reforçar a sensação de uma aventura compacta.

---

## 17. Áudio

O áudio não é obrigatório para validar o primeiro protótipo, mas sua direção deve
ser definida.

### Sons prioritários futuros

- Golpe do herói.
- Golpe do inimigo.
- Vitória.
- Derrota e renascimento.
- Level up.
- Item raro ou épico.

Os sons precisam ser curtos e discretos, pois o jogo pode permanecer aberto
durante longos períodos. Controle de volume e opção de silenciar serão
necessários antes de uma distribuição pública.

---

## 18. Persistência da Jornada

Ao encerrar e reabrir o jogo, o jogador deve encontrar o herói no mesmo estado
geral de progressão.

### Informações preservadas

- Nome do herói.
- Nível.
- Experiência.
- Vida e atributos.
- Equipamentos atuais.
- Inimigos derrotados.
- Número de mortes.

A batalha em andamento não precisa ser preservada. Ao retornar, o herói pode
começar um novo confronto.

### Progresso offline

A versão 0.1 não concede recompensas enquanto o jogo está fechado. Esse recurso
deve ser avaliado posteriormente, pois altera significativamente o ritmo e a
economia do jogo.

---

## 19. Estatísticas

As estatísticas dão contexto à jornada e ajudam a demonstrar continuidade.

### Estatísticas iniciais

- Inimigos derrotados.
- Mortes do herói.
- Nível atual.
- Maior raridade de equipamento obtida.

### Estatísticas futuras

- Tempo total de aventura.
- Dano total causado.
- Maior dano em um golpe.
- Quantidade de itens por raridade.
- Chefes derrotados.
- Maior sequência de vitórias.

---

## 20. Balanceamento Inicial

O balanceamento deve favorecer demonstrações rápidas dos sistemas.

### Metas preliminares

- A primeira vitória deve ocorrer em menos de um minuto.
- O primeiro level up deve ocorrer nos primeiros minutos.
- Um item comum deve aparecer cedo na maioria das sessões.
- A morte deve ser possível, mas não dominar as primeiras batalhas.
- Equipamentos raros devem causar uma melhoria perceptível.
- Itens épicos devem continuar especiais mesmo após uma sessão prolongada.

### Pontos de atenção

- Defesa excessiva pode reduzir todo dano a 1 e tornar combates demorados.
- Crescimento linear infinito pode produzir batalhas desequilibradas em níveis
  altos.
- Equipamento automático perde interesse quando todos os melhores itens já foram
  obtidos.
- Uma lista muito curta de inimigos pode tornar a observação repetitiva.
- A ausência de escolhas limita o envolvimento em sessões longas.

Essas limitações são aceitáveis no MVP, desde que sejam observadas e registradas
durante os testes.

---

## 21. Escopo da Versão 0.1

### Incluído

- Um herói persistente.
- Atributos de Vida, Ataque e Defesa.
- Experiência e níveis.
- Combate automático.
- Três tipos de inimigos.
- Variação de nível dos inimigos.
- Vitória, derrota e renascimento.
- Seis equipamentos.
- Três raridades.
- Equipamento automático.
- Interface lateral compacta.
- Registro de eventos.
- Estatísticas básicas.
- Salvamento e carregamento da jornada.

### Fora do escopo

- Controle direto do combate.
- Classes.
- Habilidades ativas ou passivas.
- Magias.
- Inventário.
- Loja e moedas.
- Missões.
- Chefes.
- Regiões jogáveis distintas.
- Progressão offline.
- Prestígio ou renascimento de conta.
- Conquistas.
- Multiplayer.
- Serviços online.
- História completa.
- Criação detalhada de personagem.

---

## 22. Critérios de Sucesso

A versão inicial será considerada bem-sucedida quando:

- O jogador entender o ciclo sem tutorial extenso.
- O estado da batalha puder ser lido rapidamente.
- Níveis e equipamentos transmitirem crescimento real.
- O jogo puder permanecer aberto sem exigir atenção constante.
- Retornar ao jogo produzir sensação de continuidade.
- O jogador demonstrar curiosidade pelo próximo nível ou item.
- O ciclo permanecer interessante durante uma sessão curta de teste.

### Perguntas para testes com jogadores

- Você entendeu o que estava acontecendo sem explicação?
- Em algum momento sentiu vontade de interferir no combate?
- A progressão pareceu rápida, lenta ou adequada?
- O loot gerou expectativa?
- Quais informações você procurou primeiro?
- A janela atrapalhou outras atividades?
- Você teria vontade de deixar o jogo aberto?
- O que esperaria encontrar na próxima versão?

---

## 23. Riscos de Design

### Pouca agência

Sem escolhas, o jogador pode sentir que apenas observa números. A versão 0.1 deve
validar o prazer da observação, mas versões futuras precisarão introduzir decisões
sem abandonar a natureza idle.

### Repetição

Três inimigos e seis itens formam um conjunto pequeno. O ritmo dos eventos e a
clareza da progressão precisarão sustentar o protótipo durante testes curtos.

### Progressão sem objetivo

Ganhar níveis indefinidamente pode perder significado. Marcos, regiões e chefes
são caminhos recomendados para estabelecer objetivos futuros.

### Excesso de notificações

Um jogo sempre aberto pode se tornar incômodo se cada golpe exigir atenção.
Eventos comuns devem ser discretos; apenas conquistas relevantes merecem
destaque.

### Escalada numérica

Fórmulas lineares são adequadas para o protótipo, mas devem ser revistas antes de
uma progressão longa.

---

## 24. Direção para Versões Futuras

As expansões devem adicionar escolhas em camadas, mantendo o combate automático
como base.

### Candidatos para a versão 0.2

- Seleção de nome e arquétipo do herói.
- Mais inimigos e equipamentos.
- Regiões com identidade e dificuldade próprias.
- Primeiro chefe.
- Pequenos eventos aleatórios.
- Sons e efeitos visuais.
- Tela de estatísticas.

### Candidatos para versões posteriores

- Classes e especializações.
- Habilidades automáticas.
- Inventário e comparação de itens.
- Atributos secundários, como crítico e velocidade.
- Qualidade variável dos equipamentos.
- Missões e objetivos diários.
- Progressão offline.
- Sistema de prestígio.
- Companheiros.
- Conquistas.
- Narrativa por capítulos.

Toda expansão deve respeitar a promessa central: o jogo acompanha o usuário, não
exige que o usuário acompanhe o jogo o tempo todo.

---

## 25. Resumo da Experiência

TBH2 v0.1 apresenta um herói persistente que enfrenta automaticamente Goblins,
Lobos e Esqueletos em uma região de fantasia sombria. Cada vitória concede
experiência e pode revelar um equipamento. Níveis e itens tornam o herói mais
forte, permitindo que a aventura continue contra inimigos cada vez mais
poderosos.

O jogador observa essa jornada por meio de uma pequena janela lateral, capaz de
comunicar batalha, crescimento e recompensas em poucos segundos. Não existe
punição severa, gerenciamento complexo ou necessidade de comandos constantes.

A versão inicial deve ser simples, legível e satisfatória. Seu propósito é
confirmar que acompanhar um pequeno herói vivendo continuamente na barra lateral
do computador é uma fantasia forte o suficiente para sustentar a evolução do
projeto.

