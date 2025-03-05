class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        stack = []

        for num in nums:
            if not stack or num > stack[-1]:
                stack.append(num)
                if len(stack) == 3:
                    return True

            else:
                for i in range(len(stack)):
                    if num <= stack[i]:
                        stack[i] = num
                        break


        return False