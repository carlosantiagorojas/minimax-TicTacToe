"""
Control the TicTacToe game.
It manages the game state, the game board is represented as a list of bits 
where 1 represents an X (player), 0 represents an O (computer).
"""
from typing import Union, Optional
from position import Position


class TicTacToe:

    def __init__(self) -> None:
        """Initialize a new TicTacToe game."""
        self.bit_list = [None for _ in range(9)]
        self.list_length = len(self.bit_list)
        self.finished = False
 
    @property
    def finished(self) -> bool:
        """Check if the game is finished or not."""
        result = self.check_game_status()
        if result is not None:
            if result == 1:
                print("\nGame finished X wins!")
            elif result == 0:
                print("\nGame finished O wins!")
            else:
                print("\nGame finished in tie!")
            self._finished = True
        return self._finished

    @finished.setter
    def finished(self, value: bool) -> None:
        """Set the finished status of the game.

        Args:
            value (bool): The finished status to set.
        """ 
        self._finished = value

    def reset_game(self) -> None:
        """Reset the values of the list and set the game 
        unfinished to start another."""
        for i in range(self.list_length):
            self.bit_list[i] = None
        self.finished = False

    def make_move_player(self, row: int, column: int) -> bool:
        """Make a move in the TicTacToe based on the row and the column in the list.

        Args:
            row (int): Number of the row.
            column (int): Number of the column.

        Returns:
            bool: True if the move was made, False otherwise.
        """
        # Subtract one to match the index of the list
        row -= 1
        column -= 1

        # Make a move in the index of the list
        if row == 0:
            if self.bit_list[column] == None:
                self.bit_list[column] = 1
                return True
        elif row == 1:
            if self.bit_list[column + row + 2] == None:
                self.bit_list[column + row + 2] = 1
                return True
        elif row == 2:
            if self.bit_list[column + row + 4] == None:
                self.bit_list[column + row + 4] = 1
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
                    "\nType the number of the row and column (1 to 3) separated by a space\nor 'exit' to quit: ")

                if player_input.lower() == "exit":
                    return False
                else: 
                    row, column = map(int, player_input.split())

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
                        moved = self.make_move_player(row, column)
                        if not moved:
                            print("\nERROR: The position it's already occupied select another")
                            self.print_tic_tac_toe(True, None)
                        else:
                            return True
            except ValueError:
                print("ERROR: Type in the correct format")

    def check_game_status(self) -> Union[str, int, None]:
        """Check the status of the game.

        This function checks if the player (X) wins, the computer (O) wins, 
        if it's a tie, or if the game is unfinished.

        Returns:
            int: Returns 1 if the player wins (X).
            int: Returns 0 if the computer wins (O).
            str: Returns 'tie' if it's a tie.
            None: Returns None if the game is unfinished.
        """
        # Verify the rows
        result = self.check_rows()
        if result is not None:
            return result
        
        # Verify the columns
        result = self.check_columns()
        if result is not None:
            return result
            
        # Verify the diagonals
        # Top-left to bottom-right
        result = self.check_diagonal(0, 4)  
        if result is not None:
            return result
        # Top-right to bottom-left
        result = self.check_diagonal(2, 2)  
        if result is not None:
            return result
        
        # Verify tie
        result = self.check_tie()
        if result is not None:
            return result
                
        # If the game it's not finished return None
        return None

    def check_rows(self) -> Union[int, None]:
        """Check the rows for a win.

        Returns:
            int: Returns 1 if the player wins (X).
            int: Returns 0 if the computer wins (O).
            None: Returns None if no win is found.
        """
        char_row = 0
        temp = None
        
        for i in range(self.list_length): 
            
            # Verify the rows
            # If the current character is the same as the previous and is not none
            if self.bit_list[i] == temp and self.bit_list[i] is not None:
                char_row += 1
            
            # Save the previous character
            temp = self.bit_list[i]
            
            # If are three characters in a row
            if char_row == 2:
                return self.bit_list[i]
            
            # Reset in the last character of the row
            if i == 2 or i == 5:
                char_row = 0
                temp = None
                
        return None
    
    def check_columns(self) -> Union[int, None]:
        """Check the columns for a win.

        Returns:
            int: Returns 1 if the player wins (X).
            int: Returns 0 if the computer wins (O).
            None: Returns None if no win is found.
        """
        for i in range(3):
            if self.bit_list[i] is not None:
                # If a column contains the same character
                if self.bit_list[i] == self.bit_list[i + 3] == self.bit_list[i + 6]:
                    return self.bit_list[i]
        return None

    def check_diagonal(self, index_start: int, step: int) -> Union[int, None]:
        """Check if all elements in a diagonal are the same and not None.

        Args:
            index_start (int): The start index in the list.
            step (int): The step to add to the index.

        Returns:
            int: The value of the elements in the diagonal if they are all the 
                 same and not None.
            None: If the elements in the diagonal are not all the same 
                  or a element is None.
        """
        if (self.bit_list[index_start] 
            == self.bit_list[index_start + step]
            == self.bit_list[index_start + step * 2] is not None):
            return self.bit_list[index_start]
        return None
    
    def check_tie(self) -> Union[str, None]:
        """Check for a tie

        Returns:
           str: 'tie' if all the available movements have already been made and 
                 no winner found.
           None: if there still are available movements.
        """
        if all(character is not None for character in self.bit_list):
            return "tie"
        return None

    def print_tic_tac_toe(self, main_game: bool, position: Optional[Position]) -> None:
        """Print the tic-tac-toe board to the console. 
        
        None values are printed as spaces, 1 as X and 0 as O.
        
        Args:
            main_game (bool): True if want to print the TicTacToe main game
            position Optional[Position]: Pass antoher position to print
        """
        if main_game:
            print()
            for i in range(0, self.list_length):
                if i % 3 == 2:
                    if self.bit_list[i] == 1:
                        print('X')
                    elif self.bit_list[i] == 0:
                        print('O')
                    else:
                        print(' ')

                    if i != len(self.bit_list) - 1:
                        print('---------')
                else:
                    if self.bit_list[i] == 1:
                        print('X', end=' | ')
                    elif self.bit_list[i] == 0:
                        print('O', end=' | ')
                    else:
                        print(' ', end=' | ')
        else:
            print()
            for i in range(0, position.pos_length):
                if i % 3 == 2:
                    if position.pos_list[i] == 1:
                        print('X')
                    elif position.pos_list[i] == 0:
                        print('O')
                    else:
                        print(' ')

                    if i != position.pos_length - 1:
                        print('---------')
                else:
                    if position.pos_list[i] == 1:
                        print('X', end=' | ')
                    elif position.pos_list[i] == 0:
                        print('O', end=' | ')
                    else:
                        print(' ', end=' | ')
 
    def __str__(self) -> str:
        """Print the current state of the bit list.

        Returns:
            str: The list of the bits.
        """
        return f"{self.bit_list}"
