class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # counter = Counter(nums)

        # more_than_one = [nums for nums, freq in counter.items() if freq > 1]

        # if len(more_than_one) == 0:
        #     return False
        
        # return True

        return len(nums) != len(set(nums))