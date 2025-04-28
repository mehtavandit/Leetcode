class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = [0] + cuts + [n]
        cuts.sort()
        c = len(cuts) - 2

        # dp = [ [-1 for _ in range(c+1)] for _ in range(c+1) ]

        # def rec(i, j):
        #     if i>j:
        #         return 0

        #     if dp[i][j] != -1:
        #         return dp[i][j]

        #     mini = float('inf')

        #     for ind in range(i, j+1):
        #         ans = cuts[j+1] - cuts[i-1] + rec(i, ind-1) + rec(ind+1, j)
        #         mini = min(mini, ans)

        #     dp[i][j] =  mini
        #     return dp[i][j]


        # return rec(1, len(cuts)-2)

        #Tabulation

        dp = [ [0 for _ in range(c+2)] for _ in range(c+2)]

        for i in range(c, 0, -1):
            for j in range(1, c+1):
                if i>j:
                    continue
                
                mini = float('inf')

                for ind in range(i, j+1):
                    ans = cuts[j+1] - cuts[i-1] + dp[i][ind-1] + dp[ind+1][j]
                    mini = min(mini, ans)

                dp[i][j] = mini

        return dp[1][c]