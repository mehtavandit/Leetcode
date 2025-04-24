class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        dp = [ [ [-1 for _ in range(k+1)] for _ in range(2)] for _ in range(n) ]

        def rec(ind, buy, cap):
            if cap == 0:
                return 0
            if ind == n:
                return 0

            if dp[ind][buy][cap] != -1:
                return dp[ind][buy][cap]

            if buy == 1:
                profit = max(-prices[ind] + rec(ind+1, 0, cap) , 0 + rec(ind+1, 1, cap))
            else:
                profit = max(prices[ind] + rec(ind+1, 1, cap-1), 0 + rec(ind+1, 0, cap))

            dp[ind][buy][cap] = profit
            return dp[ind][buy][cap]

        return rec(0, 1, k)