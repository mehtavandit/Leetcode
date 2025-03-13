class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        # string_arr = list(s)
        # for i in range(len(shifts)):
        #     for c in range(i+1):
        #         string_arr[c] = chr((ord(string_arr[c]) - ord('a') + shifts[i]) % 26 + ord('a'))

        # return "".join(string_arr) TLE

        for i in range(len(shifts) - 2, -1, -1):
            shifts[i] += shifts[i+1]

        def shift_letter(letter, position):
            return chr((ord(letter) - ord('a') + position) % 26 + ord('a'))



        result = ""
        for char, shift in zip(s, shifts):
            result += shift_letter(char, shift)

        return result
