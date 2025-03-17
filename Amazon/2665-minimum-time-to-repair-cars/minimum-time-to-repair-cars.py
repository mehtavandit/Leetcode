import math

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left = 1
        right = cars * cars * ranks[0]

        def repair(mid):
            total_cars = 0
            for rank in ranks:
                total_cars += int(math.sqrt(mid / rank))
                if total_cars >= cars:
                    return True

            return False
        
        
        while left < right:
            mid = (left + right) // 2
            if repair(mid):
                right = mid
            else:
                left = mid + 1
        return left