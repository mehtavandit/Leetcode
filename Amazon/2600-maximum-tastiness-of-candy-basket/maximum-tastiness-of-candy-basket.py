class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price = sorted(price)

        maxDiff = abs(price[-1] -  price[0])

        def checkPrice(mid):
            candiesInBasket = 1
            lastCandyIndex = 0

            for i in range(1, len(price)):
                if price[i] - price[lastCandyIndex] >= mid:
                    lastCandyIndex = i
                    candiesInBasket += 1

            if candiesInBasket >= k:
                return True
            
            return False

        left = 0
        right = maxDiff
        ans = 0

        while left <= right:
            mid = (left + right) // 2

            if checkPrice(mid):
                ans = mid
                left = mid + 1 #we need to maximize it
            else:
                right = mid -1

        return ans