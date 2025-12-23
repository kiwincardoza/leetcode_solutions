# Problem Title - Distance Between Bus Stops
# Date - 20251223

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start == destination:     # Base case
            return 0
        start_dest_dist = 0
        dest_start_dist = 0
        n = len(distance)
        
        # Traverse round robin fashion to avoid checking if start<dest or vice-versa
        # First compute start_dest_dist (start to destination distance)
        print("start_dest_dist")
        i = start
        while i != destination:
            print(i)
            start_dest_dist += distance[i]
            i = (i+1)%n

        # Next compute dest_start_dist (destination to start distance)
        print("dest_start_dist")
        i = destination
        while i != start:
            print(i)
            dest_start_dist += distance[i]
            i = (i+1)%n
        
        return min(start_dest_dist, dest_start_dist)
