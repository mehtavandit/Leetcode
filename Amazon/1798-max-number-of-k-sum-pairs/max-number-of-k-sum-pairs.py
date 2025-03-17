class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        mapping = defaultdict(int)
        count = 0

        for i in range(len(nums)):
            current = nums[i]
            complement = k - nums[i]

            if complement in mapping and mapping[complement] > 0:
                mapping[complement] -= 1
                count += 1
            
            else:
                mapping[current] += 1

        return count