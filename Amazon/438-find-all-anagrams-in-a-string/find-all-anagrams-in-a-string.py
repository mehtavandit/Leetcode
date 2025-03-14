class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_arr = [0] * 26
        s_arr = [0] * 26

        result = []

        

        for i in p:
            p_arr[ord(i) - ord('a')] += 1

        l1 = len(s)
        l2 = len(p)

        if l2 > l1:
            return result

        for i in range(l2):
            s_arr[ord(s[i])- ord('a')] += 1

        if s_arr == p_arr:
            result.append(0)

        for i in range(l2, l1):
            s_arr[ord(s[i])- ord('a')] += 1

            s_arr[ord(s[i - l2])- ord('a')] -= 1

            if s_arr == p_arr:
                result.append(i-l2 + 1)

        return result
