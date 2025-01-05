# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()

        peak_index = self.find_peak(1, length-2, mountainArr)

        index1 = self.bs(0, peak_index, target, mountainArr)

        if index1 != -1:
            return index1

        index2 = self.rbs(peak_index + 1, length - 1, target, mountainArr)

        if index2 != -1:
            return index2

        return -1





    def find_peak(self, left, right, mountainArr):
        while left < right:
            mid = (left + right) // 2

            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                left = mid + 1
            else:
                right = mid
                    
        return left


    def bs(self, left, right, target, mountainArr):
            
        while left <= right:
            mid = (left + right) // 2
                
            value = mountainArr.get(mid)
                
            if value == target:
                return mid
            elif value < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

    def rbs(self, left, right, target, mountainArr):
            
        while left <= right:
            mid = (left + right) // 2
                
            value = mountainArr.get(mid)
                
            if value == target:
                return mid
            elif value > target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
