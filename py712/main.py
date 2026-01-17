import pytest


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        from functools import lru_cache
        @lru_cache(None)
        def dp(i, j):
            if i == 0:
                return sum(ord(c) for c in s2[:j])
            if j == 0:
                return sum(ord(c) for c in s1[:i])
            if s1[i-1] == s2[j-1]:
                return dp(i-1, j-1)
            else:
                return min(
                    dp(i-1,j) + ord(s1[i-1]),
                    dp(i, j-1) + ord(s2[j-1])
                )
        return dp(len(s1), len(s2))


@pytest.mark.parametrize("s1, s2, expected", [
    ("sea", "eat", 231),                # 示例 1: 删除 's' 和 't'
    ("delete", "leet", 403),            # 示例 2: 删除 'd', 'e', 'e', 'e'
    ("a", "b", 195),                    # 完全不同: 97 + 98 = 195
    ("", "at", 213),                    # s1 为空: 删除 'a'(97) + 't'(116) = 213
    ("same", "same", 0),                # 完全相同: 不需要删除
])

def test_minimum_delete_sum(s1, s2, expected):
    sol = Solution()
    assert sol.minimumDeleteSum(s1, s2) == expected