class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)
        count = 0

        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        
        visited = set()

        def dfs(node):

            for neighbor in adjList[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)
        

        for i in range(n):
            if i not in visited:
                count += 1
                visited.add(i)
                dfs(i)
        
        return count