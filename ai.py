"""Computer (AI) of the TicTacToe game"""
import random
from tic_tac_toe import TicTacToe
from position import Position


class AI:

    def __init__(self, game: TicTacToe) -> None:
        """Initialize the AI with the current game state.

        Args:
            game (TicTacToe): The game
        """
        self.game = game
    
    def make_ai_move(self) -> bool:
        """Make a move in the TicTacToe game. 
        
        Based on the evaluation of all the possible moves of the current position.

        Returns:
            bool: True if the move was made, False otherwise.
        """
        p_moves_index = self.get_possible_moves()
        
        # Create the first possible moves of the current position
        position = Position(self.game.bit_list)
        position.create_children(list(p_moves_index))
        self.print_pos_children(position)
        
        # Choose the best move
        best_move_index = random.choice(p_moves_index)
        self.game.bit_list[best_move_index] = 0
        
        print("\nComputer move:")

    def get_possible_moves(self) -> list:
        """Get the list of the possible moves.

        Returns:
            list: List that have all the possible moves.
        """
        possible_moves = []
        for i in range(0, self.game.list_length):
            if self.game.bit_list[i] == None:
                possible_moves.append(i)
        return possible_moves
    
    def print_pos_children(self, position: Position) -> None:
        """Print all the possible moves of the current position like a TicTacToe.
        
        Args:
            position (Position): The current position object.
        """
        print("Current position possible moves:")
        for child in position.children:
            self.game.print_tic_tac_toe(False, child)
            child.eval_value = self.evaluation(child)
            print("Evaluation value: ", child.eval_value)
       
    def evaluation(self, position: Position) -> int:
        """Generate a value evaluating the position.

        Args:
            position (Position): The evaluated position.

        Returns:
            int: The value generated for the position.
        """
        eval_score = 0
        # Block the three in a row
        
        # Rows
        two_char = 0
        temp = None
        for i in range(position.pos_length): 
            # If the current character is the same as the previous and is not none
            if position.pos_list[i] == temp and position.pos_list[i] is not None:
               two_char += 1
                
            if (two_char == 1 and position.pos_list[i] is not None 
                and position.pos_list[i] != temp):
                eval_score += 10
                
            # Save the previous character
            temp = position.pos_list[i]
            
            # Reset in the last character of the row
            if i == 2 or i == 5:
                two_char = 0
                temp = None
        
        return eval_score
        