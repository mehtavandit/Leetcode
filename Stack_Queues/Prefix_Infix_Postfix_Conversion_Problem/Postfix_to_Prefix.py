#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def postToPre(self, post_exp):
        def isOperator(c):
            if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
                return True
            else:
                return False
                
                
        stack = []
        
        n = len(post_exp)
        
        for i in range(n):
            
            if not isOperator(post_exp[i]):
                stack.append(post_exp[i])
                i -= 1
            else:
                exp1 = stack.pop()
                exp2 = stack.pop()
                exp = post_exp[i] + exp2 + exp1
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
        res = ob.postToPre(postfix)
        print(res)
# } Driver Code Ends
