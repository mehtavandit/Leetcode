class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        st=[nums[-1]]
        ans=[-1]*n
        for i in range(2*n-1,-1,-1):
            while st and st[-1]<=nums[i%n]:
                st.pop()
            if i<n:
                ans[i]=st[-1] if st else -1
            st.append(nums[i%n])
        return ans