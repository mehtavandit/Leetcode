class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = 0
        r = 0
        n = len(s)
        count = 0
        dict_ = {'a':-1, 'b':-1, 'c':-1}

        for i in range(n):
            dict_[s[i]] = i
            count = count + (1+min(dict_['a'], dict_['b'], dict_['c']))

        return count

        

