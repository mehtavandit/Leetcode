class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n1, n2 = len(nums1), len(nums2)

        left = 0
        right = n1

        while left <= right:
            i = (left + right) // 2
            j = (n1 + n2 + 1) //2 - i

            max_left1 = float('-inf') if i == 0 else nums1[i - 1]
            min_right1 = float('inf') if i == n1 else nums1[i]
            
            max_left2 = float('-inf') if j == 0 else nums2[j - 1]
            min_right2 = float('inf') if j == n2 else nums2[j]
            
            if max_left1 <= min_right2 and max_left2 <= min_right1:
                if (n1 + n2) % 2 == 1:
                    return max(max_left1, max_left2)
                else:
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
            elif max_left1 > min_right2:
                right = i - 1
            else:
                left = i + 1
        # n1 = len(nums1)
        # n2 = len(nums2)
        # result = []

        # p1 = 0
        # p2 = 0

        # while (p1 < n1) and (p2<n2):
        #     if nums1[p1] <= nums2[p2]:
        #         result.append(nums1[p1])
        #         p1 += 1
        #     else:
        #         result.append(nums2[p2])
        #         p2 += 1
        

        # while p1 < n1:
        #     result.append(nums1[p1])
        #     p1 += 1

        # while p2 < n2:
        #     result.append(nums2[p2])
        #     p2 += 1

        # n = len(result)

        # if n % 2 == 1:
        #     return result[n // 2]

        # mid1, mid2 = n // 2 - 1, n // 2
        # return (result[mid1] + result[mid2]) / 2