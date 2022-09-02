# JoKenPower Game

## Regras

- Este é um jogo de batalha por reflexo usando jokenpô.
- Cada jogador tem 100 de vida.
- O jogador tem 3 escolhas: **pedra**, **papel** ou **tesoura**
- Cada escolha tem sua propriedade:
    - Pedra: 
        - 10 de dano
        - 1s para atingir o outro jogador
        - 0,3s para receber contra-ataque
        - único que pode fingir; finge por 0,3s e troca
        - Contra-ataca Tesoura
    - Papel:
        - 1 de dano
        - 0,7s para atingir o outro jogador
        - 0,3s para receber contra-ataque
        - não pode fingir
        - Contra-ataca Pedra
    - Tesoura: 
        - 3 de dano
        - 0,7s para atingir o outro jogador
        - 0,3s para receber contra-ataque
        - não pode fingir
        - Contra-ataca Papel

|        | Pedra | Papel | Tesoura |
|--------|-------|-------|---------|
| Dano   | 10    | 3     | 1       |
| Tempo  | 1s    | 0.7s  | 0.7s    |
| Contra | 0,3s  | 0,3s  | 0,3s    |
| Fingir | Sim   | Não   | Não     |

## Combos

Sempre 3 ataques por combo

|    1    |    2    |    3    |
|---------|---------|---------|
|  Pedra  |  Pedra  |  Pedra  |
| Tesoura | Tesoura | Tesoura |
|  Papel  |  Papel  |  Papel  |
|  Pedra  | Tesoura |  Pedra  |
| Tesoura |  Pedra  |  Papel  |
etc

## Partida
- Acaba quando a vida de um dos jogadores chega a 0

## Exemplos
|||||||||||
|---|---|---|---|---|---|---|---|---|---|
|Pedra|Pedra|Pedra|Pedra|Pedra|Pedra|Pedra|Pedra|Pedra|Pedra|
|10|10|10|10|10|10|10|10|10|10|