# Problem Title - Lucky Numbers in a Matrix
# Date - 20251227

class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        row_min_list = []
        col_max_list = []

        # Find the min. element for every row
        for row in matrix:
            min_val = min(row)
            row_min_list.append(min_val)
        
        # Find the max. element for every col
        for j in range(len(matrix[0])):
            col_max = 0
            for i in range(len(matrix)):
                if matrix[i][j] > col_max:
                    col_max = matrix[i][j]
            col_max_list.append(col_max)
        
        print(f"row_min_list: {row_min_list}")
        print(f"col_max_list: {col_max_list}")

        # Find the common elements b/w row_min and col_max lists
        result_list = list(set(row_min_list) & set(col_max_list))
        return result_list