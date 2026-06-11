# Game Loop

O loop central do TBH2 representa a jornada automática do aventureiro.

O jogador prepara o herói.

O jogo executa a jornada.

O ciclo principal é:

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

---

## Loop Principal

1. O jogo cria um novo `GameState` ou carrega um save existente.

2. O herói é posicionado no mapa atual da campanha.

3. Durante a exploração, o mundo permanece em movimento para transmitir jornada contínua.

4. O sistema seleciona um encontro compatível com:

   * ato atual;
   * mapa atual;
   * dificuldade atual;
   * pool de monstros da região.

5. Ao encontrar um inimigo, a exploração desacelera e o combate é iniciado.

6. Herói e inimigo executam ações automaticamente.

7. O resultado do combate depende da preparação do herói:

   * nível;
   * equipamentos;
   * atributos;
   * classe;
   * habilidades futuras;
   * Power;
   * Build Score.

8. Ao derrotar o inimigo, o herói recebe recompensas:

   * experiência;
   * ouro;
   * chance de loot;
   * progresso no mapa.

9. Caso um item seja encontrado, ele é adicionado ao inventário.

10. O sistema pode sugerir ou aplicar auto-equipamento quando o novo item for melhor para a build atual.

11. Ao acumular experiência suficiente, o herói sobe de nível.

12. Ao completar o objetivo do mapa, o próximo mapa é desbloqueado.

13. Ao chegar ao mapa final de um ato, o herói enfrenta o chefe do ato.

14. Ao derrotar o chefe, o próximo ato ou dificuldade pode ser desbloqueado.

15. Eventos importantes solicitam salvamento automático.

16. O ciclo retorna à exploração.

---

## Derrota

Se o herói for derrotado:

1. O combate é encerrado.
2. O avanço atual é interrompido.
3. O herói retorna a um estado seguro.
4. A vida é restaurada conforme a regra definida pelo balanceamento.
5. O chefe ou mapa permanece como bloqueio de progresso.
6. O jogador deve fortalecer o herói antes de tentar avançar novamente.

A derrota não deve apagar progresso principal.

Ela deve indicar que a build ainda não está pronta.

---

## Eventos que Salvam Progresso

O jogo deve salvar automaticamente em eventos importantes:

* criação de personagem;
* ganho de nível;
* obtenção de item relevante;
* equipamento alterado;
* conclusão de combate;
* avanço de mapa;
* derrota de chefe;
* desbloqueio de ato;
* desbloqueio de dificuldade;
* fechamento do jogo.

O save deve ser versionado e persistido pelo Sistema de Save.

---

## Regras do Game Loop

* O combate é automático.
* O jogador não controla ataques individuais.
* O jogador progride através de preparação e build.
* Inimigos são definidos pelo mundo, não apenas pelo nível do herói.
* Mapas são parte da progressão.
* Chefes bloqueiam avanço.
* Loot e equipamentos são a principal fonte de poder.
* O loop deve funcionar com baixa frequência de interação.
* A experiência deve continuar legível em janela compacta.
* O jogo deve permanecer executável e salvável a cada ciclo.

---

## Resumo Conceitual

```text
Carregar Save
↓
Explorar Mapa
↓
Encontrar Inimigo
↓
Combater Automaticamente
↓
Receber XP / Ouro / Loot
↓
Atualizar Herói
↓
Avançar Mapa ou Chefe
↓
Salvar Progresso
↓
Continuar Jornada
```
