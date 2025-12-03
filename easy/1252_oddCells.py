# Problem Title - Cells with Odd Values in a Matrix
# Date - 20251203

class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        row_dict = {}
        col_dict = {}

        # Create a dict for row and col indices of the total count
        for index_pair in indices:
            row_ind = index_pair[0]
            col_ind = index_pair[1]
            if row_ind not in row_dict:
                row_dict[row_ind] = 1
            else:
                row_dict[row_ind] += 1
            if col_ind not in col_dict:
                col_dict[col_ind] = 1
            else:
                col_dict[col_ind] += 1
        
        # Construct a row matrix and a col matrix in the same iteration
        # Then we can add them both
        row_matrix = []
        col_matrix = []
        for row in range(m):
            row_matrix.append([])
            col_matrix.append([])
            for col in range(n):
                if row in row_dict:
                    row_matrix[row].append(row_dict[row])
                else:
                    row_matrix[row].append(0)
                if col in col_dict:
                    col_matrix[row].append(col_dict[col])
                else:
                    col_matrix[row].append(0)
        print(f"row_matrix: {row_matrix}")
        print(f"col_matrix: {col_matrix}")

        result = 0
        for row in range(m):
            for col in range(n):
                sum_val = row_matrix[row][col] + col_matrix[row][col]
                if sum_val%2 == 1:
                  result += 1  
        return result