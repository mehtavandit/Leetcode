class Solution:
    def arrangeCoins(self, n: int) -> int:
        # complete_levels = 0
        # total_coins = n

        # for i in range(n):
        #     if total_coins >= i+1:
        #         complete_levels += 1
        #     total_coins -= (i+1)

        # return complete_levels

        # the above takes O(n)

        left, right = 0, n

        while left <= right:
            mid = (left + right) // 2

            coins_used = (mid * (mid+1)) // 2

            if coins_used == n:
                return mid
            elif coins_used < n:
                left = mid + 1
            else:
                right = mid - 1

        return right