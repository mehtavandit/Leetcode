class Solution:
    def countAndSay(self, n: int) -> str:
        current = "1"

        for _ in range(n-1):
            next_seq = ""
            count = 1

            for i in range(1, len(current)):
                if current[i] == current[i-1]:
                    count+=1
                else:
                    next_seq += str(count) + current[i-1]
                    count = 1

            next_seq += str(count) + current[-1]

            current = next_seq

        return current