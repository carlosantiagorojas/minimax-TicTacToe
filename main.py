from tic_tac_toe import TicTacToe
from ai import AI


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
    game = TicTacToe()
    game.print_tic_tac_toe(True, None)
    game_control(game)


def game_control(game: TicTacToe) -> None:
    """Control the order of who plays first and displays the TicTacToe board.

    Args:
        game (TicTacToe): The TicTacToe object.
    """
    counter = 1
    ai = AI(game)
    while True:
        if game.finished:
            # Reset the game and increment the counter to change who play first
            game.reset_game()
            counter += 1
            game.print_tic_tac_toe(True, None)

        # If the user moves
        if counter % 2 == 1:
            if not game.get_input():
                break
            game.print_tic_tac_toe(True, None)

            if not game.finished:
                ai.make_ai_move()
                game.print_tic_tac_toe(True, None)
        else:
            ai.make_ai_move()
            game.print_tic_tac_toe(True, None)

            if not game.finished:
                if not game.get_input():
                    break
                game.print_tic_tac_toe(True, None)


if __name__ == "__main__":
    main()
