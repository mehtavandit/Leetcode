class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        dp = [-1] * n

        def isPalindrome(subs):
            return subs == subs[::-1]

        def rec(i):
            if i == n:
                return 0

            if dp[i] != -1:
                return dp[i]

            min_cost = float('inf')

            for j in range(i, n):
                if isPalindrome(s[i:j+1]):
                    cost = 1 + rec(j+1)
                    min_cost = min(min_cost, cost)

            dp[i] = min_cost
            return dp[i]

        return rec(0) - 1
