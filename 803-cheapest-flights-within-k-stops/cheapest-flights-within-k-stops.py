import heapq as hq
from collections import defaultdict
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)

        for u, v, w in flights:
            adj[u].append((v, w))

        stops = [float("inf")] * n
        pq = [[0, src, 0]]      # distance, node, step

        while pq:
            distance, node, step = hq.heappop(pq)

            if node == dst:
                return distance

            if step > k:
                continue

            if step > stops[node]:
                continue

            stops[node] = step

            for neighbor, price in adj[node]:
                hq.heappush(pq, [distance + price, neighbor, step + 1])

        return -1