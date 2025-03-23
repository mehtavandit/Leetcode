from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        if not nums:
            return []

        result = []

        q = deque()

        for i in range(n):
            if q and q[0] < i - k + 1:
                q.popleft()

            while q and nums[q[-1]] < nums[i]:
                q.pop()

            q.append(i)

            if i>=k-1:
                result.append(nums[q[0]])

        return result