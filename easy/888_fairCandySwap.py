# Problem Title - Fair Candy Swap
# Date - 20251201

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        equal_candies = int((sum(aliceSizes)+sum(bobSizes))/2)
        diff_candies = abs(equal_candies-sum(aliceSizes))

        alice_total_candies = sum(aliceSizes)
        bob_total_candies = sum(bobSizes)

        # print(f"equal_candies: {equal_candies}")
        # print(f"diff_candies: {diff_candies}")

        alice_candies_sorted = sorted(aliceSizes)
        bob_candies_sorted = sorted(bobSizes)
        
        for alice_box in alice_candies_sorted:
            for bob_box in bob_candies_sorted:
                # print(f"alice_box: {alice_box}; bob_box: {bob_box}")
                if alice_total_candies < bob_total_candies:
                    # print(f"alice_box: {alice_box+diff_candies}; bob_box: {bob_box-diff_candies}")
                    if ((alice_box+diff_candies) == bob_box) and ((bob_box-diff_candies) == alice_box):
                        return [alice_box, bob_box]
                    elif (alice_box+diff_candies) < bob_box:
                        break
                elif bob_total_candies < alice_total_candies:
                    if ((alice_box-diff_candies) == bob_box) and ((bob_box+diff_candies) == alice_box):
                        return [alice_box, bob_box]
                    elif (bob_box+diff_candies) > alice_box:
                        break