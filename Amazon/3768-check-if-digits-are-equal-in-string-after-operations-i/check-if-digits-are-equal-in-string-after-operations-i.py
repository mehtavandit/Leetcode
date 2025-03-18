class Solution:
    def hasSameDigits(self, s: str) -> bool:
        # sequence = list(s)

        # while len(sequence) > 2:
        #     new_sequence = []

        #     for i in range(len(sequence)-1):
        #         element1 = int(sequence[i])
        #         element2 = int(sequence[i+1])

        #         number = (element1 + element2) % 10
        #         new_sequence.append(number)

        #     sequence = new_sequence

        # return True if sequence[0] == sequence[1] else False

        sequence = list(map(int, s))  # Convert string to list of integers

        # Continue reducing the sequence until its length becomes 2
        while len(sequence) > 2:
            for i in range(len(sequence) - 1):
                sequence[i] = (sequence[i] + sequence[i + 1]) % 10
            sequence.pop()  # Remove the last element, as it's already handled

        # Check if the final two elements are the same
        return sequence[0] == sequence[1]