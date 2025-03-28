import heapq

class Solution:
    def maxPoints(self, grid, queries):
        n, m = len(grid), len(grid[0])
        k = len(queries)

        q = [(queries[i], i) for i in range(k)]
        q.sort()

        vis = [[False] * m for _ in range(n)]
        res = [0] * k
        maxPoints = 0
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        pq = [(grid[0][0], 0, 0)]
        vis[0][0] = True

        for val, indx in q:
            while pq and pq[0][0] < val:
                currVal, row, col = heapq.heappop(pq)
                maxPoints += 1
                for dx, dy in directions:
                    newRow, newCol = row + dx, col + dy
                    if 0 <= newRow < n and 0 <= newCol < m and not vis[newRow][newCol]:
                        heapq.heappush(pq, (grid[newRow][newCol], newRow, newCol))
                        vis[newRow][newCol] = True
            res[indx] = maxPoints
        
        return res