class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller_elements = []
        equal_elements = []
        greater_elements = []

        for i in nums:
            if i<pivot:
                smaller_elements.append(i)
            elif i>pivot:
                greater_elements.append(i)
            else:
                equal_elements.append(i)

        result = smaller_elements + equal_elements + greater_elements
        return result