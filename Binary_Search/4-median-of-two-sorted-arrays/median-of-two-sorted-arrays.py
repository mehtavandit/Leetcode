class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        result = []

        p1 = 0
        p2 = 0

        while (p1 < n1) and (p2<n2):
            if nums1[p1] <= nums2[p2]:
                result.append(nums1[p1])
                p1 += 1
            else:
                result.append(nums2[p2])
                p2 += 1
        

        while p1 < n1:
            result.append(nums1[p1])
            p1 += 1

        while p2 < n2:
            result.append(nums2[p2])
            p2 += 1

        n = len(result)

        if n % 2 == 1:
            return result[n // 2]

        mid1, mid2 = n // 2 - 1, n // 2
        return (result[mid1] + result[mid2]) / 2