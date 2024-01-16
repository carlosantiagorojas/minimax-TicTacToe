"""Represent the state of a position in a TicTacToeGame"""
from typing import List, Union


class Position:
    """Represent the state of a position in a TicTacToeGame
    
    Attributes
    ----------
    pos_list : list
        The current position of the TicTacToe game.
    pos_length : int
        The length of the position list.
    evaluation : int
        The evaluation value of the position.
    children : List["Position"]
        The list of the children of the position.
    game_over : bool
        True if the game is finished, False otherwise.
    winner_player : int
        The winner of the game.
        
    Methods
    -------
    check_win(player: int) -> bool
        Check if the specified player has won the game.
    create_children(p_moves_index: list, ai_turn: bool) -> None
        Create the children of the position.
    get_possible_moves() -> list
        Get the list of the possible moves.
    get_empty_positions() -> int
        Get the number of empty positions in the list.
    copy()
        Create a copy of the current position.
    check_game_status() -> Union[str, int, None]
        Check the status of the game.
    check_rows() -> Union[int, None]    
        Check the rows for a win.
    check_columns() -> Union[int, None]
        Check the columns for a win.
    check_diagonal(index_start: int, step: int) -> Union[int, None]
        Check if all elements in a diagonal are the same and not None.
    check_tie() -> Union[str, None]
        Check for a tie
    print_pos_children() -> None    
        Print all the possible moves of the current position like a TicTacToe.
    print_tic_tac_toe() -> None 
        Print the tic-tac-toe board to the console.
    print_game_over() -> None
        Print the winner of the game.
    print_children() -> None
        Show each child list of the position.
    __str__() -> str
        Print the current state of the position.
    """
    
    def __init__(self, pos_list: list) -> None:
        """Intialize a new position

        Copy the current position of the game and create an empty list of children
        that represent the possible moves that can be made in the position.
        
        Args:
            pos_list (list): The current position of the TicTacToe game.
            pos_length (int): The length of the position list.
            evaluation (int): The evaluation value of the position.
            children (List["Position"]): The list of the children of the position.
            game_over (bool): True if the game is finished, False otherwise.
            winner_player (int): The winner of the game.
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
        """Get the evaluation value of the position.

        If the computer (player 0) has won, it adds 100 to the evaluation score. 
        If the human player (player 1) has won, it subtracts 100 from the evaluation score. 

        The minimax algorithm uses this evaluation function to choose the move 
        that maximizes the potential score for the computer and minimizes the potential score 
        for the human player. 

        By assigning a value of 100 for a computer win and -100 for a human player win, 
        the minimax algorithm ensures that it explores all possibilities to maximize 
        the computer's chances of winning and minimize the human player's chances. 

        The simplicity of this evaluation is crucial for the efficiency of the minimax algorithm. 
        With only two possible outcomes (win or lose), the algorithm can efficiently 
        explore the entire game tree and make optimal decisions at each level. 

        This guarantees that the computer will either win or force a draw, 
        making it a reliable strategy to avoid losing the game.        

        Returns:
            int: The evaluation value of the position.
        """
        eval_score = 0
        if self.check_win(0):
            eval_score += 100 + self.get_empty_positions()
        elif self.check_win(1):
            eval_score -= 100

        return eval_score
    
    @evaluation.setter
    def evaluation(self, value: int) -> None:
        """Set the evaluation value of the position.

        Args:
            value (int): The evaluation value to set.
        """
        self._evaluation = value
    
    def check_win(self, player: int) -> bool:
        """Check if the specified player has won the game.

        Args:
            player (int): The player to check for a win.

        Returns:
            bool: True if the player has won, False otherwise.
        """
        # Check rows
        for i in range(0, self.pos_length, 3):
            if self.pos_list[i] == player and self.pos_list[i] == self.pos_list[i+1] == self.pos_list[i+2]:
                return True

        # Check columns
        for i in range(3):
            if self.pos_list[i] == player and self.pos_list[i] == self.pos_list[i+3] == self.pos_list[i+6]:
                return True

        # Check diagonals
        if self.pos_list[0] == player and self.pos_list[0] == self.pos_list[4] == self.pos_list[8]:
            return True
        if self.pos_list[2] == player and self.pos_list[2] == self.pos_list[4] == self.pos_list[6]:
            return True

        return False
    
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
        
    def get_empty_positions(self) -> int:
        """Get the number of empty positions in the list.

        Returns:
            int: The number of empty positions.
        """
        return self.pos_list.count(None)
       
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
        """Print the winner of the game."""
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