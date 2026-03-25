class Solution:
    def canPartitionGrid(self, grid):
        m, n = len(grid), len(grid[0])

        rowSum = [0] * m
        colSum = [0] * n
        total = 0

        # Compute sums
        for i in range(m):
            for j in range(n):
                rowSum[i] += grid[i][j]
                colSum[j] += grid[i][j]
                total += grid[i][j]

        if total % 2:
            return False

        if self.check(rowSum, total):
            return True

        if self.check(colSum, total):
            return True

        return False

    def check(self, arr, total):
        left = arr[0]
        right = total - left

        for i in range(1, len(arr)):
            if left == right:
                return True
            elif left > right:
                return False
            left += arr[i]
            right -= arr[i]

        return False