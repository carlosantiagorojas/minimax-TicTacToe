"""Represent the state of a position in a TicTacToeGame"""
from typing import List, Union


class Position:

    def __init__(self, pos_list: list) -> None:
        """Intialize a new position

        Copy the current position of the game and create an empty list of children
        that represent the possible moves that can be made in the position.
        
        Args:
            pos_list (list): The current position of the TicTacToe game.
        """
        self.pos_list = pos_list
        self.pos_length = len(self.pos_list)
        self.evaluation = 0
        self.children: List["Position"] = []
        self.game_over = False
        self.winner_player = None

    @property
    def game_over(self) -> bool:
        """Check if the game is finished or not."""
        result = self.check_game_status()
        if result is not None:
            self._game_over = True
            self.winner_player = result
        return self._game_over

    @game_over.setter
    def game_over(self, value: bool) -> None:
        """Set the finished status of the game.

        Args:
            value (bool): The finished status to set.
        """
        self._game_over = value
        
    @property
    def evaluation(self) -> int:
        """Generate a value evaluating a position with a heuristic.
        
        The evaluation consider this cases:
        - Make a three in a row +100
        - Block a three in a row +10
    
        Returns:
            int: The value generated for a position.
        """
        eval_score = 0
        
        # Row
        for i in range(0, self.pos_length, 3):
            row = self.pos_list[i:i+3]
            
            # Check if possible to do three in a row
            if row.count(0) == 3:
                eval_score += 100
            
            # Check if there are three 'X' and lose the game
            if row.count(1) == 3:
                eval_score -= 100
            
            # Check if there are two 'X' and '0' blocking it
            if row.count(0) == 1 and row.count(1) == 2:
                eval_score += 10
            
            # If the row it's not full
            if row.count(None) == 1:  
                # If the next move is in the center
                if row[1] == 0:
                    eval_score += 1
                # If the next move is in the corner
                if row[0] == 0: 
                    eval_score += 2
                if row[2] == 0:
                    eval_score += 2

        # Column
        for i in range(3):
            column = [self.pos_list[i], self.pos_list[i + 3], self.pos_list[i + 6]]
            
            # Check if possible to do three in a row
            if column.count(0) == 3:
                eval_score += 100
            
            # Check if there are three 'X' and lose the game
            if column.count(1) == 3:
                eval_score -= 100
            
            # Check if there are two 'X' and '0' blocking it
            if column.count(0) == 1 and column.count(1) == 2:
                eval_score += 10
           
            # If the column it's not full
            if column.count(None) == 1:
                # If the next move is in the corner
                if column[0] == 0:
                    eval_score += 2  
                if column[2] == 0:
                    eval_score += 2
                    
                # If the next move is in the center
                elif column[1] == 0:
                    eval_score += 1
                
        # Diagonal 
        diagonals = [[self.pos_list[0], self.pos_list[4], self.pos_list[8]], 
                    [self.pos_list[2], self.pos_list[4], self.pos_list[6]]]
        
        for diagonal in diagonals:
            # Check if possible to do three in a row
            if diagonal.count(0) == 3:
                eval_score += 100

            # Check if there are three 'X' and lose the game
            if diagonal.count(1) == 3:
                eval_score -= 100
    
            # Check if there are two 'X' and '0' blocking it
            if diagonal.count(0) == 1 and diagonal.count(1) == 2:
                eval_score += 10

        # If are two 'X' and '0' in the center and '0' in another corner -= 5
        if (diagonal[0] == 1 and diagonal[2] == 1 and diagonal[1] == 0) or \
        (diagonal[0] == 0 and diagonal[2] == 0 and diagonal[1] == 1):
            eval_score -= 5

        
        # The whole board
        
        # If the other player has the first move the second move is in the center
        if self.pos_list.count(None) == 6 and self.pos_list[4] == 0:
            eval_score += 5
        
        
        return eval_score
    
    @evaluation.setter
    def evaluation(self, value: int) -> None:
        """Set the evaluation value of the position.

        Args:
            value (int): The evaluation value to set.
        """
        self._evaluation = value
    
    @property
    def children_length(self) -> int:
        """Get the number of children.

        Returns:
            int: Number of children.
        """
        return len(self.children)
    
    def reset_position(self) -> None:
        """Reset the values of the list and set the game 
        unfinished to start another."""
        for i in range(self.pos_length):
            self.pos_list[i] = None
        self.game_over = False

    def create_children(self, p_moves_index: list, ai_turn: bool) -> None:
        """Create the children of the position.
        
        Make all the available moves and create a child for each move,
        with the player that moves next turn.
        
        Args:
            p_moves_index (list): All the possible moves.
            ai_turn (bool): True if it's the AI turn, False otherwise.
        """
        # For each possible move, create a child
        while len(p_moves_index) > 0:
            pos_copy = self.pos_list.copy( )
            
            if ai_turn:
                # Perform the first available move with 0 (computer turn)
                pos_copy[p_moves_index[0]] = 0
                child = Position(pos_copy)
            else:
                # Perfrom the first available move with 1 (player turn)
                pos_copy[p_moves_index[0]] = 1
                child = Position(pos_copy)
                
            # Add the new child to the list of children
            self.children.append(child)
            
            # Remove the move that has been performed
            p_moves_index.pop(0)
       
    def get_children(self) -> List["Position"]:
        """Get the children list.

        Returns:
            List["Position"]: The list of the children.
        """
        return self.children
    
    def get_possible_moves(self) -> list:
        """Get the list of the possible moves.

        Returns:
            list: List that have all the possible moves.
        """
        possible_moves = []
        for i in range(self.pos_length):
            if self.pos_list[i] == None:
                possible_moves.append(i)
        return possible_moves
       
    def copy(self):
        """Create a copy of the current position."""
        return Position(self.pos_list.copy())
    
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
        
        for i in range(self.pos_length): 
            
            # Verify the rows
            # If the current character is the same as the previous and is not none
            if self.pos_list[i] == temp and self.pos_list[i] is not None:
                char_row += 1
            
            # Save the previous character
            temp = self.pos_list[i]
            
            # If are three characters in a row
            if char_row == 2:
                return self.pos_list[i]
            
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
            if self.pos_list[i] is not None:
                # If a column contains the same character
                if self.pos_list[i] == self.pos_list[i + 3] == self.pos_list[i + 6]:
                    return self.pos_list[i]
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
        if (self.pos_list[index_start] 
            == self.pos_list[index_start + step]
            == self.pos_list[index_start + step * 2] is not None):
            return self.pos_list[index_start]
        return None
    
    def check_tie(self) -> Union[str, None]:
        """Check for a tie

        Returns:
           str: 'tie' if all the available movements have already been made and 
                 no winner found.
           None: if there still are available movements.
        """
        if all(character is not None for character in self.pos_list):
            return "tie"
        return None
    
    def print_pos_children(self) -> None:
        """Print all the possible moves of the current position like a TicTacToe."""
        print("Current position possible moves:")
        for child in self.children:
            child.print_tic_tac_toe()
            child.evaluation
            print("Evaluation value: ", child.evaluation)
     
    def print_tic_tac_toe(self) -> None:
        """Print the tic-tac-toe board to the console. 
        
        None values are printed as spaces, 1 as X and 0 as O.
        """
        print()
        for i in range(0, self.pos_length):
            if i % 3 == 2:
                if self.pos_list[i] == 1:
                    print('X')
                elif self.pos_list[i] == 0:
                    print('O')
                else:
                    print(' ')
                if i != len(self.pos_list) - 1:
                    print('---------')
            else:
                if self.pos_list[i] == 1:
                    print('X', end=' | ')
                elif self.pos_list[i] == 0:
                    print('O', end=' | ')
                else:
                    print(' ', end=' | ')

    def print_game_over(self) -> None:
        if self.winner_player == 1:
            print("\nGame finished X wins!")
        elif self.winner_player == 0:
            print("\nGame finished O wins!")
        else:
            print("\nGame finished in tie!")
                
    def print_children(self) -> None:
        """Show each child list of the position."""
        for child in self.children:
            print(child)
                
    def __str__(self) -> str:
        """Print the current state of the position.

        Returns:
            str: The list of the position.
        """
        return f"{self.pos_list}"