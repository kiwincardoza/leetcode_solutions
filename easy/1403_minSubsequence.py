# Problem Title - Minimum Subsequence in Non-Decreasing Order
# Date - 20260102

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort()     # Sort the list, to satsify the return conditions (non-dec, and smallest sub-seq)
        n = len(nums)
        total_sum = sum(nums)

        # Pointers to keep track of left and right movements
        left_sum = total_sum
        right_sum = 0

        result_list = []
        i = n-1
        while i>=0:
            right_sum += nums[i]
            left_sum -= nums[i]
            print(f"left_sum: {left_sum}")
            print(f"right_sum: {right_sum}")
            result_list.append(nums[i])
            # Check for breaking condition
            if left_sum < right_sum:
                break
            i -= 1
        return result_list