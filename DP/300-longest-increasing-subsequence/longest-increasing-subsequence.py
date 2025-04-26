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

        #O(n) space solution and printing LIS

        # dp = [1] * n
        # hash_arr = [1] * n
        # maximum = 1
        # lastIndex = 0

        # for ind in range(0, n):
        #     hash_arr[ind] = ind
        #     for prev in range(0, ind):
        #         if nums[prev] < nums[ind] and 1 + dp[prev] > dp[ind]:
        #             dp[ind] = 1 + dp[prev]
        #             hash_arr[ind] = prev

        #     if dp[ind] > maximum:
        #         maximum = dp[ind]
        #         lastIndex = ind

        # result = []

        # while (hash_arr[lastIndex] != lastIndex):
        #     result.append(nums[lastIndex])
        #     lastIndex = hash_arr[lastIndex]

        # result.append(nums[lastIndex])

        # print(result)

        #O(nlogn)

        temp = [nums[0]]
        length = 1

        for i in range(1, n):
            if nums[i] > temp[-1]:
                temp.append(nums[i])
                length += 1
            else:
                ind = bisect_left(temp, nums[i])
                temp[ind] = nums[i]

        return length