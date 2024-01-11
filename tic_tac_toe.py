import random
from typing import Union, Optional
from position import Position


class TicTacToe:
    def __init__(self) -> None:
        self.bit_list = [None for _ in range(9)]
        self.list_length = len(self.bit_list)
        self.finished = False
    
    
    def __str__(self) -> str:
        """Print the current state of the bit list

        Returns:
            str: The list of the bits
        """
        return f"{self.bit_list}"
    
    
    def show_tic_tac_toe(self, main_game: bool, position: Optional[Position]) -> None:
        """Print the tic-tac-toe board to the console.
        
        None values are printed as spaces, 1 as X and 0 as O
        """
        if main_game:
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
    
    def make_move_user(self, row: int, column: int) -> bool:
        """Make a move in the TicTacToe based on the row and the column in the list

        Args:
            row (int): Number of the row
            column (int): Number of the column

        Returns:
            bool: True if the move was made, False otherwise
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

    
    def make_move_AI(self) -> bool:
        position = Position(self.bit_list)
        p_moves_index = self.get_possible_moves()
        position.create_childs(list(p_moves_index))
        print(position.get_childs_length())
        position.show_childs()
        
        best_move_index = random.choice(p_moves_index)
        self.bit_list[best_move_index] = 0
        
        print("\nComputer move: \n")
    
    
    def get_possible_moves(self) -> list:
        """Get the list of the possible moves

        Returns:
            list: List that have all the possible moves
        """
        possible_moves = []
        for i in range(0, self.list_length):
            if self.bit_list[i] == None:
                possible_moves.append(i)
        return possible_moves
    
    
    def reset_game(self) -> None:
        """Reset the values of the list and set the game unfinished to start another
        """
        for i in range(self.list_length):
            self.bit_list[i] = None
        self.finished = False
            
    
    def verify_status(self) -> Union[str, int, None]:
        """Verify the status of the game (user (X) wins, computer (O) wins, Tie or unfinished)

        Returns:
            Union[str, int, None]: 1 if the user wins (X), 0 if the computer wins (O), 
            'tie' if it's a tie and None if unfinished
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
            
            # Verify the columns
            
            if i <= 2:        
                if self.bit_list[i] is not None:
                    # If a column contains the same character
                    if (self.bit_list[i] == self.bit_list[i + 3] and 
                        self.bit_list[i + 3] == self.bit_list[i + 6]):
                        return self.bit_list[i]
            
            # Verify the diagonals

            if i == 0:
                # If the diagonal from top left to bottom right contains the same character
                if (self.bit_list[i] == self.bit_list[i + 4] and 
                    self.bit_list[i + 4] == self.bit_list[i + 8]):
                    return self.bit_list[i]
            elif i == 2:
                # If the diagonal from top right to bottom left contains the same character
                if (self.bit_list[i] == self.bit_list[i + 2] and 
                    self.bit_list[i + 2] == self.bit_list[i + 4]):
                    return self.bit_list[i]
        
        # Check for tie if all the movements have already been made 
        if all(character is not None for character in self.bit_list):
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
    
    def evaluation(self) -> int:
        """Do the evaluation of the position

        Returns:
            int: Result value of the evaluation
        """
        
        # About to get three in a row
        