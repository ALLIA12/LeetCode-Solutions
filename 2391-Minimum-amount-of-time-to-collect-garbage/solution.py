from typing import List


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        maxIndexG = maxIndexP = maxIndexM = -1
        countG = countP = countM = 0
        for i in range(len(garbage) - 1, -1, -1):
            if maxIndexG == -1 and "G" in garbage[i]:
                maxIndexG = i
            if maxIndexP == -1 and "P" in garbage[i]:
                maxIndexP = i
            if maxIndexM == -1 and "M" in garbage[i]:
                maxIndexM = i
            countG += garbage[i].count("G")
            countP += garbage[i].count("P")
            countM += garbage[i].count("M")
        timeG = timeP = timeM = 0
        if maxIndexG != -1:
            timeG = countG + sum(travel[:maxIndexG])
        if maxIndexP != -1:
            timeP = countP + sum(travel[:maxIndexP])
        if maxIndexM != -1:
            timeM = countM + sum(travel[:maxIndexM])
        return timeG + timeP + timeM


temp = Solution()
print(temp.garbageCollection(["G", "P", "GP", "GG"], [2, 4, 3]))
