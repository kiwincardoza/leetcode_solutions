# Problem Title - Number of Students Doing Homework at a Given Time
# Date - 20260105

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        result_count = 0
        for startT, endT in zip(startTime, endTime):
            if (queryTime >= startT) and (queryTime <= endT):
                result_count += 1
        return result_count