class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26
        left = 0
        right = 0
        n = len(s)
        max_count = 0
        while right < n:
            freq[ord(s[right]) - ord('A')] += 1
            max_count = max(max_count, freq[ord(s[right]) - ord('A')])

            if (right-left+1) - max_count > k:
                freq[ord(s[left]) - ord('A')] -= 1
                left += 1

            right += 1

        
        return right - left 