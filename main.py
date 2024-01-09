from tic_tac_toe import TicTacToe


def main() -> None:
    """Start the TicTacToe game.

    This function creates a new game, displays the initial state of the game,
    and then prompts the user to make a move.
    """
    game = TicTacToe()
    game.show_tic_tac_toe()
    get_move(game, False)


def get_move(game: TicTacToe, finished: bool) -> None:
    """Get the move of the player and call the AI next to make another move

    Args:
        game (TicTacToe): The TicTacToe object
        finished (bool): If the game it's finshed
    """
    while not finished:
        try:
            correct_col = False
            correct_row = False
            print("\nYou play with 'X' make a move")

            row = int(input("Type the number of the row (1 to 3): "))
            column = int(input("Type the number of the column (1 to 3): "))

            if 1 <= row <= 3:
                correct_row = True
            if 1 <= column <= 3:
                correct_col = True

            if correct_col and correct_row:
                moved = game.make_move_player(row, column)
                game.show_tic_tac_toe()
                if moved:
                    game.make_move_IA()
                else:
                    print("\nERROR: The position it's already occupied select another")
                    
            if not correct_row and not correct_col:
                print("ERROR: Type the number of the row and column in the specified range")
            elif not correct_row:
                print("ERROR: Type the number of the row in the specified range")
            elif not correct_col:
                print("ERROR: Type the number of the column in the specified range")

        except ValueError:
            print("ERROR: Type a number")

        
if __name__ == "__main__":
    main()