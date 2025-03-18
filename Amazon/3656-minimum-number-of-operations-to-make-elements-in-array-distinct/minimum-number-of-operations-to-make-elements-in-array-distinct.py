class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        w = nums[::-1]

        c = Counter(w)

        res = 0

        if max(c.values()) == 1:
            return res
        
        while (c and max(c.values()) > 1):
            i = 0

            if len(w) >= 3:
                while (i<3):
                    n = w.pop()
                    c[n] -= 1
                    i += 1
                    if c[n] == 0:
                        del c[n]
            else:
                while (w):
                    n = w.pop()
                    c[n] -= 1
                    if c[n] == 0:
                        del c[n]

            res += 1
        
        return res
