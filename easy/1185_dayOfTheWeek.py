# Problem Title - Day of the Week
# Date - 20251219

class Solution:
    def check_if_leap_year(self, year: int) -> bool:
        # Check if n is divisible by 4
        if year%4 == 0:
            # If it's divisible by 100, it should also be 
            # divisible by 400 to be a leap year
            if year%100 == 0:
                return year%400 == 0
            return True
        return False

    def find_number_of_days(self, year: int) -> int:
        if self.check_if_leap_year(year):
            return 366
        return 365

    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        no_of_days = 0
        for year0 in range(1971, year):
            no_of_days += self.find_number_of_days(year0)
        
        print(f"no_of_days 1: {no_of_days}")
        leap_year_flag = self.check_if_leap_year(year)
        print(f"leap_year_flag: {leap_year_flag}")
        for month0 in range(1, month):
            if month0 in (1, 3, 5, 7, 8, 10, 12):
                no_of_days += 31
            elif month0 in (4, 6, 9, 11):
                no_of_days += 30
            elif month0 == 2:
                no_of_days += 28
        print(f"no_of_days 2: {no_of_days}")
        no_of_days += day
        print(f"no_of_days 3: {no_of_days}")

        # Add a day if it was a leap year and the month is past Feb
        if leap_year_flag and (month>2):
            no_of_days += 1
        print(f"no_of_days 4: {no_of_days}")

        mod_val = no_of_days%7
        weekday_list = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
        # Subtracted based on the expected output and my output. Did not think on logic
        return weekday_list[(mod_val-1)%7]
