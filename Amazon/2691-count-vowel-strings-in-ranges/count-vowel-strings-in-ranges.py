class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = ['a', 'e', 'i', 'o', 'u']

        result = []

        prefix_arr = [0] * len(words)

        if words[0][0] in vowels and words[0][-1] in vowels:
            prefix_arr[0] = 1

        for i in range(1, len(words)):
            if words[i][0] in vowels and words[i][-1] in vowels:
                prefix_arr[i] = prefix_arr[i-1] + 1
            
            else:
                prefix_arr[i] = prefix_arr[i-1]

        for left, right in queries:
            if left == 0:
                result.append(prefix_arr[right])
            else:
                result.append(prefix_arr[right] - prefix_arr[left-1])

        return result

