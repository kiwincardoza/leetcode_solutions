# Problem Title - How Many Numbers Are Smaller Than The Current Number
# Date - 20251226

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_sorted = sorted(nums)

        ind = 1
        prev_num = nums_sorted[0]
        prev_ind = 0
        nums_dict = {prev_num: prev_ind}
        for num in nums_sorted[1:]:
            # Only update the dict val if the element is changing, else I don't touch it
            if num != prev_num:
                nums_dict[num] = ind
                prev_ind = ind
                prev_num = num
            ind += 1
        
        # Had to store in a dict, since the original nums order has to be preserved
        result_list = []
        for num in nums:
            result_list.append(nums_dict[num])
        return result_list