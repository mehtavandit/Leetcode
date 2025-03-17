class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # result = [-1, -1]

        # n = len(nums)

        # if n == 0:
        #     return result

        # for i in range(n):
        #     if nums[i] == target:
        #         result[0] = i
        #         break

        # for i in range(n-1, -1, -1):
        #     if nums[i] == target:
        #         result[1] = i
        #         break

        # return result

        n = len(nums)

        left = 0
        right = n-1

        result = [-1, -1]
        res = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                res = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        result[0] = res

        left = 0
        right = n-1
        res = -1

        while (left<=right):
            mid = (left + right) // 2

            if nums[mid] == target:
                res = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        result[1] = res

        return result
