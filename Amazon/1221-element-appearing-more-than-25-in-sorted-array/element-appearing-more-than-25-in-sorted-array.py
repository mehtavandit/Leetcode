class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        if len(arr) < 2:
            return arr[0]

        result = 0

        percent = int (len(arr) * 0.25)

        count = Counter(arr)

        for key, count in count.items():
            if count > percent:
                result = key

        return result