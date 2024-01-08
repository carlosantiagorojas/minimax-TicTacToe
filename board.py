class Board:
    def __init__(self) -> None:
        self.bit_array = [0 for _ in range(9)]
    
    def __str__(self) -> str:
        return f"{self.bit_array}"
        