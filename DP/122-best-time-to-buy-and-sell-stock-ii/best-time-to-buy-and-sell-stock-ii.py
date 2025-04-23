class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        dp = [ [-1 for _ in range(2)] for _ in range(n)]

        def rec(ind, buy):
            if ind == n:
                return 0

            if dp[ind][buy] != -1:
                return dp[ind][buy]
            if buy == 1:
                take = -prices[ind] + rec(ind+1, 0)
                notTake = 0 + rec(ind+1, 1)
                profit = max(take, notTake)
            else:
                take = prices[ind] + rec(ind+1, 1)
                notTake = 0 + rec(ind+1, 0)
                profit = max(take, notTake)

            dp[ind][buy] = profit
            return profit

        return rec(0,1)