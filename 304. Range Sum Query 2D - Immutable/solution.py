from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix_sum: List[List[int]] = list()
        for row in range(len(matrix)):
            row_sum: List[int] = list()
            for column in range(len(matrix[row])):
                row_sum.append(matrix[row][column] + (row_sum[column - 1] if column > 0 else 0))
            for column in range(len(row_sum)):
                row_sum[column] = row_sum[column] + (self.prefix_sum[row - 1][column] if row > 0 else 0)
            self.prefix_sum.append(row_sum)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix_sum[row2][col2] - \
               (self.prefix_sum[row1 - 1][col2] if row1 > 0 else 0) - \
               (self.prefix_sum[row2][col1 - 1] if col1 > 0 else 0) + \
               (self.prefix_sum[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0)
