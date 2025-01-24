import math
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        
        def status(capacity):
            total_stores = 0
            for q in quantities:
                stores_needed = math.ceil(q / capacity)
                total_stores += stores_needed

            return total_stores <= n


        left = 1
        right = max(quantities)
        res = -1

        while left <= right:
            middle = (left + right) // 2
            if status(middle):
                res = middle
                right = middle - 1
            else:
                left = middle + 1


        return res