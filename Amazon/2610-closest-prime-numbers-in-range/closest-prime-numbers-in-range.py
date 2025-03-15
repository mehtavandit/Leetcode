class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        is_prime = [True] * (right+1)

        is_prime[0] = is_prime[1] = False

        p=2

        while p*p <= right:
            if is_prime[p]:
                for i in range(p*p, right+1, p):
                    is_prime[i] = False
            p+=1

        primes = [i for i in range(left, right+1) if is_prime[i]]

        if len(primes) < 2:
            return [-1, -1]
            
        min_gap = float('inf')
        result = [-1, -1]

        for i in range(1, len(primes)):
            gap = primes[i] - primes[i-1]
            if gap < min_gap:
                min_gap = gap
                result = [primes[i-1], primes[i]]


        return result