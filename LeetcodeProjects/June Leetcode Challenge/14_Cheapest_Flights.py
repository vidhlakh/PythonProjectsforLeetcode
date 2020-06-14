from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n , flights, src, dst, K):
        if src == dst:
            return 0
        location = defaultdict(list)
        prices = defaultdict(lambda: float('inf'))
        for u,v ,p in flights:
            location[u] += [(v,p)]
        q = [(src, -1, 0)]
        while q:
            position, k , cost = q.pop(0)
            if position == dst or k == K:
                continue
            for neighbor, p in location[position]:
                if cost + p >= prices[neighbor]:
                    continue
                else:
                    prices[neighbor] = cost + p
                    q += [(neighbor, k+1, cost+p)]
        if prices[dst] < float('inf'):
            return prices[dst]


s = Solution()
print(s.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]],0, 2, 1))