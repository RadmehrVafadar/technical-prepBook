class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        """
        Run dijstras algorithm and find the larget number

        REAsoning:
            The node that it takes the longest to reach is the final node and dijkstras finds the least ammount of time it takes so the maxium value in our results will be the minimum ammount of time it would take
        """
        res = 0
        visited = {}
        adj = {node:[] for node in range(1, n+1)}

        # adj = 1: (distance, weight)
        for s, d, weight in times:
            adj[s].append((d, weight))

        minheap = [(0, k)]

        while minheap:
            w1, n1 = heapq.heappop(minheap)
            if n1 in visited:
                continue

            visited[n1] = w1

            for n2, w2 in adj[n1]:
                if n2 not in visited:
                    heapq.heappush(minheap, (w2+w1, n2))


        for i in range(1, n+1):
            if i in visited:
                res = max(res, visited[i])
            else:
                return -1
        return res
