class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        c=0
        while nums:
            if len(set(nums))==len(nums):
                return c #we can also use break
            del nums[:3]
            c+=1
        return c