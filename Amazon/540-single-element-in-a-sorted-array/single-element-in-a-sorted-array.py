# XOR has a unique property: 
# \U0001d44e
# ⊕
# \U0001d44e
# =
# 0
# a⊕a=0 and 
# \U0001d44e
# ⊕
# 0
# =
# \U0001d44e
# a⊕0=a.
# Since every element except one appears twice, XOR-ing all elements will cancel out the duplicate elements and leave us with the single non-duplicate element.


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # result = 0

        # for num in nums:
        #     result ^= num

        # return result

        n = len(nums)
        low = 0
        high = n - 1

        while low < high:

            mid = (low + high) // 2

            if mid % 2 == 1: #bcoz a pair should alwasy start at odd index
                mid -= 1

            if nums[mid] == nums[mid+1]:
                low = mid + 2
            else:
                high = mid

        return nums[low]