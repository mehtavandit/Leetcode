class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)

        result = []

        n = len(s)

        def dfs(index, path):
            if index == n:
                result.append(" ".join(path))
                return
            
            for end in range(index+1, n+1):
                if s[index:end] in wordSet:
                    path.append(s[index:end])
                    dfs(end, path)
                    path.pop()

        dfs(0, [])
        
        return result