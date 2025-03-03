class Solution:
    def reverse(self, x: int) -> int:
        res = 0

        if x < 0:
            string = str(x)[1:]
            reversed_string = string[::-1]
            res = int(reversed_string) * -1
        else:
            string = str(x)
            reverse_string = string[::-1]
            res = int(reverse_string)

        if res > 2**31 - 1 or res < -2**31:
            return 0
        
        return res