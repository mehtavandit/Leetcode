class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        mapping = defaultdict(int)
        l = 0
        r = 0
        max_count = 0
        n = len(fruits)

        while r < n:
            mapping[fruits[r]] += 1

            while len(mapping) > 2:
                mapping[fruits[l]] -= 1
                if mapping[fruits[l]] == 0:
                    del mapping[fruits[l]]
                l += 1

            max_count = max(max_count, r-l+1)
            r += 1

        return max_count
