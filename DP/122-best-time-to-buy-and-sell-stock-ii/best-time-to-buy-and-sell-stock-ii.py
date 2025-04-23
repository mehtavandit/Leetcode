class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        #Memoization

        # dp = [ [-1 for _ in range(2)] for _ in range(n)]

        # def rec(ind, buy):
        #     if ind == n:
        #         return 0

        #     if dp[ind][buy] != -1:
        #         return dp[ind][buy]
        #     if buy == 1:
        #         take = -prices[ind] + rec(ind+1, 0)
        #         notTake = 0 + rec(ind+1, 1)
        #         profit = max(take, notTake)
        #     else:
        #         take = prices[ind] + rec(ind+1, 1)
        #         notTake = 0 + rec(ind+1, 0)
        #         profit = max(take, notTake)

        #     dp[ind][buy] = profit
        #     return profit

        # return rec(0,1)

        #Tabulation

        dp = [ [-1 for _ in range(2)] for _ in range(n+1)]

        dp[n][0] = dp[n][1] = 0

        for ind in range(n-1, -1, -1):
            for buy in range(2):
                profit = 0

                if buy == 1:
                    profit = max(0 + dp[ind+1][1], -prices[ind] + dp[ind+1][0])
                else:
                    profit = max(0 + dp[ind+1][0], prices[ind] + dp[ind+1][1])

                dp[ind][buy] = profit

        return dp[0][1]