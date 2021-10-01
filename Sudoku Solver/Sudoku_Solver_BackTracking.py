from itertools import chain

from unsolved_grids import test1, test2, test3, test4


def is_valid(row: int, col: int, num: int, matrix: list[list[int]]) -> bool:
    box_x, box_y = row // 3 * 3, col // 3 * 3  # 0, 3, 6
    return num not in chain(matrix[row],  # Row wise checking
                            [*zip(*matrix)][col],  # Column wise checking
                            chain(*[*zip(*matrix[box_x: box_x + 3])][box_y: box_y + 3])  # Box wise checking
                            )


def solve(board: list[list[int]]) -> bool:
    for row in range(10):
        if row > 8:  # when all cells are filled
            return True
        for col in range(9):
            if board[row][col] != 0:  # when cell is already filled
                continue
            for num in range(1, 10):
                if is_valid(row, col, num, board):
                    board[row][col] = num
                    if solve(board):
                        return True
                    board[row][col] = 0
            return False


def matrix_printer(matrix: list[list[int]]) -> None:
    print(*matrix, sep='\n')
    print()


solve(test1)
solve(test2)
solve(test3)
solve(test4)

matrix_printer(test1)
matrix_printer(test2)
matrix_printer(test3)
matrix_printer(test4)
