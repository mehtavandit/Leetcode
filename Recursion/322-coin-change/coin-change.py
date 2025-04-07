class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        dp = [ [-1 for _ in range(amount+1)] for _ in range(n)]

        #Memoization
        # def rec(i, target):
        #     if i == 0:
        #         if target % coins[i] == 0:
        #             return target // coins[i]
        #         else:
        #             return float('inf')

        #     if dp[i][target] != -1:
        #         return dp[i][target]

        #     notTake = 0 + rec(i-1, target)
        #     take = float('inf')

        #     if coins[i] <= target:
        #         take = 1 + rec(i, target - coins[i])

        #     dp[i][target] = min(notTake, take)
        #     return dp[i][target]

        # res =  rec(n-1, amount)
        # return -1 if res == float('inf') else res

        #Tabulation

        # dp = [ [0 for _ in range(amount+1)] for _ in range(n)]

        # for target in range(0, amount+1):
        #     if target % coins[0] == 0:
        #         dp[0][target] = target // coins[0]
        #     else:
        #         dp[0][target] = float('inf')

        # for i in range(1, n):
        #     for target in range(0, amount + 1):
        #         notTake = 0 + dp[i-1][target]
        #         take = float('inf')

        #         if coins[i] <= target:
        #             take = 1 + dp[i][target - coins[i]]

        #         dp[i][target] = min(notTake, take)

        # res = dp[n-1][amount]

        # return -1 if res == float('inf') else res 

        #Space Optimized

        prev = [0 for _ in range(amount + 1)]

        for target in range(amount+1):
            if target % coins[0] == 0:
                prev[target] = target // coins[0]
            else:
                prev[target] = float('inf')

        for i in range(1, n):
            curr = [0 for _ in range(amount+1)]

            for target in range(amount+1):
                notTake = 0 + prev[target]
                take = float('inf')

                if coins[i] <= target:
                    take = 1 + curr[target - coins[i]]

                curr[target] = min(notTake, take)

            prev = curr


        res = prev[-1]
        return -1 if res == float('inf') else res 


