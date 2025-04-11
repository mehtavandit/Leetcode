class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1 = len(text1)
        l2 = len(text2)

        dp = [ [-1 for _ in range(l2+1)] for _ in range(l1+1)]

        print(dp)

        def rec(i1, i2):
            if i1<0 or i2<0:
                return 0

            if dp[i1][i2] != -1:
                return dp[i1][i2]
          
            if text1[i1] == text2[i2]:
                dp[i1][i2] =  1 + rec(i1-1, i2-1)
            else:
                dp[i1][i2] =  0 + max(rec(i1-1, i2), rec(i1, i2-1))
            
            return dp[i1][i2]

        return rec(l1-1, l2-1)