class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])
        result = []
        
        row_min = set()
        for r in range(ROWS):
            row_min.add(min(matrix[r]))
        
        
        for c in range(COLS):
            cur_max = matrix[0][c]
            for r in range(ROWS):
                cur_max = max(cur_max, matrix[r][c])
            if cur_max in row_min:
                result.append(cur_max)
        

        return result
        





# class Solution:
#     def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
#         ROWS, COLS = len(matrix), len(matrix[0])
#         res = []
        
#         row_min = set()
#         for r in range(ROWS):
#             row_min.add(min(matrix[r]))
        
#         col_max = set()
#         for c in range(COLS):
#             cur_max = matrix[0][c]
#             for r in range(ROWS):
#                 cur_max = max(cur_max, matrix[r][c])
#             col_max.add(cur_max)
#         for i in row_min:
#             if i in col_max:
#                 res.append(i)

#         return res
        