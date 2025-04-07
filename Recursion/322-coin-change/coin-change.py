class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        dp = [ [-1 for _ in range(amount+1)] for _ in range(n)]

        def rec(i, target):
            if i == 0:
                if target % coins[i] == 0:
                    return target // coins[i]
                else:
                    return float('inf')

            if dp[i][target] != -1:
                return dp[i][target]

            notTake = 0 + rec(i-1, target)
            take = float('inf')

            if coins[i] <= target:
                take = 1 + rec(i, target - coins[i])

            dp[i][target] = min(notTake, take)
            return dp[i][target]

        res =  rec(n-1, amount)
        return -1 if res == float('inf') else res