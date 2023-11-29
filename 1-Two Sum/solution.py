from typing import List


def twoSum( nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            if (target - nums[i] in hash):
                return [i, hash[target - nums[i]][1]]
            else:
                hash[nums[i]] = [target - nums[i], i]
print(twoSum([3,2,4,6],8))