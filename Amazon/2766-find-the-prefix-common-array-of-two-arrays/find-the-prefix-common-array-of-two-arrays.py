class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)

        prefix_arr = [0] * n

        elements_A, elements_B = set(), set()

        for i in range(n):
            elements_A.add(A[i])
            elements_B.add(B[i])

            count = 0

            for element in elements_A:
                if element in elements_B:
                    count += 1

            prefix_arr[i] = count

        return prefix_arr