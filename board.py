class Board:
    def __init__(self) -> None:
        self.bit_array = [None for _ in range(9)]
    
    
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
        print("\n")
        for i in range(0, len(self.bit_array)):
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
    
    
    def make_move_player(self, row: int, column: int) -> bool:
        """The player make a moved based on the row and the column in the array

        Args:
            row (int): Number of the row
            column (int): Number of the column

        Returns:
            bool: True if the move was made, False otherwise
        """
        
        moved = False
        # Subtract one to match the index of the array
        row -= 1 
        column -= 1
        
        # Make a move in the index of the array
        if row == 0:
            if self.bit_array[column] == None:
                self.bit_array[column] = 1
                moved = True
            else:
                print("\nERROR: The position it's already occupied select another")
        elif row == 1:
            if self.bit_array[column + row + 2] == None:
                self.bit_array[column + row + 2] = 1
                moved = True
            else:
                print("\nERROR: The position it's already occupied select another")
        elif row == 2:
            if self.bit_array[column + row + 4] == None:
                self.bit_array[column + row + 4] = 1
                moved = True
            else:
                print("\nERROR: The position it's already occupied select another")
        return moved