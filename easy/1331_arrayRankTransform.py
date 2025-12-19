# Problem Title - Rank Transform of an Array
# Date - 20251217

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        unsorted_dict = {k: 0 for k in arr}
        # Sort dict by key
        sorted_dict = {k: v for k, v in sorted(unsorted_dict.items(), key=lambda item: item[0])}
        ind = 1
        # Assign rank in just ascending order
        for num, rank in sorted_dict.items():
            sorted_dict[num] = ind
            ind += 1

        print(f"sorted_dict: {sorted_dict}")
        result_list = []
        for num in arr:
            rank = sorted_dict[num]
            result_list.append(rank)
        return result_list