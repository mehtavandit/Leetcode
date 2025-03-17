from collections import defaultdict

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mapping = defaultdict(int)

        for i in range(len(s)):
            mapping[s[i]] = i

        print(mapping)

        partitions = []

        start, end = 0, 0

        for i in range(len(s)):
            end = max(end, mapping[s[i]])
            if i == end:
                partitions.append(i-start+1)
                start = i+1

        return partitions

