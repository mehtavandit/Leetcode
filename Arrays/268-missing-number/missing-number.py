class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max = -99999

        n = len(nums)

        sum = 0

        for i in range(n+1):
            sum = sum + i

        array_sum = 0

        for i in range(n):
            array_sum = array_sum + nums[i]

        return sum - array_sum