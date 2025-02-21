class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def sum_of_digits(n):
            string = str(n)

            total = 0

            for letter in string:
                total += int(letter)

            return total
        
        digit_sum_map = {}

        for index, num in enumerate(nums):
            s = sum_of_digits(num)

            if s not in digit_sum_map:
                digit_sum_map[s] = []
            digit_sum_map[s].append(index)


        max_result = -1

        for indices in digit_sum_map.values():
            if len(indices) > 1:
                values = [nums[i] for i in indices]
                values.sort(reverse = True) #sorting in desceding order
                max_result = max(max_result, values[0] + values[1])

        return max_result