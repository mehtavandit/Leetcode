class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        number_to_letters = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        ans = ['']

        for digit in digits:

            letters = number_to_letters[int(digit) - 2]

            ans = [prefix + letter for prefix in ans for letter in letters]

        
        return ans

