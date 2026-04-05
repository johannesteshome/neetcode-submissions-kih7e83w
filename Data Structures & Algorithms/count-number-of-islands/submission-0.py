class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # steps I'm gonna take
        # 1. to look if there is an unvisited 'land' - value 1
        # 2. do dfs seatch starting from that cell
        # 3. once the dfs is complete we can say that it is an island we can count it as an island
        # 4. iterate do step 1

        # the directions which are horizontal and vertical direction
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        visited = set()

        # helper function to check if we are inside the grid
        def inbound(x, y):
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                return True
            
            return False
        
        nums = 0

        # dfs search
        def dfs(x, y):
                        
            for dir in directions:
                newX = x + dir[0]
                newY = y + dir[1]
                # print(newX, newY)

                if not inbound(newX, newY):
                    # print('not in grid', newX, newY)
                    continue

                # print('in grid', newX, newY, grid[newX][newY])
                if grid[newX][newY] != '0' and (newX, newY) not in visited:
                    visited.add((newX, newY))
                    dfs(newX, newY)

        # iterate through the grid to find unvisited land
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != '0' and (i, j) not in visited:
                    visited.add((i, j))
                    # print(visited, 'visited')
                    dfs(i, j)
                    nums += 1
        

        return nums
