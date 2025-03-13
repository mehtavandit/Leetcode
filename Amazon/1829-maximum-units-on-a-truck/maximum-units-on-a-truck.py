class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x : x[1], reverse = True)

        total_units = 0

        i=0
        while truckSize>=0 and i<len(boxTypes):
            y = boxTypes[i]
            if y[0] <= truckSize:
                units = y[0] * y[1]
                total_units += units
                truckSize -= y[0]
            else:
                units = truckSize * y[1]
                total_units += units
                truckSize -= y[0]
            i += 1

        return total_units