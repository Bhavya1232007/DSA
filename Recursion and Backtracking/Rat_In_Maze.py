# geeksforgeeks : Rat in a maze
class Solution:
    def ratInMaze(self, maze: list[list[int]]) -> list[str]:
        n = len(maze)
        
        if n == 0 or maze[0][0] == 0 or maze[n-1][n-1] == 0:
            return []
            
        def backtrack(row, col, directions, maze, result, ans, n):
            if row == n - 1 and col == n - 1:
                ans.append(result)
                return
            
            for r, c, d in directions:
                nr = row + r
                nc = col + c
                if nr >= 0 and nr < n and nc >= 0 and nc < n and maze[nr][nc] == 1:
                    maze[nr][nc] = '.'
                    backtrack(nr, nc, directions, maze, result + d, ans, n)
                    maze[nr][nc] = 1

        directions = [[1, 0, 'D'], [0, -1, 'L'], [0, 1, 'R'], [-1, 0, 'U']]
        row, col = 0, 0
        
        maze[row][col] = '.'
        ans = []
        result = ""
        backtrack(row, col, directions, maze, result, ans, n)
        return ans
