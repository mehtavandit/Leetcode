class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canCarry(capacity):
            days_needed = 1

            current_weight = 0

            for w in weights:
                if current_weight + w > capacity:
                    days_needed += 1
                    current_weight = w

                    if days_needed > days:
                        return False
                else:
                    current_weight += w

            return True


        left = max(weights)
        right = sum(weights)

        while left<=right:

            k = (left + right) // 2

            if canCarry(k):
                right = k - 1
            else:
                left = k + 1

        return left
