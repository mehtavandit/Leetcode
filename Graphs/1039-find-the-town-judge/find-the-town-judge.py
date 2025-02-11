class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        trusted_by_others = [0] * (n+1)
        trust_others = [0] * (n+1)

        for i in trust:
            trust_others[i[0]] += 1
            trusted_by_others[i[1]] += 1

        for i in range(1, n+1):
            if trusted_by_others[i] == n-1 and trust_others[i] == 0:
                return i
        
        return -1