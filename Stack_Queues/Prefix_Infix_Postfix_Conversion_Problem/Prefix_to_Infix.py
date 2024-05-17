#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def preToInfix(self, pre_exp):
        # Code here
        
        def isOperator(c):
            if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
                return True
            else:
                return False
                
                
        stack = []
        
        i = len(pre_exp) - 1
        
        while i>=0:
            
            if not isOperator(pre_exp[i]):
                stack.append(pre_exp[i])
                i -= 1
            else:
                exp = "(" + stack.pop() + pre_exp[i] + stack.pop() + ")"
                stack.append(exp)
                i -=1
                
        return stack.pop()
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        prefix = input()
        ob = Solution()
        res = ob.preToInfix(prefix)
        print(res)
# } Driver Code Ends
