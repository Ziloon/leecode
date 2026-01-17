from typing import List
import pytest


class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        if len(bottomLeft) != len(topRight):
            return 0
        qty = len(bottomLeft)
        common_side_max = 0
        for i in range(qty - 1):
            for j in range(i + 1, qty):
                common_bottom_l = (max(bottomLeft[i][0], bottomLeft[j][0]), max(bottomLeft[i][1], bottomLeft[j][1]))
                common_top_r = (min(topRight[i][0], topRight[j][0]), min(topRight[i][1], topRight[j][1]))
                common_side = min(max(common_top_r[0] - common_bottom_l[0], 0),
                                  max(common_top_r[1] - common_bottom_l[1], 0))
                if common_side > common_side_max:
                    common_side_max = common_side
        return common_side_max * common_side_max


@pytest.mark.parametrize("bottomLeft, topRight, expected", [
    (
            [[1, 1], [2, 2], [3, 1]],
            [[3, 3], [4, 4], [6, 6]],
            1
    ),
    (
            [[1, 1], [3, 3]],
            [[2, 2], [4, 4]],
            0
    ),
    (
            [[1, 1], [1, 1]],
            [[5, 5], [5, 5]],
            16
    ),
    (
            [[1, 1], [1, 10]],
            [[10, 2], [10, 11]],
            0
    ),
    (
            [[1, 1], [2, 2], [1, 2]],
            [[3, 3], [4, 4], [3, 4]],
            1
    ),
    (
            [[1, 1], [3, 3], [3, 1]],
            [[2, 2], [4, 4], [4, 2]],
            0
    )
])
def test_largest_square_area(bottomLeft, topRight, expected):
    assert Solution().largestSquareArea(bottomLeft, topRight) == expected
