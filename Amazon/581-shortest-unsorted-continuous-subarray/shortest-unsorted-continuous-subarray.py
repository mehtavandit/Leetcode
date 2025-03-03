class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Step 1: Find the left_index
        left_index = -1
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                left_index = i
                break
        
        # If no such index exists, the array is already sorted
        if left_index == -1:
            return 0
        
        # Step 2: Find the right_index
        right_index = -1
        for i in range(n - 1, 0, -1):
            if nums[i] < nums[i - 1]:
                right_index = i
                break
        
        # Step 3: Find the min and max in the unsorted subarray
        min_val = min(nums[left_index:right_index + 1])
        max_val = max(nums[left_index:right_index + 1])
        
        # Step 4: Expand the left index to the left if needed
        while left_index > 0 and nums[left_index - 1] > min_val:
            left_index -= 1
        
        # Step 5: Expand the right index to the right if needed
        while right_index < n - 1 and nums[right_index + 1] < max_val:
            right_index += 1
        
        return right_index - left_index + 1
