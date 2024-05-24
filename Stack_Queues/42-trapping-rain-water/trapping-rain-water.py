class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0

        n = len(height)

        left_height = [0] * n
        right_height = [0] * n

        left_height[0] = height[0]
        right_height[n-1] = height[n-1]

        for i in range(1, n):
            left_height[i] = max(left_height[i-1], height[i])

        for i in range(n-2, -1, -1):
            right_height[i] = max(right_height[i+1], height[i])

        for i in range(1, n-1):
            total_water += min(left_height[i], right_height[i]) - height[i]

        return total_water