class Solution:
    def fib(self, n: int) -> int:

        #Memoization Approach
        # dp = [-1] * (n+1)

        # def nested_function(n):
        #     if n<= 1:
        #         return n

        #     if dp[n] != -1:
        #         return dp[n]

        #     dp[n] = nested_function(n-1) + nested_function(n-2)
        #     return dp[n]

        # result = nested_function(n)
        # return result

        #tabulation (bottom - up)

        if n<=1:
            return n

        dp = [-1] * (n+1)

        dp[0] = 0
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]