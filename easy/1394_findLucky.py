# Problem Title - Find Lucky Integer in an Array
# Date - 20251229

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr.sort()

        prev_num = arr[-1]
        count = 1

        # Traverse reverese from last second element
        for num in arr[:-1][::-1]:
            print(f"num: {num}")
            if prev_num == num: # If it matches the prev element, move on incrementing the count
                count += 1
            else:
                # If it does not match the prev element, then check if its a magic number, else reset the count
                if count == prev_num:
                    return prev_num
                count = 1
            prev_num = num
        
        # If the first element also is not magic, then return -1
        if count != arr[0]:
            return -1
        return count