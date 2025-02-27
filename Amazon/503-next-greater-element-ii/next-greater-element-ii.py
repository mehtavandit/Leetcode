class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n

        for i in range(n):
            for j in range(1,n):
                next_index = (i+j) % n
                if nums[next_index] > nums[i]:
                    res[i] = nums[next_index]
                    break
        
        return res