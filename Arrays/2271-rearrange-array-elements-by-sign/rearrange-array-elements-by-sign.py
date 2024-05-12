class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        positive_numbers = []
        negative_numbers = []

        for i in nums:
            if i>0:
                positive_numbers.append(i)
            else:
                negative_numbers.append(i)

        counter = 1
        first_pointer = 0
        second_pointer = 0


        for i in range(0,n,2):
            first_element = positive_numbers[first_pointer]
            second_element = negative_numbers[second_pointer]

            nums[i] = first_element
            nums[i+1] = second_element

            first_pointer += 1
            second_pointer += 1

        return nums
