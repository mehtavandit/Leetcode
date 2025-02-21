class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        sorted_counter = sorted(count.items(), key = lambda item: -item[1])

        result = ''.join(letter * freq for letter, freq in sorted_counter)

        return result