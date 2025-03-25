class Solution:
    def countPrimes(self, n: int) -> int:
        
        if n<=1:
            return 0
        
        is_prime = [True] * n

        is_prime[0] = is_prime[1] = False

        p = 2

        while p*p < n:
            if is_prime[p]:
                for i in range(p*p, n, p):
                    is_prime[i] = False
            
            p += 1

        count = 0

        for i in range(len(is_prime)):
            if is_prime[i] == True:
                count += 1

        return count