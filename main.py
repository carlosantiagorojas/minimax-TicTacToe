from game import Game


def main() -> None:
    """Start the TicTacToe game.

    This function creates a new game, displays the initial state of the game
    and then prompts the user to make a move.
    """
    print("""
    -----------------------------------------------------------------
    TicTacToe
    
    You start playing first in the first game and the computer the next one an so on.
    You play with 'X' and the computer with 'O'
    -----------------------------------------------------------------
    """)
    game = Game()
    game.position.print_tic_tac_toe()
    game.game_control()

if __name__ == "__main__":
    main()
