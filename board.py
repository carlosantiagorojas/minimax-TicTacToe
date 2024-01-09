class Board:
    def __init__(self) -> None:
        self.bit_array = [None for _ in range(9)]
    
    def show_tic_tac_toe(self) -> None:
        for i in range(0, len(self.bit_array)):
               if i % 3 == 2:
                   print(self.bit_array[i] if self.bit_array[i] is not None else ' ')
                   if i != len(self.bit_array) - 1:
                       print('---------')
               else:
                   print(self.bit_array[i] if self.bit_array[i] is not None else ' ', end=' | ')

    
    def __str__(self) -> str:
        return f"{self.bit_array}"