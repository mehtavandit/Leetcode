class Solution:
    def partitionString(self, s: str) -> int:
        count = 1
        seen = set()

        for i in range(len(s)):
            if s[i] not in seen:
                seen.add(s[i])
            else:
                seen = set()
                seen.add(s[i])
                count += 1

        return count
