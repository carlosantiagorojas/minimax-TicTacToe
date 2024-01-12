from typing import List


class Position:
    def __init__(self, bit_list: list) -> None:
        """Intialize a new position

        Copy the current position of the game and create an empty list of children
        that represent the possible moves that can be made in the position.
        
        Args:
            bit_list (list): The current position of the TicTacToe game.
        """
        self.pos_list = bit_list
        self.pos_length = len(self.pos_list)
        self.eval_value = 0
        self.children: List["Position"] = []

        
    def create_children(self, p_moves_index: list) -> None:
        """ Create the children of the position 

        Args:
            p_moves_index (list): All the possible moves
        """
        # For each possible move, create a child
        while len(p_moves_index) > 0:
            pos_copy = list(self.pos_list)
            
            # Perform the first available move
            pos_copy[p_moves_index[0]] = 0
            child = Position(pos_copy)
            
            # Add the new child to the list of children
            self.children.append(child)
            
            # Remove the move that has been performed
            p_moves_index.pop(0)


    def print_children(self) -> None:
        """Show each child list of the position."""
        for child in self.children:
            print(child)
    
    
    def get_children(self) -> List["Position"]:
        """Get the children list.

        Returns:
            List["Position"]: The list of the children.
        """
        return self.children


    def get_children_length(self) -> int:
        """Get the number of children.

        Returns:
            int: Number of children.
        """
        return len(self.children)
    
    
    def __str__(self) -> str:
        """Print the current state of the position.

        Returns:
            str: The list of the position.
        """
        return f"{self.pos_list}"
