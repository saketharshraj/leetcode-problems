# https://leetcode.com/problems/cheapest-flights-within-k-stops/
# 787. Cheapest Flights Within K Stops

from typing import List

class Solution:

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0
        for i in range(k+1):
            tmpPrices = prices.copy()
            for s, d, p in flights:
                if prices[s] == float('inf'):
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
        return prices[dst] if prices[dst] != float('inf') else -1


s = Solution()
n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1
result = s.findCheapestPrice(n, flights, src, dst, k)
print(result)
