class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)

        #Memo
        # dp = [ [-1 for _ in range(2)] for _ in range(n)]

        # def rec(ind, buy):
        #     if ind == n:
        #         return 0
            
        #     if dp[ind][buy] != -1:
        #         return dp[ind][buy]

        #     if buy == 1:
        #         dp[ind][buy] = max(-prices[ind] + rec(ind+1, 0), 0 + rec(ind+1, 1))
        #     else:
        #         dp[ind][buy] = max(prices[ind] + rec(ind+1, 1) - fee, 0 + rec(ind+1, 0))

        #     return dp[ind][buy]

        # return rec(0,1)

        #Tabulation

        # dp = [ [0 for _ in range(2)] for _ in range(n+1)]

        # for ind in range(n-1, -1, -1):
        #     for buy in range(2):
        #         if buy == 1:
        #             dp[ind][buy] = max(-prices[ind] + dp[ind+1][0], 0 + dp[ind+1][1])
        #         else:
        #             dp[ind][buy] = max(prices[ind] + dp[ind+1][1] - fee, 0+dp[ind+1][0])

        # return dp[0][1]

        #Space optimized

        ahead = [0,0]
        curr = [0,0]

        for ind in range(n-1, -1, -1):
            for buy in range(2):
                if buy == 1:
                    curr[buy] = max(-prices[ind] + ahead[0], 0 + ahead[1])
                else:
                    curr[buy] = max(prices[ind] + ahead[1] - fee, 0 + ahead[0])

            ahead = curr.copy()

        return curr[1]

            