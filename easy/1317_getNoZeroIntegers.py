# Problem Title - Convert Integer to the Sum of Two No-Zero Integers
# Date - 20251209

class Solution:

    def check_zero_in_integer(self, n: int) -> bool:
        """
        Just gets each digit (decimal) by bruteforce
        """
        temp = n
        while temp>0:
            # print(f"temp: {temp}")
            digit = temp%10
            if digit == 0:
                return False
            temp = int(temp/10)
        return True


    def getNoZeroIntegers(self, n: int) -> List[int]:
        start_no = 1
        while True:
            # print(f"start_no: {start_no}")
            # Pre-check -  If it divisible by 10, it definitely has a 0 in number
            if (start_no%10 == 0) or ((n-start_no)%10 == 0):
                start_no += 1
                continue
            first_check = self.check_zero_in_integer(start_no)
            # print("First check done")
            second_check = self.check_zero_in_integer(n-start_no)
            # print("Second check done")
            if first_check and second_check:
                return [start_no, n-start_no]
            start_no += 1