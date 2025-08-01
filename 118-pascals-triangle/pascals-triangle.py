class Solution:
    def generate(self, numRows):
        triangle = [[1]]
        for i in range(1, numRows):
            prev = triangle[-1]
            row = [1]
            for j in range(1, i):
                row.append(prev[j - 1] + prev[j])
            row.append(1)
            triangle.append(row)
        return triangle