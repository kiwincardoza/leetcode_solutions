# Problem Title - Shift 2D Grid
# Date - 20251204

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        """
        This problem description looks quite complex, but its just simply rotations
        """
        m = len(grid)
        n = len(grid[0])

        k = k%(n*m)

        result_list = []
        for i in range(m):
            result_list.append([])
            for j in range(n):
                result_list[i].append(0)

        # Get the row and col marker
        # Row
        first_val = ceil(k/n)
        row_marker = m-first_val

        # Col
        col_marker = (n*m-k)%n

        print(f"row_marker: {row_marker}; col_marker: {col_marker}")

        # Fills in the rotated values 
        real_i = 0
        real_j = 0

        for i in range(row_marker, m):
            if i == row_marker:
                var_j = col_marker
            else:
                var_j = 0
            for j in range(var_j, n):
                print(f"i: {i}; j: {j}")
                print(f"real_i: {real_i}; real_j: {real_j}")
                result_list[real_i][real_j%n] = grid[i][j]
                if (real_j+1)%n == 0:
                    real_i += 1
                    real_i = (real_i)%m
                real_j += 1
                real_j = real_j%n
        print(f"result_list: {result_list}")
        print(f"real_i: {real_i}; real_j: {real_j}")
        
        # Fills in the proper values
        sec_i = 0
        sec_j = 0
        for i in range(real_i, m):
            if i == real_i:
                var_j = real_j
            else:
                var_j = 0
            for j in range(var_j, n):
                # print(f"i: {i}; j: {j}")
                # print(f"sec_i: {sec_i}; sec_j: {sec_j%n}")
                result_list[i][j] = grid[sec_i][sec_j%n]
                if (sec_j+1)%n == 0:
                    sec_i += 1
                    sec_i = (sec_i)%m
                sec_j += 1
        return result_list
