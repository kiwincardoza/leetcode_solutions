# Problem Title - Kids With Greatest Number of Candies
# Date - 20260102

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_num = max(candies)  # Store the max candy in existing list
        added_candies = [candy+extraCandies for candy in candies]
        result_list = []
        # Now compare max candy with the added candies
        for candy in added_candies:
            if candy >= max_num:
                result_list.append(True)
            else:
                result_list.append(False)
        return result_list