class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        l1 = len(str1)
        l2 = len(str2)

        dp = [ [-1 for _ in range(l2+1)] for _ in range(l1+1)]

        for i1 in range(l1+1):
            dp[i1][0] = 0

        for i2 in range(l2+1):
            dp[0][i2] = 0

        for i1 in range(1, l1+1):
            for i2 in range(1, l2+1):
                if str1[i1-1] == str2[i2-1]:
                    dp[i1][i2] = 1 + dp[i1-1][i2-1]
                else:
                    dp[i1][i2] = max(dp[i1-1][i2], dp[i1][i2-1])

        result = []

        i1 = l1
        i2 = l2

        while i1 > 0 and i2 > 0:
            if str1[i1-1] == str2[i2-1]:
                result.append(str1[i1-1])
                i1 -= 1
                i2 -= 1
            elif dp[i1-1][i2] > dp[i1][i2-1]:
                result.append(str1[i1-1])
                i1 -= 1
            else:
                result.append(str2[i2-1])
                i2 -= 1

        while i1 > 0:
            result.append(str1[i1 - 1])
            i1 -= 1

        while i2 > 0:
            result.append(str2[i2 - 1])
            i2 -= 1

        return ''.join(reversed(result))