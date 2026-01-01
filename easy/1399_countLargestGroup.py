# Problem Title - Count Largest Group
# Date - 20251231

class Solution:
    def get_sum_of_digits(self, num: int) -> int:
        temp = num
        sum1 = 0
        while temp > 0:
            digit = temp%10
            sum1 += digit
            temp = int(temp/10)
        return sum1

    def countLargestGroup(self, n: int) -> int:
        count_dict = {}     # To keep track of the sum digits for every num from 0 to 8 (9 is 0)
        # Iterate from 1 to n
        for num in range(1, n+1):

            """
            # Below was my first solution - Assuming that we should 
            # sum up digits until only 1 digit is obtained
            # This will give the sum of digits (if its 0, it is 9).
            # But the number itself does not matter here. Only the highest frequency count matters.
            sum_digits = num%9
            """
            sum_digits = self.get_sum_of_digits(num)
            # Update the dict with frequency
            if sum_digits not in count_dict:
                count_dict[sum_digits] = 1
            else:
                count_dict[sum_digits] += 1
                
        print(f"count_dict: {count_dict}")
        # Take the max frequency count for all the digits
        max_count_value = max(count_dict.values())
        result_count = 0
        # Count the group count, which matches the max frequency value
        for val in count_dict.values():
            if val == max_count_value:
                result_count += 1
        
        return result_count