class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        # Memoization
        # dp = [ [-1 for _ in range(amount+1)] for _ in range(n) ]

        # def rec(index, target):
        #     if index == 0:
        #         if target % coins[index] == 0:
        #             return 1
        #         else:
        #             return 0

        #     if dp[index][target] != -1:
        #         return dp[index][target]

        #     notTake = 0 + rec(index-1, target)
        #     take = 0

        #     if coins[index] <= target:
        #         take =  rec(index, target - coins[index])

        #     dp[index][target] =  notTake + take
        #     return dp[index][target]

        # return rec(n-1, amount)

        # Tabulation

        # dp = [ [0 for _ in range(amount+1)] for _ in range(n) ]

        # for target in range(amount + 1):
        #     if target % coins[0] == 0:
        #         dp[0][target] = 1
        #     else:
        #         dp[0][target] = 0


        # for i in range(1, n):
        #     for target in range(amount+1):
        #         notTake = dp[i-1][target]
        #         take = 0

        #         if coins[i] <= target:
        #             take = dp[i][target-coins[i]]

        #         dp[i][target] = take + notTake

        # return dp[n-1][amount]

        #Space Optmized
        prev = [0 for _ in range(amount+1)]

        for target in range(amount+1):
            if target % coins[0] == 0:
                prev[target] = 1
            else:
                prev[target] = 0

        for i in range(1, n):
            curr = [0 for _ in range(amount+1)]

            for target in range(amount+1):
                notTake = prev[target]
                take = 0

                if coins[i] <= target:
                    take = curr[target - coins[i]]

                curr[target] = notTake + take
            
            prev = curr

        return prev[-1]




        