class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf= 0
        n = len(prices)
        for i in range(n):
            for j in range(i, n):
                if prices[j] - prices[i] > maxProf:
                    maxProf = prices[j] - prices[i]
        return maxProf
