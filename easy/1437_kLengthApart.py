# Problem Title - Check If All 1's Are at Least Length K Places Away
# Date - 20260105

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        zero_counter = 0

        # Find the first 1 (since 0's before first 1 is not needed)
        first_1_ind = -1
        for ind, num in enumerate(nums):
            if num == 1:
                first_1_ind = ind
                break
        
        if first_1_ind == -1:   # To handle if all are 0s
            return True

        for num in nums[first_1_ind+1:]:
            if num == 0:
                zero_counter += 1
            else:
                if zero_counter < k:
                    return False
                zero_counter = 0

        return True