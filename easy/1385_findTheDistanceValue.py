# Problem Title - Find the Distance Value Between Two Arrays
# Date - 20251228

class Solution:
    def find_max_neg_num_index(self, arr2: List[int]) -> int:
        if arr2[0] >= 0:
            return -1
        i = 0
        while i < len(arr2):
            if arr2[i] >= 0:
                return i-1  # Return the last negative number's index
            i += 1
        
    def find_min_pos_num_index(self, arr2: List[int]) -> int:
        if arr2[-1] < 0:
            return -1
        i = 0
        while i < len(arr2):
            if arr2[i] >= 0:
                return i    # Return the first positive number's index
            i += 1

    def get_mid_index_of_arr2(self, arr2: List[int], num: int) -> int:
        """
        Get the index where the num is lesser than the index, but greater than index-1.
        """
        n = len(arr2)
        low = 0
        high = n-1
        mid = int((low+high)/2)

        while low <= high:
            print(f"mid: {mid}; low: {low}; high: {high}")
            if (mid == 0):
                if arr2[mid] >= num:
                    return mid
            if mid == n-1:
                if arr2[mid] <= num:
                    return mid  
            if (arr2[mid] > num) and (arr2[mid-1] <= num):
                return mid
            if (arr2[mid] >= num) and (arr2[mid-1] <= num):
                return mid+1
            if arr2[mid] > num:
                high = mid-1
            elif arr2[mid] < num:
                low = mid+1
            mid = int((low+high)/2)
        return -1
            
            

    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        # The below is my first solution, which is wrong
        """
        arr1.sort()
        arr2.sort()

        m = len(arr1)
        n = len(arr2)
        print(arr1)
        print(arr2)

        max_neg_ind = self.find_max_neg_num_index(arr2)
        min_pos_ind = self.find_min_pos_num_index(arr2)

        print(f"max_neg_ind: {max_neg_ind}")
        print(f"min_pos_ind: {min_pos_ind}")

        i_flag = False
        for i in range(m-1, -1, -1):
            if i_flag:
                break
            if max_neg_ind!=-1 and min_pos_ind!=-1:
                if (abs(arr1[i]-arr2[max_neg_ind]) > d) and (abs(arr1[i]-arr2[min_pos_ind]) > d):
                    i_flag = True
            elif max_neg_ind!=-1:
                if (abs(arr1[i]-arr2[max_neg_ind]) > d):
                    i_flag = True
            elif min_pos_ind!=-1:
                if (abs(arr1[i]-arr2[min_pos_ind]) > d):
                    i_flag = True
        
        if i_flag:
            return i+2
        return 0
        """

        # Sorting both arrays - Actually first array sorting is not needed
        # Can be optimised more with first array sorting by ignoring traversal after a point
        arr1.sort()
        arr2.sort()

        m = len(arr1)
        n = len(arr2)
        print(arr1)
        print(arr2)

        result_count = 0

        # Travers each element in the first array - Not needed as mentioned in the top
        for i in range(m):
            num = arr1[i]
            # To get the two element range
            mid_ind = self.get_mid_index_of_arr2(arr2, num)
            print(f"mid_ind: {mid_ind}")
            if mid_ind == n:    # Handle separately if its the last element
                if (abs(num-arr2[-1]) > d):
                    result_count += 1
            elif mid_ind == 0:    # Handle separately if its the first element
                if (abs(num-arr2[0]) > d):
                    result_count += 1
            elif ((mid_ind > 0) and (mid_ind < n)):
                if (abs(num-arr2[mid_ind-1]) > d) and (abs(num-arr2[mid_ind]) > d):
                    result_count += 1
            
        return result_count