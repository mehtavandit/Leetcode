class Solution:
    def check(self, nums: List[int]) -> bool:
        
        size = len(nums)
        
        counter = 0

        for i in range(0, size):

            if nums[i] > nums[(i+1)%size]:
                counter += 1

            if counter > 1:
                return False

        return True 

