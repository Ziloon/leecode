from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        sum = 0
        negtive_cnt = 0
        num_min = float('inf')
        for row in matrix:
            for num in row:
                num_abs = abs(num)
                sum += num_abs
                if num < 0:
                    negtive_cnt += 1
                if num_abs < num_min:
                    num_min = num_abs
        if negtive_cnt % 2 == 0:
            return sum
        else:
            return sum - num_min * 2
