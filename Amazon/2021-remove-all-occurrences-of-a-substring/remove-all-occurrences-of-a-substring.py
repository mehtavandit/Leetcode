class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        n = len(s)
        m = len(part)

        while part in s:
            index = s.find(part)

            s = s[:index] + s[index+m:]

        return s