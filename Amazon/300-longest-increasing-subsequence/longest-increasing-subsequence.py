class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []

        def binary_search(arr, n):
            l = 0
            r = len(arr) - 1

            while (l <= r):
                mid = (l+r) // 2

                if arr[mid] == n:
                    return mid
                elif res[mid] > n:
                    r = mid - 1
                else:
                    l = mid + 1

            return l



        for n in nums:
            if not res or res[-1] < n:
                res.append(n)
            else:
                idx = binary_search(res, n)
                res[idx] = n

        
        return len(res)
