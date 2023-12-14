from typing import List
import numpy as np


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        np_matrix = np.array(grid)

        row_ones = np.sum(np_matrix, axis=1)
        col_ones = np.sum(np_matrix, axis=0)

        row_zeros = np_matrix.shape[1] - row_ones
        col_zeros = np_matrix.shape[0] - col_ones

        row_diff = row_ones - row_zeros
        col_diff = col_ones - col_zeros

        diff = np.zeros(np_matrix.shape, dtype=int)

        diff += row_diff[:, np.newaxis]
        diff += col_diff

        return diff.tolist()

solution = Solution()
grid = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 1, 1]
]

result = solution.onesMinusZeros(grid)
print(result)
