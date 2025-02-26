class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = -1
        n = len(nums)

        
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break

        
        if pivot == -1:  
            nums.reverse()  
            return

        
        idx = pivot + 1
        for i in range(pivot + 1, n):
            if nums[i] > nums[pivot] and nums[i] <= nums[idx]:
                idx = i

        
        nums[pivot], nums[idx] = nums[idx], nums[pivot]

        
        nums[pivot + 1:] = reversed(nums[pivot + 1:])

        

