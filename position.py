from typing import List


class Position:
    def __init__(self, bit_list: list) -> None:
        self.pos_list = bit_list
        self.pos_length = len(self.pos_list)
        self.eval_value = 0
        self.childs: List[Position] = []


    def __str__(self) -> str:
        """Print the current state of the position

        Returns:
            str: The list of the position
        """
        return f"{self.pos_list}"
    
    
    def create_childs(self, p_moves_index: list) -> None:
        """Crate the childs of the position 

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
            self.childs.append(child)
            
            # Remove the move that has been performed
            p_moves_index.pop(0)
    
    def get_childs_length(self) -> int:
        return len(self.childs)

    def show_childs(self) -> None:
        for child in self.childs:
            print(child)