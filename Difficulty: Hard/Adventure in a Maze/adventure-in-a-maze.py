class Solution:
    def findWays(self, grid):
        # code here
        M = 10**9 + 7
        n = len(grid)
        states = [[[0]*2 for _ in range(n)] for _ in range(n)]
        states[0][0] = [1, grid[0][0]]
        
        
        q = [(0, 0)]
        while q:
            nq = set()
            for r, c in q:
                path, adventure = states[r][c]
                match grid[r][c]:
                    case 1:
                        if c+1 < n:
                            states[r][c+1][0] = (states[r][c+1][0]+path)%M
                            states[r][c+1][1] = max(states[r][c+1][1], adventure+grid[r][c+1])
                            nq.add((r, c+1))
                    case 2:
                        if r+1 < n:
                            states[r+1][c][0] = (states[r+1][c][0]+path)%M
                            states[r+1][c][1] = max(states[r+1][c][1], adventure+grid[r+1][c])
                            nq.add((r+1, c))
                    case 3:
                        if c+1 < n:
                            states[r][c+1][0] = (states[r][c+1][0]+path)%M
                            states[r][c+1][1] = max(states[r][c+1][1], adventure+grid[r][c+1])
                            nq.add((r, c+1))
                        if r+1 < n:
                            states[r+1][c][0] = (states[r+1][c][0]+path)%M
                            states[r+1][c][1] = max(states[r+1][c][1], adventure+grid[r+1][c])            
                            nq.add((r+1, c))
            q = nq
        return states[-1][-1]