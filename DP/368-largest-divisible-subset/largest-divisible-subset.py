class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)

        nums.sort()

        dp = [1] * n
        hash_arr = [1] * n
        maximum = 1
        last_index = 0

        for ind in range(n):
            hash_arr[ind] = ind
            for prev in range(ind):
                if nums[ind] % nums[prev] == 0 and 1 + dp[prev] > dp[ind]:
                    dp[ind] = 1 + dp[prev]
                    hash_arr[ind] = prev

            if dp[ind] > maximum:
                maximum = dp[ind]
                last_index = ind

        result = []

        while (hash_arr[last_index] != last_index):
            result.append(nums[last_index])
            last_index = hash_arr[last_index]

        result.append(nums[last_index])

        return result

        
        
        

        
