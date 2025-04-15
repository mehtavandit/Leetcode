class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        l1 = len(p) #p
        l2 = len(s) #s

        #Memoization
        # dp = [ [-1 for _ in range(l2)] for _ in range(l1)]

        # def rec(i1 , i2):
        #     if i1 < 0 and i2 < 0:
        #         return True

        #     if i1 < 0 and i2 >= 0:
        #         return False

        #     if i2<0 and i1 >= 0:
        #         for j in range(i1+1):
        #             if p[j] != '*':
        #                 return False

        #         return True

        #     if dp[i1][i2] != -1:
        #         return dp[i1][i2]

        #     if p[i1] == s[i2] or p[i1] == '?':
        #         dp[i1][i2] =  rec(i1-1, i2-1)
        #     elif p[i1] == '*':
        #         dp[i1][i2] = rec(i1-1, i2) or rec(i1, i2-1)
        #     else:
        #         dp[i1][i2] = False

        #     return dp[i1][i2]

        # return rec(l1-1, l2-1)

        #Tabulation

        # dp = [ [False for _ in range(l2+1)] for _ in range(l1+1)]

        # dp[0][0] = True

        # for i1 in range(1, l1+1):
        #     if p[i1-1] == "*":
        #         dp[i1][0] = dp[i1-1][0]
        #     else:
        #         break

        # for i1 in range(1, l1+1):
        #     for i2 in range(1, l2+1):
        #         if p[i1-1] == s[i2-1] or p[i1-1] == '?':
        #             dp[i1][i2] = dp[i1-1][i2-1]
        #         elif p[i1-1] == "*":
        #             dp[i1][i2] = dp[i1-1][i2] or dp[i1][i2-1]
        #         else:
        #             dp[i1][i2] = False

        # return dp[l1][l2]

        prev = [False] * (l2 + 1)
        curr = [False] * (l2 + 1)

        prev[0] = True

        for i in range(1, l1 + 1):
            curr[0] = prev[0] if p[i - 1] == '*' else False

            for j in range(1, l2 + 1):
                if p[i - 1] == s[j - 1] or p[i - 1] == '?':
                    curr[j] = prev[j - 1]
                elif p[i - 1] == '*':
                    curr[j] = prev[j] or curr[j - 1]
                else:
                    curr[j] = False

            prev, curr = curr, [False] * (l2 + 1)

        return prev[l2]

