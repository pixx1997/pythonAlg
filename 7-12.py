from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0

        min_price = sys.maxsize

        #최대값 최소값 갱신
        for price in prices:
            answer = max(answer, price - min_price)
            min_price = min(min_price,price)


        return answer

