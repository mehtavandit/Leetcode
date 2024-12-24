class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = [0] * 128
        l2 = [0] * 128

        for i in s:
            value = ord(i)
            l1[value] += 1


        for i in t:
            value = ord(i)
            l2[value] += 1

        for i in range(len(l1)):
            if l1[i] != l2[i]:
                return False

        return True
