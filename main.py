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
    game.print_tic_tac_toe(True, None)
    game_control(game)
    

def game_control(game: TicTacToe) -> None:
    """Control the order of who plays first the user or the computer and displays
    the TicTacToe board

    Args:
        game (TicTacToe): The TicTacToe object
    """
    counter = 1
    while True:
        if game.finished:
            # Reset the game and increment the counter to change who play first
            game.reset_game()
            counter += 1
            print()
            game.print_tic_tac_toe(True, None)
            
        # If the user moves
        if counter % 2 == 1:
            if not make_move(game):
                break
            game.print_tic_tac_toe(True, None)
            game.check_game_finished()

            if not game.finished:
                game.make_ai_move()
                game.print_tic_tac_toe(True, None)
                game.check_game_finished()
        else:
            game.make_ai_move()
            game.print_tic_tac_toe(True, None)
            game.check_game_finished()
            
            if not game.finished:
                if not make_move(game):
                    break
                game.print_tic_tac_toe(True, None)
                game.check_game_finished()

 
def make_move(game: TicTacToe) -> bool:
    """Get the move of the user and call the AI next to make another move
    
    Args:
        game (TicTacToe): The TicTacToe object
        
    Returns:
        bool: True if the user make a move. False if there is something wrong with the input
    """
    while True:
        try:
            correct_col = False
            correct_row = False

            user_input = input(
                "\nType the number of the row and column (1 to 3) separated by a space\nor 'exit' to quit: ")
            print()
            
            if user_input.lower() == "exit":
                return False
            else: 
                row, column = map(int, user_input.split())

                if 1 <= row <= 3:
                    correct_row = True
                if 1 <= column <= 3:
                    correct_col = True

                if not correct_row and not correct_col:
                    print("ERROR: Type the number of the row and column in the specified range")
                elif not correct_row:
                    print("ERROR: Type the number of the row in the specified range")
                elif not correct_col:
                    print("ERROR: Type the number of the column in the specified range")
                else:                
                    moved = game.make_move_user(row, column)
                    if not moved:
                        print("\nERROR: The position it's already occupied select another\n")
                        game.print_tic_tac_toe()
                    else:
                        return True
        except ValueError:
            print("ERROR: Type in the correct format")
        
        
if __name__ == "__main__":
    main()