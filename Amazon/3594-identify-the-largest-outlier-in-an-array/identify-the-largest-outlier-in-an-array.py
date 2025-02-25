from itertools import combinations

class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        # n = len(nums)
        # sum_counts = {}

        # for subset in combinations(nums, n-2): #O(n2) since we are iterating over size of n-2
        #     subset_sum = sum(subset) # O(n)
        #     sum_counts[subset_sum] = sum_counts.get(subset_sum, 0) + 1

        # outliers = []
        # for num in nums:
        #     if num not in sum_counts:
        #         outliers.append(num)

        # return max(outliers)

        max_outlier = float('-inf')

        total = sum(nums)

        num_counts = defaultdict(int)

        for num in nums:
            num_counts[num] += 1

        for num in num_counts.keys():
            y = total - 2 * num

            if y in num_counts:
                if y!=num or num_counts[y] > 1:
                    max_outlier = max(max_outlier, y)

        return max_outlier 

    
