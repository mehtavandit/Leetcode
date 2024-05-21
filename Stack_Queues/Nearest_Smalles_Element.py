class Solution:
	# @param A : list of integers
	# @return a list of integers
	def prevSmaller(self, A):
        n = len(A)
        stack = [A[0]]
        res = [-1]*n
        
        for i in range(1, n):
            while stack and stack[-1] >= A[i]:
                stack.pop()
                
            res[i] = stack[-1] if stack else -1
            stack.append(A[i])
            
        return res
