class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Initialize the distance matrix
        dist = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0

        # Set initial edge weights
        for edge in edges:
            dist[edge[0]][edge[1]] = edge[2]
            dist[edge[1]][edge[0]] = edge[2]

        # Floyd-Warshall algorithm to find shortest paths between all pairs of cities
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] < float('inf') and dist[k][j] < float('inf'):
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        ans_node = -1
        city_cnt = float('inf')
        for i in range(n - 1, -1, -1):
            cnt = 0
            for j in range(n):
                if dist[i][j] <= distanceThreshold and i != j:
                    cnt += 1

            if cnt < city_cnt:
                ans_node = i
                city_cnt = cnt

        return ans_node       