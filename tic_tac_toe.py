import random
from typing import Union

class TicTacToe:
    def __init__(self) -> None:
        self.bit_array = [None for _ in range(9)]
        self.array_length = len(self.bit_array)
        self.finished = False
    
    
    def __str__(self) -> str:
        """Print the current state of the bits

        Returns:
            str: The array of bits
        """
        return f"{self.bit_array}"
    
    
    def show_tic_tac_toe(self) -> None:
        """Print the tic-tac-toe board to the console.
        
        None values are printed as spaces, 1 as X and 0 as O
        """
        for i in range(0, self.array_length):
            if i % 3 == 2:
                if self.bit_array[i] == 1:
                    print('X')
                elif self.bit_array[i] == 0:
                    print('O')
                else:
                    print(' ')
                    
                if i != len(self.bit_array) - 1:
                    print('---------')
            else:
                if self.bit_array[i] == 1:
                    print('X', end=' | ')
                elif self.bit_array[i] == 0:
                    print('O', end=' | ')
                else:
                    print(' ', end=' | ')
    
    
    def make_move_user(self, row: int, column: int) -> bool:
        """Make a move in the TicTacToe based on the row and the column in the array

        Args:
            row (int): Number of the row
            column (int): Number of the column

        Returns:
            bool: True if the move was made, False otherwise
        """
        
        # Subtract one to match the index of the array
        row -= 1 
        column -= 1
        
        # Make a move in the index of the array
        if row == 0:
            if self.bit_array[column] == None:
                self.bit_array[column] = 1
                return True
        elif row == 1:
            if self.bit_array[column + row + 2] == None:
                self.bit_array[column + row + 2] = 1
                return True
        elif row == 2:
            if self.bit_array[column + row + 4] == None:
                self.bit_array[column + row + 4] = 1
                return True
        return False

    
    def make_move_AI(self) -> bool:
        p_moves_index = self.get_possible_moves()
        best_move_index = random.choice(p_moves_index)
        self.bit_array[best_move_index] = 0
        
        print("\nComputer move: \n")
    
    
    def get_possible_moves(self) -> list:
        """Get the list of the possible moves

        Returns:
            list: List that have all the possible moves
        """
        possible_moves = []
        for i in range(0, self.array_length):
            if self.bit_array[i] == None:
                possible_moves.append(i)
        return possible_moves
    
    
    def reset_game(self) -> None:
        """Reset the values of the array and set the game unfinished to start another
        """
        for i in range(self.array_length):
            self.bit_array[i] = None
        self.finished = False
            
    
    def verify_status(self) -> Union[str, int, None]:
        """Verify the status of the game (user (X) wins, computer (O) wins, Tie or unfinished)

        Returns:
            Union[str, int, None]: 1 if the user wins (X), 0 if the computer wins (O), 
            'tie' if it's a tie and None if unfinished
        """
        
        char_row = 0
        temp = None
        
        for i in range(self.array_length): 
            
            # Verify the rows
             
            # If the current character is the same as the previous and is not none
            if self.bit_array[i] == temp and self.bit_array[i] is not None:
                char_row += 1
            
            # Save the previous character
            temp = self.bit_array[i]
            
            # If are three characters in a row
            if char_row == 2:
                return self.bit_array[i]
            
            # Reset in the last character of the row
            if i == 2 or i == 5:
                char_row = 0
                temp = None
            
            # Verify the columns
            
            if i <= 2:        
                if self.bit_array[i] is not None:
                    # If a column contains the same character
                    if (self.bit_array[i] == self.bit_array[i + 3] and 
                        self.bit_array[i + 3] == self.bit_array[i + 6]):
                        return self.bit_array[i]
            
            # Verify the diagonals

            if i == 0:
                # If the diagonal from top left to bottom right contains the same character
                if (self.bit_array[i] == self.bit_array[i + 4] and 
                    self.bit_array[i + 4] == self.bit_array[i + 8]):
                    return self.bit_array[i]
            elif i == 2:
                # If the diagonal from top right to bottom left contains the same character
                if (self.bit_array[i] == self.bit_array[i + 2] and 
                    self.bit_array[i + 2] == self.bit_array[i + 4]):
                    return self.bit_array[i]
                
        if all(character is not None for character in self.bit_array):
            return "tie"
                
        # If the game it's not finished return None
        return None
    
    
    def verify_finish(self) -> None:
        """Verify that the game is finshed or not
        """
        result = self.verify_status()
        if result is not None:
            self.finished = True
            if result == 1:
                print("\nGame finished X wins!")
            elif result == 0:
                print("\nGame finished O wins!")
            else:
                print("\nGame finished in tie!")