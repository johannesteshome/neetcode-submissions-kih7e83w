class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        '''
        (i, j) -> (j, len(matrix) - 1 - i)
        (1,0) -> (0, 1)
        (2,0) -> (0, 0)

        (0,2) -> (2,2)
        '''

        for i in range(len(matrix) // 2):
            for j in range(i, len(matrix[i]) - 1 - i):

                x, y = i, j

                temp = matrix[x][y]

                for _ in range(4):

                    newX = y
                    newY = len(matrix) - 1 - x

                    temp1 = matrix[newX][newY] 

                    matrix[newX][newY] = temp

                    temp = temp1

                    x = newX
                    y = newY


