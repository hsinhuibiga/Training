#Cheapest Flights Within K Stops

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        graph = collections.defaultdict(dict)
        for u, v, e in flights:
            graph[u][v] = e
        ans = float('inf')
        que = collections.deque()
        que.append((src, 0))
        step = 0
        while que:
            size = len(que)
            for i in range(size):
                cur, cost = que.popleft()
                if cur == dst:
                    ans = min(ans, cost)
                for v, w in graph[cur].items():
                    if cost + w > ans:
                        continue
                    que.append((v, cost + w))
            if step > K: break
            step += 1
        return -1 if ans == float('inf') else ans