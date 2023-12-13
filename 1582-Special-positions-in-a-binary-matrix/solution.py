from typing import List


class Solution:

    def numSpecial(self, mat: List[List[int]]) -> int:
        count = 0
        # for i in range(len(mat)):
        #     for j in range(len(mat[i])):
        #         print(mat[i][j], end="")
        #     print()
        for i in range(len(mat)):
            columnIndexToCheck = -1
            currRow = mat[i]
            sumcurr = sum(currRow)
            if sumcurr == 1:
                for j in range(len(currRow)):
                    if currRow[j] == 1:
                        columnIndexToCheck = j
                        break
                currCol = [row[columnIndexToCheck] for row in mat]
                sumcurr = sum(currCol)
                if sumcurr == 1:
                    count += 1
        return count


test = Solution()
print(test.numSpecial([[0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0]]))
