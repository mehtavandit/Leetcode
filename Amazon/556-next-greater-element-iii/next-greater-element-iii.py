class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))

        i = len(digits) - 2

        while i>=0 and digits[i] >= digits[i+1]: #finding the digit that is smaller than digit to it's right
            i -= 1

        if i==-1:
            return -1

        j = len(digits) - 1

        while digits[j] <= digits[i]:
            j -= 1

        digits[i], digits[j] = digits[j], digits[i]

        digits = digits[:i+1] + sorted(digits[i+1:])

        result = int(''.join(digits))
    
        # Step 5: Check for 32-bit integer range
        if result > 2**31 - 1:
            return -1
    
        return result