from typing import List, Tuple

from union_find import UnionFind


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])

        union_find = UnionFind(m * n + 1)
        dummy_head = m * n

        for column in range(n):
            if board[0][column] == "O":
                union_find.union(0 * column + column, dummy_head)
            if board[m - 1][column] == "O":
                union_find.union(n * (m - 1) + column, dummy_head)
        for row in range(m):
            if board[row][0] == "O":
                union_find.union(n * row, dummy_head)
            if board[row][n - 1] == "O":
                union_find.union(n * row + n - 1, dummy_head)
        offset: List[Tuple[int, int]] = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for row in range(1, m - 1, 1):
            for column in range(1, n - 1, 1):
                if board[row][column] == "O":
                    for offset_m, offset_n in offset:
                        offset_row = row + offset_m
                        offset_column = column + offset_n
                        if board[offset_row][offset_column] == "O":
                            union_find.union(n * row + column, n * offset_row + offset_column)

        for row in range(1, m - 1, 1):
            for column in range(1, n - 1, 1):
                if not union_find.connected(n * row + column, dummy_head):
                    board[row][column] = "X"
