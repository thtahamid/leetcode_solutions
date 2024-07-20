class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows, cols = len(rowSum), len(colSum)
        
        result = [[0] * cols for _ in range(rows)]

        for r in range(rows):
            result[r][0] = rowSum[r]

        for c in range(cols):
            cur_col_sum = 0
            for r in range(rows):
                cur_col_sum += result[r][c]

            r = 0
            while cur_col_sum > colSum[c]:
                diff = cur_col_sum - colSum[c]
                max_shift = min(result[r][c], diff)
                result[r][c] -= max_shift
                result[r][c+1] += max_shift
                cur_col_sum -= max_shift
                r += 1
        return result

        