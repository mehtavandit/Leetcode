class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # res = [-1] * n

        # for i in range(n):
        #     for j in range(1,n):
        #         next_index = (i+j) % n
        #         if nums[next_index] > nums[i]:
        #             res[i] = nums[next_index]
        #             break
        
        # return res

        # TC :- O(n2) not good

        n = len(nums)
        stack = []
        res = [-1] * n

        for i in range(2*n):
            while stack and nums[i%n] > nums[stack[-1]]:
                res[stack.pop()] = nums[i%n]
            if i<n:
                stack.append(i)

        return res