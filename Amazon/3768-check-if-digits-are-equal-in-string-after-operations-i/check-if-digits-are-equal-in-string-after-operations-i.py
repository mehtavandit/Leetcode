class Solution:
    def hasSameDigits(self, s: str) -> bool:
        sequence = list(s)

        while len(sequence) > 2:
            new_sequence = []

            for i in range(len(sequence)-1):
                element1 = int(sequence[i])
                element2 = int(sequence[i+1])

                number = (element1 + element2) % 10
                new_sequence.append(number)

            sequence = new_sequence

        return True if sequence[0] == sequence[1] else False