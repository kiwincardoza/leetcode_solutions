# Problem Title - Special Array With X Elements Greater Than or Equal X
# Date - 20260107

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        """
        Sort the array.
        if num > remaining elements, then return remaining elements (since min. value)
        if they are equal, return num
        if nothing is returned in loop, return -1
        """
        n = len(nums)
        nums.sort()
        prev_num = -1

        for ind, num in enumerate(nums):
            remaining_elements = n-(ind+1)+1
            
            # Condition to handle an edge case: should track of max.element 
            # until then to avoid excluding that in solution (figured this later)
            if remaining_elements > prev_num:
                if num > remaining_elements:
                    return remaining_elements
                if num == remaining_elements:
                    return num
            prev_num = num
        return -1