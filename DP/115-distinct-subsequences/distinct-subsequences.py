class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        l1 = len(s)
        l2 = len(t)

        dp = [ [-1 for _ in range(l2)] for _ in range(l1) ]

        def rec(i1, i2):
            if i2 < 0:
                return 1
            
            if i1 < 0:
                return 0

            if dp[i1][i2] != -1:
                return dp[i1][i2]

            if s[i1] == t[i2]:
                dp[i1][i2] =  rec(i1-1, i2-1) + rec(i1-1, i2)
            else:
                dp[i1][i2] =  rec(i1-1, i2)

            return dp[i1][i2]
            
        return rec(l1-1, l2-1)