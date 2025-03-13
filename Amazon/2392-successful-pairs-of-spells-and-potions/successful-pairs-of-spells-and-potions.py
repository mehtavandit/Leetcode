from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # Sort the potions array to enable binary search
        potions.sort()
        
        def binary_search(potions, target):
            # Custom binary search to find the first potion >= target
            left, right = 0, len(potions)
            while left < right:
                mid = (left + right) // 2
                if potions[mid] >= target:
                    right = mid  # Narrow down to the left part
                else:
                    left = mid + 1  # Narrow down to the right part
            return left
        
        result = []
        
        for spell in spells:
            # Calculate the target value which is success / spell
            target = success / spell
            # Use binary search to find the smallest index where potion >= target
            index = binary_search(potions, target)
            # The number of valid potions is from index to the end of the potions array
            result.append(len(potions) - index)
        
        return result
