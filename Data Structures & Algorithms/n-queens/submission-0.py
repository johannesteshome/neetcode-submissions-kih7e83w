class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        answer = []
        board = [["." for _ in range(n)] for _ in range(n)]

        def backtrack(row, cols, diag, antiDiag, queens):
            
            if queens == 0:
                answer.append(["".join(row) for row in board])
                return
            
            for col in range(n):
                if col in cols:
                    continue
                if row-col in diag:
                    continue
                if row + col in antiDiag:
                    continue
                cols.add(col)
                diag.add(row-col)
                antiDiag.add(row+col)
                board[row][col] = "Q"
                backtrack(row+1, cols, diag, antiDiag, queens - 1)
                cols.remove(col)
                diag.remove(row-col)
                antiDiag.remove(row+col)
                board[row][col] = "."
            
        
        backtrack(0, set(), set(), set(), n)
        
        return answer
                