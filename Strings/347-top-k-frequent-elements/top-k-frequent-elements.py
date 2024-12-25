class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_map = {}

        result = []

        for i in nums:
            if i in my_map:
                my_map[i] += 1
            else:
                my_map[i] = 1

        sorted_items = sorted(my_map.items(), key = lambda x : x[1], reverse=True)
        
        for i in range(k):
            result.append(sorted_items[i][0])  # Take the element (not the frequency)
        
        return result