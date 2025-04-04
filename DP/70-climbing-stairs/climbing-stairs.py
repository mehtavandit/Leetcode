class Solution:
    def climbStairs(self, n: int) -> int:
        
        
        #recursion
        # if n==0:
        #     return 1
        # if n==1:
        #     return 1
        
        # return self.climbStairs(n-1) + self.climbStairs(n-2)

        #Memoization

        # dp = [-1] * (n+1)

        # def nested_fun(n):
        #     if n <= 1:
        #         return 1

        #     if dp[n] != -1:
        #         return dp[n]
            
        #     dp[n] = nested_fun(n-1) + nested_fun(n-2)

        #     return dp[n]

        # result = nested_fun(n)
        # return result

        #Tabulation

        if n <= 1:
            return 1

        dp = [-1] * (n+1)

        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]
