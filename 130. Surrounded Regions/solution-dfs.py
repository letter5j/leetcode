from typing import Optional, Dict, Set, List, Tuple
import copy


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        for column in range(n):
            self.traverse(board, 0, column)
            self.traverse(board, m - 1, column)
        for row in range(m):
            self.traverse(board, row, 0)
            self.traverse(board, row, n - 1)
        for row in range(m):
            for column in range(n):
                if board[row][column] == "#":
                    board[row][column] = "O"
                elif board[row][column] == "O":
                    board[row][column] = "X"
    def traverse(self, board: List[List[str]], row: int, column: int):
        if row < 0 or row >= len(board) or column < 0 or column >= len(board[row]):
            return
        if board[row][column] == "X" or board[row][column] == "#":
            return
        board[row][column] = "#"
        self.traverse(board, row + 1, column)
        self.traverse(board, row - 1, column)
        self.traverse(board, row, column + 1)
        self.traverse(board, row, column - 1)