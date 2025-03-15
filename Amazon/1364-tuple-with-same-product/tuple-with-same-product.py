class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_map = {}

        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                product = nums[i] * nums[j]

                if product not in product_map:
                    product_map[product] = []
                product_map[product].append((nums[i], nums[j]))

        result = 0

        for product in product_map:
            pairs = product_map[product]
            count = len(pairs)
            if count > 1:
                result += (count * (count - 1) // 2) * 8
            
        return result