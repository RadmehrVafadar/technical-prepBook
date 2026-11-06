# python please :)
"""
0 0 1 X .
1 1 2 . .
1 X . . E
(2,4)

"""
"""
Create a function that takes in the state of the game r*c and takes an input from the user r,c

Questions:
- what is the grid input? grid is a 2D array of strings
- X would represent a exploded
- . represents not discovered yet
- 0-8 would represents the number of bombs that are adjacent and diagonal

- for the second input [r,c]
- we would be flooding the adjacent cells
- what are we returning? the gird after the selected
- does the input have to start as never clicked? no

- would the user ever click something that has been clicked? still return that grid with the appropriate update
- might click out of bounds, click on the mine the game is over?
- what to return when the game is over? give -1

- grid? n*m
- range of n? 2-100 (inclusive) 10,000
- range of m? 2-100 (inclusive)

- range of the number of bombs? 30 mines always
- the mines will have random locations
- modify? yes

- for input r range? positive integer: 0-float('inf')
- for input c range? positive integer: 0-inf

- is the an inherit complexity? no

- what are we creating? the gird has already been created, up to us how we accsess it


- design it how we like in order to figure out where the bombs were

- given a set where the mines are
- are we allwed to use deque? yes
""

""
Highe leve:
1. take a grid and input (r,c)
2. if the r,c is out of bounds? Print an error messaage saying it is out of bounds or if the game is over print game is over (raise an exception)
3. otherwise, the (r,c) will be clicked within the grid and the flood function will update the exsting grid
4. once that is finished, it would return the new grid

Casses:
1. Cell is already clicked (do nothing)
2. Cell is a bomb (return the grid and say game over?)
3. Cell is not a bomb, (expand the adjacent cells around it and replace the locations that had bombs with the number of bombs the had)
4. If cell has atleast one adjacent mine we would update that cell (base case would be the single cell)


Approach:
Validate input
check if the cell has already been visited
check weather the player has activated a bomb
Iterative DFS
return the updated board and game status

Approach:  (iterative dfs)
1. base case being the cell that we start with.
2.

""""

class Solution:
  def isOutOfBoudns():
    return ...

	def findCell(self, grid, row, col, bombs, visited):
    	ROWS, COLS = len(grid), len(grid[0])

      if cell in visited:
        	return grid

      if (isOutOfBounds(grid, row, col)):
        	return grid

      if (row, col) in bombs:
        	return grid

  def fillFlood(self, grid, row, col, bombs):
    	ROWS, COLS = len(grid), len(grid[0])

      directions = [
        (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
      ]

      q = deque([(row, col)])
      visited = {(row, col)}

      while q:
        	row, col = q.popleft()
          visited.add((row, col))
          count = 0


          for dr, dc in directions:
            	newR, newC = (row + dr), (col + dc)

              if (newR, newC) in bombs:
                	count += 1
          grid[row][col] = str(count)

          if count == 0:
            for dr, dc in directions:
              newR, newC = (row + dr), (col + dc)

              if (newR < 0 or  newC < 0 or newC == COLS or newR == ROWS or (newR, newC) in bombs or (newR, newC) in visted):
                continue
              visited.add((newR, newC))
              q.append((newR, newC))





if __name__ == "__mnain__":
  print()











"""
