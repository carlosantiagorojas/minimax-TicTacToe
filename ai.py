"""Computer (AI) of the TicTacToe"""
import random
from position import Position


class AI:

    def __init__(self, position: Position) -> None:
        """Initialize the AI with the current position in the game.

        Args:
            position (Position): The position
        """
        self.position = position

    def make_ai_move(self) -> bool:
        """Make a move in the TicTacToe. 

        Based on the evaluation of all the possible moves of the current position.

        Returns:
            bool: True if the move was made, False otherwise.
        """
        p_moves_index = self.position.get_possible_moves()
        self.position.create_children(p_moves_index.copy())
        self.position.print_pos_children()

        # Choose the best move
        best_move_index = random.choice(p_moves_index)
        self.position.pos_list[best_move_index] = 0

        print("\nComputer move:")

    def minimax(self, start_position: Position, depth: int, maximizingAI: bool):
        if depth == 0:
            pass
