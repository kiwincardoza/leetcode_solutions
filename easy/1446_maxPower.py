# Problem Title - Consecutive Characters
# Date - 20260105

class Solution:
    def maxPower(self, s: str) -> int:
        """
        Traverses the chars, and reset the counts when the next char is different.
        Keeps track of the max count, and returns that.
        """

        counter = 1
        result_max_count = 1
        prev_char = s[0]

        for char in s[1:]:
            if char == prev_char:
                counter += 1
            else:
                if result_max_count < counter:
                    result_max_count = counter
                counter = 1
            prev_char = char
        
        # To check for the remaining set of chars.
        if result_max_count < counter:
            result_max_count = counter
        return result_max_count
