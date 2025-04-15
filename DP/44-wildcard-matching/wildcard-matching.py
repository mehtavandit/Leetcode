class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        l1 = len(p) #p
        l2 = len(s) #s

        dp = [ [-1 for _ in range(l2)] for _ in range(l1)]

        def rec(i1 , i2):
            if i1 < 0 and i2 < 0:
                return True

            if i1 < 0 and i2 >= 0:
                return False

            if i2<0 and i1 >= 0:
                for j in range(i1+1):
                    if p[j] != '*':
                        return False

                return True

            if dp[i1][i2] != -1:
                return dp[i1][i2]

            if p[i1] == s[i2] or p[i1] == '?':
                dp[i1][i2] =  rec(i1-1, i2-1)
            elif p[i1] == '*':
                dp[i1][i2] = rec(i1-1, i2) or rec(i1, i2-1)
            else:
                dp[i1][i2] = False
                
            return dp[i1][i2]

        return rec(l1-1, l2-1)