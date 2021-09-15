from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            temp = 1
            for j in range(len(nums)):
                if i != j:
                    temp *= nums[j]
            output.append(temp)
        return output


    # class Solution:
    #     def productExceptSelf(self, nums: List[int]) -> List[int]:
    #         output = []
    #
    #         temp = 1 #곱할 값 곱셈이니깐 1부터 시작
    #         # 자기 자신을 제외하고 왼쪽에 있는 값 곱셈
    #         for i in range(len(nums)): #nums의 수 만큼 반복
    #             output.append(temp) #temp를 붙힌다 > 왼쪽으로 이동시킴
    #             temp *= nums[i] #왼쪽부터 차례대로 곱셈한다.
    #
    #         temp = 1 #초기화
    #         # 자기 자신을 제외하고 오른쪽에 있는 값 곱셈
    #         for i in range(len(nums) - 1, -1, -1):  # nums를 역순으로 탐색
    #             output[i] *= temp  #곱셈
    #             temp *= nums[i] #오른쪽부터 차례대로 곱셈한다.
    #
    #         return output

