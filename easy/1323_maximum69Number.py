# Problem Title - Maximum 69 Number
# Date - 20251210

class Solution:
    def get_digits(self, num: int) -> List[int]:
        digits_list = []
        temp = num
        while temp > 0:
            digit = temp%10
            temp = int(temp/10)
            digits_list.append(digit)
        return digits_list[::-1]

    def maximum69Number (self, num: int) -> int:
        digits_list = self.get_digits(num)
        # Just replace the first occurence of 6 (if there) by 9
        for ind, digit in enumerate(digits_list):
            if digit == 6:
                digits_list[ind] = 9
                break
        return int(''.join([str(digit) for digit in digits_list]))