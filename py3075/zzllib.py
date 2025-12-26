from typing import List

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        total_happiness = 0
        for i in range(k):
            curr_happiness = happiness[i] - i
            if curr_happiness <= 0:
                return total_happiness
            else:
                total_happiness += curr_happiness
        return total_happiness