class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        mapping = defaultdict(int)

        for i in range(k):
            mapping[blocks[i]]+=1

        changes_need = mapping["W"]

        

        for i in range(k, len(blocks) ):
            mapping[blocks[i]] += 1
            mapping[blocks[i-k]] -= 1

            changes_need = min(changes_need, mapping["W"])

        return changes_need