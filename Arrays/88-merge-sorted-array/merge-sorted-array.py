class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l1 = len(nums1)
        l2 = len(nums2)
        index = 0

        for i in range(l1-n, l1):
            nums1[i] = nums2[index]
            index += 1

        nums1.sort()

