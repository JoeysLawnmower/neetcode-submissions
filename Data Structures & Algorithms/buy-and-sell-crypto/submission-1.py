class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       
        b = 0
        s = 1  
        max_p = 0

        while s < len(prices):
            if prices[b] < prices[s]:
                profit = prices[s] - prices[b]
                max_p = max(max_p, profit)
            else:
                b = s
            
            
            s += 1
        return max_p

            