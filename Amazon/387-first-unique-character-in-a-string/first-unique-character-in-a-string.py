class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)

        print(counter)

        for i in range(len(s)):
            if counter[s[i]] == 1:
                return i

        return -1