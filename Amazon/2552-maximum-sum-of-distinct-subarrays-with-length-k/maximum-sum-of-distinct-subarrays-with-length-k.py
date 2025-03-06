class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        begin = 0
        end = 0
        elements = set()
        current_sum = 0
        max_sum = 0

        for end in range(len(nums)):
            if nums[end] not in elements:
                elements.add(nums[end])
                current_sum += nums[end]

                if end - begin +1 == k:
                    max_sum = max(max_sum, current_sum)

                    current_sum -= nums[begin]
                    elements.remove(nums[begin])
                    begin += 1

            else:
                while nums[begin] != nums[end]:
                    current_sum -= nums[begin]
                    elements.remove(nums[begin])
                    begin += 1

                begin += 1

        return max_sum


        