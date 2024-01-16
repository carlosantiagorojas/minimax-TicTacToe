# Minimax algorithm for TicTacToe

This is a simple and well documented implementation of the minimax algorithm with alpha-beta pruning for the TicTacToe game in Python. The game allows a player to play against a computer opponent using this basic AI algorithm, which guarantees that the computer will either **WIN** or force a **DRAW**, try if you can beat it!

## How to Play

1. Run the game:

    ```bash
    python main.py
    ```

![TicTacToe game](img/game_start.png)

2. Follow the on-screen instructions to make your moves. To make a move, enter the column and row numbers separated by a space when prompted. For example, entering `2 3` would place your 'X' in the second column and third row. Or if you want to quit the game enter `exit`.

## The minimax algorithm

The minimax algorithm uses a simple evaluation function to choose the move that maximizes the potential score for the computer and minimizes the potential score for the human player. 

- Value of 100 for a computer win, plus the empty squares on the board.
- Value of -100 for a human player win. 

The simplicity of this evaluation is crucial for the efficiency of the minimax algorithm. With only two possible outcomes (win or lose), the algorithm can efficiently explore the entire game tree and make optimal decisions at each level.

## Alpha-beta pruning

Alpha-beta pruning is an optimization technique for the minimax algorithm. It reduces the number of nodes that the algorithm needs to explore in the game tree. This is achieved by maintaining the best possible scores for both the maximizing player (alpha) and the minimizing player (beta) at each level of the tree. If a node's score is worse than the maximizing player's best score, or better than the minimizing player's best score, that node can be pruned. This is because the respective players would never choose such nodes.