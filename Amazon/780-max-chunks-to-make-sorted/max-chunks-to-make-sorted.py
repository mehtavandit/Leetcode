class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max_so_far = -float('inf')
        chunks = 0
        
        for i, num in enumerate(arr):
            # Update the max value encountered so far
            max_so_far = max(max_so_far, num)
            
            # If the max_so_far equals the current index, we can form a chunk
            if max_so_far == i:
                chunks += 1
        
        return chunks