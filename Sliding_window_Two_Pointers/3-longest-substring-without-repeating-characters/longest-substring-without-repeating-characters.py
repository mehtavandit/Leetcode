class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)
        
        if n == 0:
            return 0

        maxlength = -555
        l = 0
        set_ = set()
        for r in range(n):
            if (s[r] in set_):
                while l < r and s[r] in set_:
                    set_.remove(s[l])
                    l += 1

            set_.add(s[r])
            maxlength = max(maxlength, r-l+1)

        return maxlength
             