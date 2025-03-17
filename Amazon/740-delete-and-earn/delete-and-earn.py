class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        max_num = max(nums)

        freq = [0] * (max_num + 1)

        for num in nums:
            freq[num] += num

        print(freq)

        dp = [0] * (max_num+1)
        dp[0] = 0
        dp[1] = freq[1]

        for i in range(2, max_num+1):
            dp[i] = max(dp[i-1], dp[i-2] + freq[i])

        return dp[max_num]
