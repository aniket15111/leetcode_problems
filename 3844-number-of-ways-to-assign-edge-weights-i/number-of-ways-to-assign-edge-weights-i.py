class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        queue = deque([(1, -1, 0)])
        max_depth = 0
        
        while queue:
            node, parent, depth = queue.popleft()
            max_depth = max(max_depth, depth)
            
            for neighbor in graph[node]:
                if neighbor != parent:
                    queue.append((neighbor, node, depth + 1))

        MOD = 10**9 + 7
        return pow(2, max_depth - 1, MOD)