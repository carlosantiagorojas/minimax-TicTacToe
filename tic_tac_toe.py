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

    
    def make_move_IA(self) -> bool:
        # self.get_possible_moves()
        pass
    
    
    # def get_possible_moves(self) -> list:
    #     possible_moves = []
    #     for i in self.array_length:
    #         if self.bit_array[i] == None:
    #             possible_moves.append(i)