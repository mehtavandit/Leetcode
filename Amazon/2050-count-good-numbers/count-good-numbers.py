class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        def expo(number, raise_to):
            if raise_to == 0:
                return 1
            elif raise_to %2 == 0:
                return expo(number ** 2 % MOD, raise_to // 2) 
            return number * expo(number, raise_to - 1) % MOD

        return 5 ** (n % 2) * expo(20, n//2) % MOD