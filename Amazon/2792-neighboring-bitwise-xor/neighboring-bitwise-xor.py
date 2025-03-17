class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)
        xorr_sum = 0

        for i in derived:
            xorr_sum ^= i

        return xorr_sum == 0