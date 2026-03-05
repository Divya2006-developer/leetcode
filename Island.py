class Solution(object):
    def islandPerimeter(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # Add 4 for the current land cell
                    perimeter += 4
                    
                    # Check neighbor ABOVE
                    if r > 0 and grid[r-1][c] == 1:
                        perimeter -= 2
                    
                    # Check neighbor to the LEFT
                    if c > 0 and grid[r][c-1] == 1:
                        perimeter -= 2
                        
        return perimeter
