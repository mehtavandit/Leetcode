class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        dp = [ [-1 for _ in range(amount+1)] for _ in range(n) ]

        def rec(index, target):
            if index == 0:
                if target % coins[index] == 0:
                    return 1
                else:
                    return 0

            if dp[index][target] != -1:
                return dp[index][target]

            notTake = 0 + rec(index-1, target)
            take = 0

            if coins[index] <= target:
                take =  rec(index, target - coins[index])

            dp[index][target] =  notTake + take
            return dp[index][target]

        return rec(n-1, amount)


        