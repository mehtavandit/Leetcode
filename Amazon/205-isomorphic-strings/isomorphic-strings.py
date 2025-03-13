from collections import defaultdict

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        l1 = len(s)
        l2 = len(t)

        if l1 != l2:
            return False

        mapping_s_to_t = {}
        mapping_t_to_s = {}

        for i in range(l1):
            if s[i] in mapping_s_to_t:
                if mapping_s_to_t[s[i]] != t[i]:
                    return False
            else:
                mapping_s_to_t[s[i]] = t[i]

            if t[i] in mapping_t_to_s:
                if mapping_t_to_s[t[i]] != s[i]:
                    return False
            else:
                mapping_t_to_s[t[i]] = s[i]

        return True
