class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def canSplit(maxSum):
            current_sum = 0
            split = 1

            for num in nums:
                if current_sum + num > maxSum:
                    split += 1
                    current_sum = num
                    if split > k:
                        return False
                else:
                    current_sum += num

            return True


        left = max(nums)
        right = sum(nums)
        result = right

        while left <= right:
            mid = (left + right) // 2

            if canSplit(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result