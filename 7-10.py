from typing import List
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort() #정렬을 먼저 해준다.
        sum =0 # sum값 초기화

        for i,n in enumerate(nums): #순서대로 nums값을 입력받음
            if i % 2 ==0: #짝수일경우
                sum += n #더해줌.
        return sum
