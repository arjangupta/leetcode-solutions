# https://leetcode.com/problems/koko-eating-bananas/
# Last attempted: 2024-02-15

from typing import List

class Solution:
    def eatAtRateK(self, rate: int, original_piles: List[int], h:int) -> bool:
        piles = original_piles.copy()
        # print(f"Given piles: {piles}")
        while h > 0:
            # Always choose the largest pile to eat first
            largest_pile = max(piles)
            largest_pile_idx = piles.index(largest_pile)
            piles[largest_pile_idx] = largest_pile - rate
            if max(piles) <= 0:
                return True
            h -= 1
            print(f"Piles: {piles}, remaining hours: {h}")
        return False
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        return self.minEatingSpeedK(max(piles), max(piles), piles, h)
    def minEatingSpeedK(self, curr_k:int, prev_k:int, piles: List[int], h: int) -> int:
        print(f"curr_k: {curr_k}, prev_k: {prev_k}")
        if self.eatAtRateK(curr_k, piles, h):
            # Decrease rate
            prev_k = curr_k
            curr_k = int(prev_k/2)
        else:
            # Increase rate
            diff = prev_k - curr_k
            if diff == 1:
                return prev_k
            elif diff == -1:
                return curr_k + 1
            elif diff == 0:
                return curr_k
            else:
                prev_k = curr_k
                curr_k = prev_k + int(abs(diff)/2)
        return self.minEatingSpeedK(curr_k,prev_k,piles,h)