class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
        def isInbound(i, j):
            return 0 <= i < len(board) and 0 <= j < len(board[0])
        
        def dfs(i,j, index):

            if index == len(word) - 1:
                return True

            for offsetI, offsetJ in directions:

                newI = i + offsetI
                newJ = j + offsetJ

                if isInbound(newI, newJ) and word[index+1] == board[newI][newJ] and (newI, newJ) not in visited:
                    visited.add((newI, newJ))
                    if dfs(newI, newJ, index+1):
                        return True

            visited.remove((i, j))
        
        visited = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                if word[0] == board[i][j]:
                    visited.add((i, j))
                    if dfs(i, j, 0):
                        return True
        
        return False
                
