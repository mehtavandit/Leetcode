from collections import defaultdict, deque
import math

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = defaultdict(list)

        for source, destination, price in flights:
            adj_list[source].append((destination, price))

        q = deque()
        q.append((src, 0, k+1)) #k+1 are the remaining stops
        min_cost = {i:math.inf for i in range(n)}
        min_cost[src] = 0

        while q:
            city, cost, stops = q.popleft()

            if city == dst: #now explore a cheaper option
                continue

            if stops > 0:
                for neighbour, prices in adj_list[city]:
                    new_cost = cost + prices

                    if new_cost < min_cost[neighbour]:
                        min_cost[neighbour] = new_cost
                        q.append((neighbour, new_cost, stops-1))

        return min_cost[dst] if min_cost[dst] != math.inf else -1