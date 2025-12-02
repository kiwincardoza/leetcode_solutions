# Problem Title - Minimum Cost To Move The Chips To The Same Position
# Date - 20251202


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        # Below is my first solution
        """
        min_position = 1000000001
        max_position = 1
        max_chips_position_list = []
        position_dict = {}
        for pos in position:
            if pos in position_dict:
                position_dict[pos] += 1
            else:
                if pos < min_position:
                    min_position = pos
                if pos > max_position:
                    max_position = pos
                position_dict[pos] = 1
        sorted_position_dict = dict(sorted(position_dict.items(), key=lambda x: x[1], reverse=True))
        max_chips = list(sorted_position_dict.values())[0]

        print(f"sorted_position_dict: {sorted_position_dict}")
        print(f"max_chips: {max_chips}")
        for pos, chips in sorted_position_dict.items():
            if chips != max_chips:
                break
            max_chips_position_list.append(pos)
        
        total_chips = sum(list(position_dict.values()))
        min_cost = 1000000000

        print(f"max_chips_position_list: {max_chips_position_list}")
        print(f"position_dict: {position_dict}")

        for pos in max_chips_position_list:
            if pos-2 in position_dict:
                prev_cost = position_dict[pos-2]
            else:
                prev_cost = 0
            if pos+2 in position_dict:
                next_cost = position_dict[pos+2]
            else:
                next_cost = 0
            cost = total_chips - prev_cost - next_cost - position_dict[pos]
            if cost < min_cost:
                min_cost = cost

        return min_cost
        """

        odd_positioned_chips = 0
        even_positioned_chips = 0
        position_dict = {}
        for pos in position:
            if pos in position_dict:
                position_dict[pos] += 1
            else:
                position_dict[pos] = 1
        for pos, chips in position_dict.items():
            if pos%2 == 0:
                even_positioned_chips += chips
            else:
                odd_positioned_chips += chips

        return min(odd_positioned_chips, even_positioned_chips)    
            