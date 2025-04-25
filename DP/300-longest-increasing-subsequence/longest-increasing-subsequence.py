class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        #Memo

        # dp = [ [-1 for _ in range(n+1)] for _ in range(n)]
        # def rec(ind, prev_ind):
        #     if ind == n:
        #         return 0

        #     if dp[ind][prev_ind+1] != -1:
        #         return dp[ind][prev_ind+1]

        #     length = 0 + rec(ind+1, prev_ind)

        #     if prev_ind == -1 or nums[ind] > nums[prev_ind]:
        #         length = max( length , 1 + rec(ind+1, ind))

        #     dp[ind][prev_ind+1] = length
        #     return length


        # return rec(0, -1)

        # dp = [ [0 for _ in range(n+1)] for _ in range(n+1)]

        # for ind in range(n-1, -1, -1):
        #     for prev_ind in range(ind-1, -2, -1):
        #         length = 0 + dp[ind+1][prev_ind+1]

        #         if prev_ind == -1 or nums[ind] > nums[prev_ind]:
        #             length = max(length, 1 + dp[ind+1][ind+1]) #prev index is now ind, and since it is shfited by +1, so ind+1

        #         dp[ind][prev_ind +1] = length

        # return dp[0][0]

        #O(n) solution

        dp = [1] * n

        for ind in range(0, n):
            for prev in range(0, ind):
                if nums[prev] < nums[ind]:
                    dp[ind] = max(dp[ind], 1 + dp[prev])

        return max(dp)