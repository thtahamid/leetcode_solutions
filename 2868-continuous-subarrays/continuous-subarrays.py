from typing import List

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        minTable = self.buildMinTable(nums)
        maxTable = self.buildMaxTable(nums)

        result = 0
        for i in range(n):
            low, high = i, n - 1

            while low < high:
                mid = (low + high + 1) // 2
                min_val = self.query(minTable, i, mid)
                max_val = self.queryMax(maxTable, i, mid)

                if max_val - min_val > 2:
                    high = mid - 1
                else:
                    low = mid

            result += high - i + 1
        return result

    def lg2(self, x):
        return -1 if x == 0 else (x.bit_length() - 1)

    def buildMinTable(self, a):
        n = len(a)
        max_k = self.lg2(n) + 1
        minTable = [[0] * n for _ in range(max_k)]

        for i in range(n):
            minTable[0][i] = a[i]

        for k in range(1, max_k):
            for i in range(n - (1 << k) + 1):
                minTable[k][i] = min(minTable[k - 1][i], minTable[k - 1][i + (1 << (k - 1))])
        return minTable

    def buildMaxTable(self, a):
        n = len(a)
        max_k = self.lg2(n) + 1
        maxTable = [[0] * n for _ in range(max_k)]

        for i in range(n):
            maxTable[0][i] = a[i]

        for k in range(1, max_k):
            for i in range(n - (1 << k) + 1):
                maxTable[k][i] = max(maxTable[k - 1][i], maxTable[k - 1][i + (1 << (k - 1))])
        return maxTable

    def query(self, table, x, y):
        k = self.lg2(y - x + 1)
        return min(table[k][x], table[k][y - (1 << k) + 1])

    def queryMax(self, table, x, y):
        k = self.lg2(y - x + 1)
        return max(table[k][x], table[k][y - (1 << k) + 1])      