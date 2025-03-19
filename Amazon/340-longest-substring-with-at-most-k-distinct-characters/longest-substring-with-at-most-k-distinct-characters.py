class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        visited = defaultdict(int)
        l = 0
        n = len(s)
        r= 0
        maxlength = float('-inf')

        while r<n:

            visited[s[r]] += 1

            while len(visited) > k:
                visited[s[l]] -= 1
                if visited[s[l]] == 0:
                    del visited[s[l]]
                l += 1
                
            maxlength = max(maxlength, r - l + 1)
            r+=1

        return maxlength