import unittest
from zzllib import minimumBoxes  # 请将your_module替换为实际的模块名


class TestMinimumBoxes(unittest.TestCase):

    def test_example_1(self):
        """测试示例1"""
        apple = [1, 3, 2]
        capacity = [4, 3, 1, 5, 2]
        self.assertEqual(minimumBoxes(apple, capacity), 2)

    def test_example_2(self):
        """测试示例2"""
        apple = [5, 5, 5]
        capacity = [2, 4, 2, 7]
        self.assertEqual(minimumBoxes(apple, capacity), 4)

    def test_single_apple_single_box(self):
        """测试单个苹果和单个箱子"""
        apple = [5]
        capacity = [5]
        self.assertEqual(minimumBoxes(apple, capacity), 1)

    def test_single_apple_multiple_boxes(self):
        """测试单个苹果和多个箱子"""
        apple = [3]
        capacity = [1, 2, 3, 4]
        self.assertEqual(minimumBoxes(apple, capacity), 1)

    def test_multiple_apples_single_box(self):
        """测试多个苹果和单个箱子（刚好装下）"""
        apple = [2, 2, 2]
        capacity = [6]
        self.assertEqual(minimumBoxes(apple, capacity), 1)

    def test_exact_capacity_match(self):
        """测试总容量刚好等于苹果总数"""
        apple = [1, 2, 3, 4]
        capacity = [10, 5, 3]
        self.assertEqual(minimumBoxes(apple, capacity), 1)

    def test_need_all_boxes(self):
        """测试需要使用所有箱子"""
        apple = [10, 10]
        capacity = [1, 2, 3, 4, 5, 5]
        self.assertEqual(minimumBoxes(apple, capacity), 6)

    def test_large_numbers(self):
        """测试较大的数值"""
        apple = [50, 50, 50]
        capacity = [50, 50, 50, 50]
        self.assertEqual(minimumBoxes(apple, capacity), 3)

    def test_unsorted_capacity(self):
        """测试未排序的容量数组"""
        apple = [4, 4, 4]
        capacity = [3, 7, 2, 5]
        self.assertEqual(minimumBoxes(apple, capacity), 2)  # 7 + 5 = 12

    def test_edge_case_min_values(self):
        """测试边界情况 - 最小值"""
        apple = [1, 1]
        capacity = [1, 1, 1]
        self.assertEqual(minimumBoxes(apple, capacity), 2)

    def test_edge_case_max_values(self):
        """测试边界情况 - 最大值"""
        apple = [50] * 50  # 50个50
        capacity = [50] * 50  # 50个50
        self.assertEqual(minimumBoxes(apple, capacity), 50)

    def test_one_by_one_filling(self):
        """测试需要逐个箱子填充的情况"""
        apple = [1, 1, 1, 1, 1]
        capacity = [1, 1, 1, 1, 1, 1]
        self.assertEqual(minimumBoxes(apple, capacity), 5)


if __name__ == '__main__':
    unittest.main()