# Problem Title - Nim Game
# Date - 20251221

class Solution:
    def canWinNim(self, n: int) -> bool:
        # Referred to Discussions tab in Leetcode
        if n%4 == 0:
            return False
        return True