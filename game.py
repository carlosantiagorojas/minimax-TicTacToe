"""
Control the TicTacToe game.
It manages the game state, the game board is represented as a list of bits 
where 1 represents an X (player), 0 represents an O (computer).
"""
from position import Position
from ai import AI

class Game:
    """Control the TicTacToe game.
    
    It manages the game state, the game board is represented as a list of bits
    where 1 represents an X (player), 0 represents an O (computer).
    
    Parameters
    ----------
    position : Position
        The current position of the game.
    
    Methods
    -------
    game_control() -> None
        Control the order of who plays first and displays the TicTacToe board.
    make_move_player(column: int, row: int) -> bool
        Make a move in the TicTacToe based on the row and the column in the list.
    get_input() -> bool
        Get the move of the player and call the AI next to make another move.
    __str__() -> str
        Print the current state of the bit list.    
    """
    
    def __init__(self) -> None:
        """Initialize a new TicTacToe game."""
        self.position = Position([None for _ in range(9)])

    def game_control(self) -> None:
        """Control the order of who plays first and displays the TicTacToe board."""
        counter = 1
        ai = AI(self.position)
        while True:
            if self.position.game_over:
                self.position.print_game_over()
                # Reset the game and increment the counter to change who play first
                self.position.reset_position()
                counter += 1
                self.position.print_tic_tac_toe()

            # If the user moves
            if counter % 2 == 1:
                if not self.get_input():
                    break
                self.position.print_tic_tac_toe()

                if not self.position.game_over:
                    ai.make_ai_move()
                    self.position = ai.position
                    self.position.print_tic_tac_toe()
            else:
                ai.make_ai_move()
                self.position = ai.position
                self.position.print_tic_tac_toe()

                if not self.position.game_over:
                    if not self.get_input():
                        break
                    self.position.print_tic_tac_toe()

    def make_move_player(self, column: int, row: int) -> bool:
        """Make a move in the TicTacToe based on the row and the column in the list.

        Args:
            column (int): Number of the column.
            row (int): Number of the row.

        Returns:
            bool: True if the move was made, False otherwise.
        """
        # Subtract one to match the index of the list
        row -= 1
        column -= 1

        # Make a move in the index of the list
        if row == 0:
            if self.position.pos_list[column] == None:
                self.position.pos_list[column] = 1
                return True
        elif row == 1:
            if self.position.pos_list[column + row + 2] == None:
                self.position.pos_list[column + row + 2] = 1
                return True
        elif row == 2:
            if self.position.pos_list[column + row + 4] == None:
                self.position.pos_list[column + row + 4] = 1
                return True
        return False

    def get_input(self) -> bool:
        """Get the move of the player and call the AI next to make another move.

        Returns:
            bool: True if the player make a move. False if there is something wrong with the input
        
        Raises:
            ValueError: if the row or column are not the correct type.
        """
        while True:
            try:
                correct_col = False
                correct_row = False

                player_input = input(
                    "\nType the number of the column and row (1 to 3) separated by a space\nor 'exit' to quit: ")

                if player_input.lower() == "exit":
                    return False
                else: 
                    column, row = map(int, player_input.split())

                    if 1 <= row <= 3:
                        correct_row = True
                    if 1 <= column <= 3:
                        correct_col = True

                    if not correct_row and not correct_col:
                        print(
                            "ERROR: Type the number of the column and row in the specified range")
                    elif not correct_row:
                        print(
                            "ERROR: Type the number of the row in the specified range")
                    elif not correct_col:
                        print("ERROR: Type the number of the column in the specified range")
                    else:                
                        moved = self.make_move_player(column, row)
                        if not moved:
                            print("\nERROR: The position it's already occupied select another")
                            self.position.print_tic_tac_toe()
                        else:
                            return True
            except ValueError:
                print("ERROR: Type in the correct format")

    def __str__(self) -> str:
        """Print the current state of the bit list.

        Returns:
            str: The list of the bits.
        """
        return f"{self.position.pos_list}"