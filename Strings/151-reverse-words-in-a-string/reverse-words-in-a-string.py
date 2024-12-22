class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()

        words = s.split(" ")

        length = len(words)

        for i in range(int(length/2)):
            x = words[i]
            words[i] = words[length - (i+1)]
            words[length - (i+1)] = x


        print(words)
        output = ""

        for i in words:
            if i != " " and len(i) > 0:
                output = output + i + " "

        output = output.strip()

        return output