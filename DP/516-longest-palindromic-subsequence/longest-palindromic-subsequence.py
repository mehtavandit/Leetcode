class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s1 = s
        s2 = ''.join(reversed(s))

        l1 = len(s1)
        l2 = len(s2)

        # dp = [ [-1 for _ in range(l2+1)] for _ in range(l1+1)]

        # for i1 in range(l1+1):
        #     dp[i1][0] = 0

        # for i2 in range(l2+1):
        #     dp[0][i2] = 0

        # for i1 in range(1, l1+1):
        #     for i2 in range(1, l2+1):
        #         if s1[i1-1] == s2[i2-1]:
        #             dp[i1][i2] = 1 + dp[i1-1][i2-1]
        #         else:
        #             dp[i1][i2] = max(dp[i1-1][i2], dp[i1][i2-1])

        # return dp[l1][l2]

        prev = [0] * (l2+1)

        for i1 in range(1, l1+1):
            curr = [0] * (l2+1)
            for i2 in range(1, l2+1):
                if s1[i1-1] == s2[i2-1]:
                    curr[i2] = 1 + prev[i2-1]
                else:
                    curr[i2] = max(prev[i2], curr[i2-1])

            prev = curr

        return curr[-1]