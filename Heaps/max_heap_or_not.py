
class Solution:
    def isMaxHeap(self,arr,n):
        # Your code goes here
        for i in range(n):
            lchild = 2*i+1
            rchild = 2*i+2
            
            if lchild < n:
                if arr[lchild] > arr[i]:
                    return False
                
            if rchild < n:
                if arr[rchild] > arr[i]:
                    return False
                
        
        return True



#{ 
 # Driver Code Starts
if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]
        ob=Solution()
        print(int(ob.isMaxHeap(arr,n)))
# } Driver Code Ends
