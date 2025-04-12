class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)

        dp = [ [-1 for _ in range(l2+1)] for _ in range(l1+1)]

        for i1 in range(l1+1):
            dp[i1][0] = 0

        for i2 in range(l2+1):
            dp[0][i2] = 0

        for i1 in range(1,l1+1):
            for i2 in range(1,l2+1):
                if word1[i1-1] == word2[i2-1]:
                    dp[i1][i2] = 1 + dp[i1-1][i2-1]
                else:
                    dp[i1][i2] = max(dp[i1-1][i2], dp[i1][i2-1])

        longest_seq = dp[l1][l2]

        return (l1 - longest_seq) + (l2 - longest_seq)
