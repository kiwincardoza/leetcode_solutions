# Problem Title - Sort Integers by The Number of 1 Bits
# Date - 20251226

class Solution:
    def count_1_bits(self, num: int) -> int:
        """ Just counts the number of bits where bit == 1 """
        count = 0
        temp = num
        while temp > 0:
            if temp%2 == 1:
                count += 1
            temp = int(temp/2)
        return count

    def sortByBits(self, arr: List[int]) -> List[int]:
        arr_sorted = sorted(arr)    # Useful when not needed to sort again when they have the same no. of bits
        arr_dict = {}

        # Construct arr_dict{} in such a way:
        # _[1] = [1,2,4,8]
        # _[2] = [3,5,7]
        for num in arr_sorted:
            no_of_1_bits = self.count_1_bits(num)
            if no_of_1_bits in arr_dict:
                arr_dict[no_of_1_bits].append(num)
            else:
                arr_dict[no_of_1_bits] = [num]
        
        # Sort by the number of 1 bits
        sorted_arr_dict = dict(sorted(arr_dict.items(), key=lambda item: item[0]))
        print(sorted_arr_dict)
        
        # Just keep on appending the main list iterating the dict
        result_list = []
        for val_list in sorted_arr_dict.values():
            result_list.extend(val_list)
        
        return result_list