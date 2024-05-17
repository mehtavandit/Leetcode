#User function Template for python3


class Solution:
    
    #Function to convert an infix expression to a postfix expression.
    def InfixtoPostfix(self, exp):
        
        def precedence(c):
            if c == '^':
                return 3
            elif c == '*' or c == '/':
                return 2
            elif c == '+' or c == '-':
                return 1
            else:
                return -1
                
        def associativity(c):
            # if c in ['^']:
            #     return 'R'
            return 'L'
            
        result = []
        stack = []
        
        for i in exp:
            
            if ('a'<= i <='z') or ('A'<= i <='Z') or ('0'<= i <='9'):
                result.append(i)
            elif i == '(':
                stack.append(i)
            elif i == ')':
                while stack and stack[-1] != '(':
                    result.append(stack.pop())
                stack.pop()
            else:
                while stack and (precedence(i) < precedence(stack[-1]) or (precedence(i) == precedence(stack[-1]) and associativity(i) == 'L')):
                    result.append(stack.pop())
                stack.append(i)
                
        while stack:
            result.append(stack.pop())
            
        main_result = ''.join(result)
        
        return main_result
                
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        exp = str(input())
        ob=Solution()
        print(ob.InfixtoPostfix(exp))
# } Driver Code Ends
