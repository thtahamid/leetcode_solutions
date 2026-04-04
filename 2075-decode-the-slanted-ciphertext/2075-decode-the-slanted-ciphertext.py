class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 0:
            return ""

        n = len(encodedText)
        if n == 0:
            return ""

        cols = n // rows

        # Step 1: Build matrix
        mat = []
        idx = 0
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(encodedText[idx])
                idx += 1
            mat.append(row)

        # Step 2: Diagonal traversal
        result = []

        for startCol in range(cols):
            i, j = 0, startCol
            while i < rows and j < cols:
                result.append(mat[i][j])
                i += 1
                j += 1

        # Step 3: Remove trailing spaces
        return "".join(result).rstrip()