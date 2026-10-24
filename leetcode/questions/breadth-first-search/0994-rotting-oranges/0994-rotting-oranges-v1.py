# Early pseudocode

# Earlier revision (preserved)

# # [2, 1 , 1]
#       # bfs(index)
#       # q = collections.deque()
#       # q.append(grid[index])
#       # timer = 0
#       # while q:
#       # timer += 1
#       # adding adjecent oranges

# Partial screenshot draft

# Earlier revision (preserved)

# visited = set()
# def bfs(r,c)
# rows, cols = len(grid), len(grid[0])
#
# for row in range(rows):
#     for col in range(cols):
#         if grid[row][col] == '2' and (row,col) not in visited:
#
# return -1

# Final user implementation, assisted by coaching and a solution video

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        q = collections.deque()
        time = oranges = 0
        rows, cols = len(grid), len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    oranges += 1
                if grid[row][col] == 2:
                    q.append((row,col))

        while q and oranges > 0:
            # Review later: move directions before the while loop to avoid
            # rebuilding this list each minute; asymptotic complexity is unchanged.
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    r_dr, c_dc = r+dr,c+dc
                    if 0 <= r_dr < rows and 0 <= c_dc < cols and grid[r_dr][c_dc] == 1:
                        q.append((r_dr, c_dc))
                        oranges -= 1
                        grid[r_dr][c_dc] = 2
            time += 1
        if oranges == 0:
            return time
        else:
            return -1
