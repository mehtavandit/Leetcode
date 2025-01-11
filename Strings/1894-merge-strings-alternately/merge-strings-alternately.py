class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1 = 0
        p2 = 0
        l1 = len(word1)
        l2 = len(word2)

        res = ""

        while p1 < l1 and p2 < l2:
            res = res + word1[p1]
            res = res + word2[p2]
            p1 += 1
            p2 += 1

        while p1 < l1:
            res = res + word1[p1]
            p1 += 1

        while p2 < l2:
            res = res + word2[p2]
            p2 += 1

        return res
