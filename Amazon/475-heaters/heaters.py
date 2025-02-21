class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        left = 0
        right = int(1e9)

        def can_work(radius):
            house_index, num_houses = 0, len(houses)
            heater_index, num_heaters = 0, len(heaters)

            while house_index < num_houses:
                if heater_index >= num_heaters:
                    return False

                min_range = heaters[heater_index] - radius
                max_range = heaters[heater_index] + radius

                if houses[house_index] < min_range:
                    return False
                
                if houses[house_index] > max_range:
                    heater_index += 1
                else:
                    house_index += 1

            return True 

        while left < right:
            mid = (left + right) // 2

            if can_work(mid):
                right = mid
            else:
                left = mid + 1

        return left