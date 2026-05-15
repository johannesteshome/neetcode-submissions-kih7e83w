class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = set()
        cols = set()
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        
        for i in rows:
            for j in range(n):
                matrix[i][j] = 0

        for i in range(m):
            for j in cols:
                matrix[i][j] = 0
        