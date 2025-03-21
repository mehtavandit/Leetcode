class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        # n = len(A)

        # prefix_arr = [0] * n

        # elements_A, elements_B = set(), set()

        # for i in range(n):
        #     elements_A.add(A[i])
        #     elements_B.add(B[i])

        #     count = 0

        #     for element in elements_A:
        #         if element in elements_B:
        #             count += 1

        #     prefix_arr[i] = count

        # return prefix_arr

        #TC = O(n2) SC = O(n)

        # For O(n) see editorial

        result = []
        n = len(A)

        freq = [0] * (n+1)
        count = 0

        for i in range(n):
            freq[A[i]] += 1

            if freq[A[i]] == 2:
                count += 1

            freq[B[i]] += 1

            if freq[B[i]] == 2:
                count += 1

            result.append(count)

        return result