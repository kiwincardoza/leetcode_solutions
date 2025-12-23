# Problem Title - Number of Steps to Reduce a Number to Zero
# Date - 20251222

class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:   # Edge case
            return 0
        temp = num
        result_steps = 0
        while temp > 0:
            if temp%2 == 0:
                result_steps += 1    # If even, just increment by 1
            else:
                result_steps += 2    # If odd, we inc. by 2, bypassing one extra iteration
            temp = int(temp/2)     # Instead of subtracting, we take the floor val
        # Since last iteration num will be always 1, we make up for adding-by-2 (for odd)
        return result_steps-1