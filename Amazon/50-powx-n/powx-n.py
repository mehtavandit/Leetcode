class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def exponent(x,n):
            if n==0:
                return 1
            
            if n<0:
                return 1.0 / exponent(x, -1 * n)
            
            if n%2 == 0:
                return exponent(x*x, n//2)
            else:
                return x * exponent(x*x, (n-1) // 2)
        
        return exponent(x,n)