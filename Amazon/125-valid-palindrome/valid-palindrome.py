class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        string = ""

        for char in s:
            if char.isalnum():
                string += char

        left = 0
        right = len(string) - 1

        while (left <= right):
            if string[left] != string[right]:
                return False
            left += 1
            right -=1

        return True