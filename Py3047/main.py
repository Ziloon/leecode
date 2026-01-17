from typing import List
import pytest


class SegmentTree:
    def __init__(self, size):
        self.size = size
        self.cnt = [0] * (4 * size)
        self.max_cnt = [0] * (4 * size)

    def update(self, v, tl, tr, l, r, add):
        if l > r:
            return
        if l == tl and r == tr:
            self.cnt[v] += add
        else:
            tm = (tl + tr) // 2
            self.update(2 * v, tl, tm, l, min(r, tm), add)
            self.update(2 * v + 1, tm + 1, tr, max(l, tm + 1), r, add)

        # 核心逻辑：当前节点的 max_cnt 等于自身的完整覆盖次数加上子节点的最大值
        if tl != tr:
            self.max_cnt[v] = self.cnt[v] + max(self.max_cnt[2 * v], self.max_cnt[2 * v + 1])
        else:
            self.max_cnt[v] = self.cnt[v]

    def get_max(self):
        return self.max_cnt[1]

class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        def check(l):
            if l == 0: return True

            # 1. 过滤：只保留能容纳边长 L 的矩形
            rects = []
            for i in range(n):
                w = topRight[i][0] - bottomLeft[i][0]
                h = topRight[i][1] - bottomLeft[i][1]
                if w >= l and h >= l:
                    # 存储转换后的 y 区间 [y1, y2 - L]
                    rects.append((bottomLeft[i][0], topRight[i][0], bottomLeft[i][1], topRight[i][1] - l))

            if not rects: return False

            # 2. 离散化 y 坐标 📍
            y_coords = set()
            for _, _, y1, y2_L in rects:
                y_coords.add(y1)
                y_coords.add(y2_L)
            sorted_y = sorted(list(y_coords))
            y_map = {val: i for i, val in enumerate(sorted_y)}
            m = len(sorted_y)

            # 3. 扫描线准备 🧹
            # 按左边界 x1 排序
            rects.sort()
            tree = SegmentTree(m)

            # 存储所有事件：(x坐标, 类型[入/出], y1索引, y2_L索引)
            # 窗口逻辑：当处理矩形 i 时，窗口内必须是那些 x2 >= x1_i + L 的矩形
            # 这里用更简单的做法：把每个矩形拆成两个 x 事件
            events = []
            for x1, x2, y1, y2_L in rects:
                # 入场：在 x1 处增加覆盖
                events.append((x1, 1, y1, y2_L))
                # 出场：在 x2 - L 处移除覆盖（因为过了这个点，重叠宽度就不足 L 了）
                if x2 - l >= x1:
                    events.append((x2 - l, -1, y1, y2_L))

            # 再次按 x 排序，若 x 相同，先处理“入场” (+1)
            events.sort(key=lambda x: (x[0], -x[1]))

            for _, type, y1, y2_L in events:
                tree.update(1, 0, m - 1, y_map[y1], y_map[y2_L], type)
                if tree.get_max() >= 2:
                    return True
            return False

        # 二分查找最大边长 L
        low, high = 0, 10 ** 7
        ans_L = 0
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans_L = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans_L * ans_L

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
