from collections import deque

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = [[] for _ in range(n + 1)]

        for u, v, w in roads:
            g[u].append((v, w))
            g[v].append((u, w))

        vis = [False] * (n + 1)
        q = deque([1])
        vis[1] = True

        ans = float("inf")

        while q:
            u = q.popleft()

            for v, w in g[u]:
                ans = min(ans, w)

                if not vis[v]:
                    vis[v] = True
                    q.append(v)

        return ans