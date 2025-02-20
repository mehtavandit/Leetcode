import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s) #Hashmap, counting each character and returning hashmap for it

        maxHeap = [[-cnt, char]for char, cnt in count.items()] #keeping cnt first bcoz python will heapify on basis of first element, and if it's a tie will use second value

        heapq.heapify(maxHeap) # O(n)

        prev = None
        res = ""

        while maxHeap or prev: #we need most freqeuent one except prev
            
            if prev and not maxHeap:
                return ""
            
            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None

            if cnt!= 0:
                prev = [cnt, char]

        return res
    

         