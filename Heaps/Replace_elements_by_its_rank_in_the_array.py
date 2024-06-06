#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def replaceWithRank(self, N, arr):
        # Code here
        dummy_array = arr.copy()
        dummy_array.sort()
        order_map = {}
        n = len(dummy_array)
        
        rank = 1
        
        order_map[dummy_array[0]] = rank
        
        for i in range(1, n):
            if (dummy_array[i] == dummy_array[i-1]):
                order_map[dummy_array[i]] = rank
            else:
                rank += 1
                order_map[dummy_array[i]] = rank
        
        for i in range(n):
            arr[i] = order_map[arr[i]]
            
        return arr
        
        
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.replaceWithRank(N, arr)
        for rank in res:
            print(rank, end = ' ')
        print()
# } Driver Code Ends
