from tic_tac_toe import TicTacToe


def main() -> None:
    """Start the TicTacToe game.

    This function creates a new game, displays the initial state of the game,
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
    game.show_tic_tac_toe()
    game_control(game)
    

def handle_move(game: TicTacToe) -> bool:
    """Handles the move base on the moved of the user

    Args:
        game (TicTacToe): The TiacTacToe object

    Returns:
        bool: False if the user wants to exit, True otherwise
    """
    status, row, column = get_move()
    if status == "exit":
        return False
    elif status == "continue":
        moved = game.make_move_user(row, column)
        if not moved:
            print("\nERROR: The position it's already occupied select another")
    return True

def game_control(game: TicTacToe) -> None:
    """Control the order of who plays first the user or the computer and displays
    the TicTacToe board

    Args:
        game (TicTacToe): The TiacTacToe object
    """
    counter = 1
    while True:
        if game.finished:
            counter += 1

        if counter % 2 == 1:
            if not handle_move(game):
                break
            game.show_tic_tac_toe()
            game.make_move_IA()
        else:
            game.make_move_IA()
            game.show_tic_tac_toe()
            if not handle_move(game):
                break

def get_move() -> tuple[str, int, int]:
    """Get the move of the user and call the AI next to make another move

    Returns:
        Tuple[str, Optional[int], Optional[int]]: A tuple containing the exit status, row, and column of the user move
    """
    while True:
        try:
            correct_col = False
            correct_row = False

            user_input = input(
                "\nType the number of the row and column (1 to 3) separated by a space\nor 'exit' to quit: ")
            print()
            if user_input.lower() == "exit":
                return "exit", None, None

            row, column = map(int, user_input.split())

            if 1 <= row <= 3:
                correct_row = True
            if 1 <= column <= 3:
                correct_col = True

            if correct_col and correct_row:
                return "continue", row, column

            if not correct_row and not correct_col:
                print("ERROR: Type the number of the row and column in the specified range")
            elif not correct_row:
                print("ERROR: Type the number of the row in the specified range")
            elif not correct_col:
                print("ERROR: Type the number of the column in the specified range")

        except ValueError:
            print("ERROR: Type in the correct format")
        
if __name__ == "__main__":
    main()