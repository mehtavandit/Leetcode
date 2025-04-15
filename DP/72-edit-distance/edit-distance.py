class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)

        dp = [ [-1 for _ in range(l2)] for _ in range(l1)]


        def rec(i1, i2):
            if i1<0:
                return i2+1
            
            if i2 < 0 :
                return i1+1

            if dp[i1][i2] != -1:
                return dp[i1][i2]

            if word1[i1] == word2[i2]:
                return 0 + rec(i1-1, i2-1)
            insert = 1 + rec(i1, i2-1)
            delete = 1 + rec(i1-1, i2)
            replace = 1 + rec(i1-1, i2-1)

            dp[i1][i2] =  min(insert, delete, replace)
            return dp[i1][i2]

        return rec(l1-1, l2-1)