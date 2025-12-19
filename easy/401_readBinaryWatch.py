# Problem Title - Binary Watch
# Date - 20251218

class Solution:
    def find_number_of_set_bits(self, num: int) -> int:
        temp = num
        set_bits = 0
        while temp > 0:
            mod = temp%2
            if mod == 1:
                set_bits += 1
            temp = int(temp/2)
        return set_bits

    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn >= 9:
            return []
        
        # Get the number of set bits for all possible times
        set_bits_dict = {0: 0, 1: 1, 2: 1, 4: 1, 8: 1, 16: 1, 32: 1}
        for i in range(3, 60):
            if i in (4, 8, 16, 32):   # Already set above
                continue
            set_bits = self.find_number_of_set_bits(i)
            set_bits_dict[i] = set_bits

        print(f"set_bits_dict: {set_bits_dict}")
        result_list = []
        for hour in range(12):
            for minute in range(60):
                if ((set_bits_dict[hour]+set_bits_dict[minute]) != turnedOn):
                    continue
                result_list.append(f"{hour}:{minute:0>2}")
        
        return result_list