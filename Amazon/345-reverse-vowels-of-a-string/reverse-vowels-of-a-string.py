class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

        left = 0
        right = len(s) - 1

        s = list(s)

        while left < right:
            if s[left] in vowels and s[right] in vowels:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            
            if s[left] not in vowels:
                left += 1
            
            if s[right] not in vowels:  
                right -= 1

        return ''.join(s)
