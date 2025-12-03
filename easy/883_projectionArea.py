# Problem Title - Projection Area of 3D Shapes
# Date - 20251126

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        top_count = 0
        front_count = 0
        side_count = 0

        for row in grid:
            for col in row:
                if col != 0:
                    top_count += 1
        
        n = len(grid)
        for row in grid:
            side_count += max(row)
        
        for i in range(n):
            tmp_max = -9
            for j in range(n):
                if grid[j][i] > tmp_max:
                    tmp_max = grid[j][i]
            front_count += tmp_max
        
        print(f"top_count: {top_count}")
        print(f"front_count: {front_count}")
        print(f"side_count: {side_count}")
        return top_count+front_count+side_count