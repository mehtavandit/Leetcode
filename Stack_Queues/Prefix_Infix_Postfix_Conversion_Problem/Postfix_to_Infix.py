#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def postToInfix(self, postfix):
        # Code here
        def isOperator(c):
            if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
                return True
            else:
                return False
                
                
        stack = []
        
        n = len(postfix)
        
        for i in range(n):
            
            if not isOperator(postfix[i]):
                stack.append(postfix[i])
                i -= 1
            else:
                exp1 = stack.pop()
                exp2 = stack.pop()
                exp = "(" + exp2 + postfix[i] + exp1 +")"
                stack.append(exp)
                i -=1
                
        return stack.pop()

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        postfix = input()
        ob = Solution()
        res = ob.postToInfix(postfix)
        print(res)
# } Driver Code Ends
