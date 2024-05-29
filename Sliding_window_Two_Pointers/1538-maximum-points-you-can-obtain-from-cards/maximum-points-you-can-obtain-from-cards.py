class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        lsum = 0
        rsum = 0
        max_sum = 0
        n = len(cardPoints)

        for i in range(k):
            lsum += cardPoints[i]

        max_sum = lsum

        rightindex = n-1

        for i in range(k-1, -1, -1):
            lsum -= cardPoints[i]
            rsum += cardPoints[rightindex]
            sum_ = lsum + rsum
            rightindex -= 1
            max_sum = max(max_sum, sum_)

        return max_sum