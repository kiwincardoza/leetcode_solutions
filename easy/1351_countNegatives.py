# Problem Title - Count Negative Numbers in a Sorted Matrix
# Date - 20251224

class Solution:
    def binSearchIndex(self, row: List[int]) -> int:
        low = 0
        high = self.n-1
        mid = int((low+high)/2)
        while low<=high:
            # print(f"mid: {mid}; low: {low}; high: {high}")
            # Cover exit cases
            if (row[mid]>=0) and (mid+1 == self.n):    # Edge case when there are no negative nos.
                return self.n-1
            if (row[mid]>=0) and (row[mid+1]<0):    # Found our index
                return mid
            if (row[mid]<0) and (mid==0):     # Edge case when there are no positive nos.
                return -1
            if (row[mid]<0) and (row[mid-1]>=0):    # Found our index
                return mid-1
            
            if row[mid]<0:
                high = mid-1
            elif row[mid]>=0:
                low = mid+1
            mid = int((low+high)/2)

    def countNegatives(self, grid: List[List[int]]) -> int:
        result_neg_count = 0
        self.m = len(grid)   # no. of rows
        self.n = len(grid[0])    # no. of columns

        for row in grid:
            mid_index = self.binSearchIndex(row)
            print(f"mid_index: {mid_index}")
            result_neg_count += (self.n-mid_index-1)    # Count the remaining neg. nos.

        return result_neg_count
