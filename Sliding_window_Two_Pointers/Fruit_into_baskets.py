#User function Template for python3

class Solution:
    def sumSubarrayMins(self, N, fruits):
        # Code here
        
        l = 0
        r = 0
        max_length = 0
        basket = {}
        
        while r < N:
            if fruits[r] in basket:
                basket[fruits[r]] += 1
            else:
                basket[fruits[r]] = 1
                
            if len(basket) > 2:
                while len(basket) > 2:
                    basket[fruits[l]] -= 1
                    if basket[fruits[l]] == 0:
                        del basket[fruits[l]]
                    l += 1
                    
            if len(basket) <= 2:
                max_length = max(max_length, r - l + 1)
            r += 1
            
        return max_length


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range (t):
        N = int(input())
        fruits = list(map(int,input().split()))
        ob = Solution()
        res = ob.sumSubarrayMins(N, fruits)
        print(res)
# } Driver Code Ends
