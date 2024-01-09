from board import Board


def main():
    board = Board()
    board.show_tic_tac_toe()
    get_move(board, False)

def get_move(board: Board, finished: bool) -> None:
    while not finished:
        try:
            correct_col = False
            correct_row = False
            print("\nYou play with 'X' make a move")

            row = int(input("Type the number of the row (1 to 3): "))
            column = int(input("Type the number of the column (1 to 3): "))

            if 1 <= row <= 3:
                correct_row = True
            if 1 <= column <= 3:
                correct_col = True

            if correct_col and correct_row:
                board.make_move_player(row, column)
                board.show_tic_tac_toe()

            if not correct_row and not correct_col:
                print("ERROR: Type the number of the row and column in the specified range")
            elif not correct_row:
                print("ERROR: Type the number of the row in the specified range")
            elif not correct_col:
                print("ERROR: Type the number of the column in the specified range")

        except ValueError:
            print("ERROR: Type a number")

        
if __name__ == "__main__":
    main()