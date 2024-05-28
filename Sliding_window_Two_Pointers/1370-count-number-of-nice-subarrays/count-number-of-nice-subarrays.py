class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums2 = []

        for i in nums:
            if i%2 == 0:
                nums2.append(0)
            else:
                nums2.append(1)

        def findSum(nums, goal):
            if goal < 0:
                return 0

            l = 0
            r = 0
            sum_ = 0
            count = 0
            n = len(nums)

            while (r<n):
                sum_ += nums[r]%2
                while (sum_ > goal):
                    sum_ -= nums[l]%2
                    l += 1
                count += r-l+1
                r += 1
            return count

        main_count = findSum(nums2, k) - findSum(nums2, k-1)
        return main_count