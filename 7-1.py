from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(length - 1):
            for j in range(1, length):

                if nums[i] + nums[j] == target:
                    return i, j




number = [2,7,11,5]
target = 9
a = Solution()
print(a.twoSum(number,target))