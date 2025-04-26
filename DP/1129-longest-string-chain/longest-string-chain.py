class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        n = len(words)
        words.sort(key=len)

        dp = [1] * n

        max_length = 1

        def compare(word1, word2):
            if len(word1) != len(word2) + 1:
                return False

            i = 0
            j = 0

            while i < len(word1):
                if j < len(word2) and word1[i] == word2[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            
            return j == len(word2)

        for ind in range(n):
            for prev in range(ind):
                if compare(words[ind], words[prev]) and 1 + dp[prev] > dp[ind]:
                    dp[ind] = dp[prev] + 1
                max_length = max(max_length, dp[ind])

        return max_length
