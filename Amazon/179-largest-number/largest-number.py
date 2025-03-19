class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        s = [str(x) for x in nums]

        def comparator(x,y):
            return -1 if x+y > y+x else 1

        s.sort(key = cmp_to_key(comparator))

        ans = "".join(s)

        return '0' if ans[0] == '0' else ans