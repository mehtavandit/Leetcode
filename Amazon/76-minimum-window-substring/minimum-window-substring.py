class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)

        counter_t = Counter(t)
        counter_s = defaultdict(int)
        minlen = float('inf')
        startIndex = -1
        l = 0
        r = 0
        required = len(counter_t)
        formed = 0

        while r < m:
            char = s[r]
            if char in counter_t:
                counter_s[char] += 1
                if counter_s[char] == counter_t[char]:
                    formed += 1

            while formed == required:
                if r-l+1 < minlen:
                    minlen = r-l+1
                    startIndex = l

                left_char = s[l]
                if left_char in counter_t:
                    counter_s[left_char] -= 1
                    if counter_s[left_char] < counter_t[left_char]:
                        formed -=1

                l += 1

            r += 1


        if startIndex == -1:
            return ""
        return s[startIndex:startIndex + minlen]
