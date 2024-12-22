class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len1 = len(haystack)
        len2 = len(needle)

        for i in range(0, (len1 - len2)+1):
            substring = haystack [i: i+len2]

            if (substring == needle):
                return i


        return -1

