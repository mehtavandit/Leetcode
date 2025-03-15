class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))

        last_occurence = {int(digit): i for i, digit in enumerate(digits)}

        for i, digit in enumerate(digits):
            for d in range(9, int(digit), -1):
                if d in last_occurence and last_occurence[d] > i:
                    digits[i], digits[last_occurence[d]] = digits[last_occurence[d]], digits[i]

                    return int(''.join(digits))

        return num