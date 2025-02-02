class Solution:
    def numTrees(self, n: int) -> int:
        u_t = [1] * (n+1)

        for nodes in range(2, n+1):
            total = 0

            for root in range(1, nodes+1):
                total += u_t[root-1] * u_t[nodes - root]
            
            u_t[nodes] = total

        return u_t[n]