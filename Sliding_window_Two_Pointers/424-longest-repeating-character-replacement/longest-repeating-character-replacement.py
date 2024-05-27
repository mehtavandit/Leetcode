class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        n = len(s)
        max_length = 0
        max_frequency = 0

        capital_letters = {chr(65 + i): 0 for i in range(26)}

        while(right<n):
            capital_letters[s[right]] += 1
            max_frequency = max(max_frequency, capital_letters[s[right]])
            if ((right-left+1) - max_frequency > k ):
                capital_letters[s[left]] -= 1
                left += 1

            if ((right-left+1) - max_frequency <= k):
                max_length = max(max_length, right-left+1)

            right += 1

        return max_length