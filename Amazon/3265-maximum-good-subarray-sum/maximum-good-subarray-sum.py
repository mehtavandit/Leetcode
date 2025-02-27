class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # max_sum = float('-inf')

        # n = len(nums)

        # for i in range(n):
        #     for j in range(i+1, n):
        #         if abs(nums[i] - nums[j]) == k:
        #             current_sum = sum(nums[i:j+1])
        #             max_sum = max(max_sum, current_sum)

        # return max_sum if max_sum != float('-inf') else 0

        # TC :- O(n3) getting TLE

        prefix_left = defaultdict(lambda:inf)
        res = -inf
        cur = 0

        for x in nums:
            prefix_left[x] = min(prefix_left[x], cur)
            cur += x

            if x-k in prefix_left:
                res = max(res, cur - prefix_left[x-k])

            if x+k in prefix_left:
                res = max(res, cur - prefix_left[x+k])

        return res if res!=-inf else 0
