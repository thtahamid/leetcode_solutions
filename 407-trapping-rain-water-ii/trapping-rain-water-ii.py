class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """

        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        
        pq = []
        
        # Set the boundary elements as visited
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1 or j == 0 or j == n-1:
                    heapq.heappush(pq, (heightMap[i][j], i, j))
                    visited[i][j] = True
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        water_volume = 0
        
        # Applying the BFS Traversal
        while pq:
            cv, cr, cc = heapq.heappop(pq)
            
            # Visiting the adjacent elements of current element
            for dr, dc in directions:
                nr, nc = cr + dr, cc + dc
                
                # Checking if the element is within row, column and not visited
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    # Volume of water it can trap after raining
                    if cv - heightMap[nr][nc] > 0:
                        water_volume += cv - heightMap[nr][nc]
                        heapq.heappush(pq, (cv, nr, nc))
                    else:
                        heapq.heappush(pq, (heightMap[nr][nc], nr, nc))
                    
                    visited[nr][nc] = True
        
        return water_volume
        