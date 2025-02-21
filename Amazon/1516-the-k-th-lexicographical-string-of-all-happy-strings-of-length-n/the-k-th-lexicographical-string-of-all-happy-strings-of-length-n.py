class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        letters = ['a', 'b', 'c']

        ans = ['a', 'b', 'c']

        for i in range(n-1):
            # ans = [prefix + letter for prefix in ans for letter in letters]

            new_ans = []

            for prefix in ans:
                for letter in letters:
                    if prefix[-1] != letter:
                        new_ans.append(prefix + letter)

            ans = new_ans

        if k > len(ans):
            return ""
        return ans[k-1]


