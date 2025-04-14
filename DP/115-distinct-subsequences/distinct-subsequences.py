class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        l1 = len(s)
        l2 = len(t)

        # dp = [ [-1 for _ in range(l2)] for _ in range(l1) ]

        #Memoization
        # def rec(i1, i2):
        #     if i2 < 0:
        #         return 1
            
        #     if i1 < 0:
        #         return 0

        #     if dp[i1][i2] != -1:
        #         return dp[i1][i2]

        #     if s[i1] == t[i2]:
        #         dp[i1][i2] =  rec(i1-1, i2-1) + rec(i1-1, i2)
        #     else:
        #         dp[i1][i2] =  rec(i1-1, i2)

        #     return dp[i1][i2]
            
        # return rec(l1-1, l2-1)

        #Tabulation
        # dp = [ [0 for _ in range(l2+1)] for _ in range(l1+1) ]

        # for i1 in range(l1+1): #whenever i2 is 0 there is 1
        #     dp[i1][0] = 1

        # for i1 in range(1, l1+1):
        #     for i2 in range(1, l2+1):
        #         if s[i1-1] == t[i2-1]:
        #             dp[i1][i2] = dp[i1-1][i2-1] + dp[i1-1][i2]
        #         else:
        #             dp[i1][i2] = dp[i1-1][i2]

        # return dp[l1][l2] 

        #Space Optimized

        prev = [0] * (l2+1)
        prev[0] = 1

        for i1 in range(1, l1+1):
            curr = [0] * (l2+1)
            curr[0] = 1

            for i2 in range(1, l2+1):
                if s[i1-1] == t[i2-1]:
                    curr[i2] = prev[i2-1] + prev[i2]
                else:
                    curr[i2] = prev[i2]

            prev = curr

        return prev[-1]