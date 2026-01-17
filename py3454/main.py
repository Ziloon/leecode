from typing import List


class SegmentTree:
    def __init__(self, X):
        self.X = X
        self.n = len(X) - 1
        self.cnt = [0] * (4 * self.n)
        self.tree_len = [0.0] * (4 * self.n)

    def push_up(self, node, L, R):
        if self.cnt[node] > 0:
            self.tree_len[node] = float(self.X[R + 1] - self.X[L])
        elif L == R:
            self.tree_len[node] = 0.0
        else:
            self.tree_len[node] = self.tree_len[node * 2] + self.tree_len[node * 2 + 1]

    def update(self, node, L, R, qL, qR, val):
        if qL <= L and R <= qR:
            self.cnt[node] += val
        else:
            mid = (L + R) // 2
            if qL <= mid: self.update(node * 2, L, mid, qL, qR, val)
            if qR > mid: self.update(node * 2 + 1, mid + 1, R, qL, qR, val)
        self.push_up(node, L, R)


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        x_set = set()
        for x, y, l in squares:
            x_set.add(x)
            x_set.add(x + l)
        sorted_x = sorted(list(x_set))
        x_map = {val: i for i, val in enumerate(sorted_x)}

        events = []
        for x, y, l in squares:
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))
        events.sort()

        st = SegmentTree(sorted_x)
        total_area = 0.0
        pre_y = events[0][0]

        for cur_y, type, x1, x2 in events:
            if cur_y > pre_y:
                total_area += st.tree_len[1] * (cur_y - pre_y)
            st.update(1, 0, st.n - 1, x_map[x1], x_map[x2] - 1, type)
            pre_y = cur_y

        target_area = total_area / 2.0
        current_area = 0.0
        st = SegmentTree(sorted_x)
        pre_y = events[0][0]

        for cur_y, type, x1, x2 in events:
            if cur_y > pre_y:
                layer_area = st.tree_len[1] * (cur_y - pre_y)
                if current_area + layer_area >= target_area:
                    return pre_y + (target_area - current_area) / st.tree_len[1]

                current_area += layer_area
            st.update(1, 0, st.n - 1, x_map[x1], x_map[x2] - 1, type)
            pre_y = cur_y
        return float(pre_y)


def test_solution():
    test_cases = [
        {
            "name": "示例 1: 垂直分离",
            "input": [[0, 0, 1], [2, 2, 1]],
            "expected": 1.00000
        },
        {
            "name": "示例 2: 内部包含/重叠",
            "input": [[0, 0, 2], [1, 1, 1]],
            "expected": 1.00000
        },
        {
            "name": "重叠且水平错开",
            "input": [[0, 0, 2], [1, 0, 2]],  # x从0-2和1-3，总x宽度是3
            "expected": 1.00000
        },
        {
            "name": "大数据范围测试",
            "input": [[522261215, 954313664, 225462], [628661372, 718610752, 10667]],
            "expected": None  # 用于观察输出
        }
    ]

    for case in test_cases:
        # 假设你的函数名为 separate_squares
        result = Solution().separateSquares(case["input"])
        print(f"Case {case['name']}: Result = {result:.5f}, Expected = {case['expected']}")
        print(f"准备运行测试: {case['name']}")


if __name__ == "__main__":
    test_solution()
