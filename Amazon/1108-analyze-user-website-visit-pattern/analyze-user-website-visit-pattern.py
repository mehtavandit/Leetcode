from typing import List
from collections import defaultdict, Counter
import itertools

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # Step 1: Group the websites visited by each user in chronological order
        user_visited = defaultdict(list)

        for user, _, site in sorted(zip(username, timestamp, website), key=lambda x: x[1]):
            user_visited[user].append(site)

        # Step 2: Count all unique triples of websites visited by users
        counter = Counter()

        for visited_websites in user_visited.values():
            # Get unique combinations of triples
            unique_triples = set(itertools.combinations(visited_websites, 3))
            for triple in unique_triples:
                counter[triple] += 1

        # Step 3: Find the most visited pattern with tie-breaking
        pattern, count = None, 0

        for pat, c in counter.items():
            if c > count or (c == count and (pattern is None or pat < pattern)):
                pattern = pat
                count = c

        return list(pattern) if pattern else []
