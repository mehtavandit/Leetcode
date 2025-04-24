class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)

        dp = [ [-1 for _ in range(2)] for _ in range(n)]

        def rec(ind, buy):
            if ind >= n:
                return 0

            if dp[ind][buy] != -1:
                return dp[ind][buy]

            if buy == 1:
                profit = max(-prices[ind] + rec(ind+1, 0), 0 + rec(ind+1, 1))
            else:
                profit = max(prices[ind] + rec(ind+2, 1), 0 + rec(ind+1, 0))

            dp[ind][buy] = profit
            return dp[ind][buy]

        return rec(0,1)