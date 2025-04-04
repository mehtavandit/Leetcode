class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        n = len(nums)
        #Memoization
        # dp = [ [-1 for _ in range(target+1)] for _ in range(n) ]

        # def rec(index, target):
        #     if target == 0:
        #         return True

        #     if index == 0:
        #         return True if nums[index] == target else False

        #     if dp[index][target] != -1:
        #         return dp[index][target]

        #     notTake = rec(index - 1, target)
        #     take = False

        #     if nums[index] <= target:
        #         take = rec(index-1, target - nums[index])

        #     dp[index][target] = notTake or take
        #     return dp[index][target]

        # return rec(n-1, total // 2)

        #Tabulation

        dp = [ [False for _ in range(target+1)] for _ in range(n) ]

        for i in range(n):
            dp[i][0] = True

       

        if nums[0] <= target:
            dp[0][nums[0]] = True

        for index in range(1, n):
            for target_ in range(1, target+1):
                notTake = dp[index-1][target_]
                take = False

                if nums[index] <= target_:
                    take = dp[index-1][target_ - nums[index]]

                dp[index][target_] = notTake or take


        return dp[n-1][target]





