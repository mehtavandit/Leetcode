class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = {}
        result = []

        for i in range(0, len(s) - 9):
            string = s[i:i+10]

            if string in seen:
                seen[string] += 1
            else:
                seen[string] = 1


            if seen[string] == 2:
                result.append(string)

        return result