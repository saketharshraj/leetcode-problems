# https://leetcode.com/problems/cheapest-flights-within-k-stops/
# 787. Cheapest Flights Within K Stops

from typing import List
class Solution:
    def build_graph(self, n, edges):
        graph = {}
        for i in range(n):
            graph[i] = set()

        for u, v, w in edges:
            graph[u].add((v,w))
        
        return graph


    def bfs(self, graph, src, dst, k):
        queue = [(src, 0, 0)]
        visited = set()
        while queue:
            node, cost, stops = queue.pop(0)
            if node == dst:
                return cost
            
            if stops > k:
                continue
            for neighbor, w in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, cost + w, stops + 1))
                    visited.add(neighbor)
        return -1


    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = self.build_graph(n, flights)
        return self.bfs(graph, src, dst, k)
    

s = Solution()
n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600]]
src = 0
dst = 3
k = 1
result = s.findCheapestPrice(n, flights, src, dst, k)
print(result)
