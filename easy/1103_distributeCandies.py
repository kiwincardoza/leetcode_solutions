# Problem Title - Distribute Candies To People
# Date - 20251201

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        result_list = [0]*num_people
        sum_till_now = 1
        current_index = 0
        current_sum = 1
        prev_sum_till_now = 0
        while sum_till_now <= candies:
            result_list[current_index%num_people] += current_sum
            current_index += 1
            current_sum += 1
            prev_sum_till_now = sum_till_now
            sum_till_now += current_sum
        result_list[current_index%num_people] += (candies-prev_sum_till_now)

        return result_list