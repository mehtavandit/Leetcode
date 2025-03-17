class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        # if len(arr) < 2:
        #     return arr[0]

        # result = 0

        # percent = int (len(arr) * 0.25)

        # count = Counter(arr)

        # for key, count in count.items():
        #     if count > percent:
        #         result = key

        # return result

        n = len(arr)
        percent = n * 0.25
        
        
        i = 0
        while i < n:
            count = 1
            while i + 1 < n and arr[i] == arr[i + 1]:
                i += 1
                count += 1
            
            if count > percent:
                return arr[i]
            
            i += 1
            
        return -1