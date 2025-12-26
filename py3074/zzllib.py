from typing import List

def minimumBoxes(apple: List[int], capacity: List[int]) -> int:
    # 获取苹果总数
    apple_amount = sum(apple)
    # 如果没苹果，也不需要箱子
    if apple_amount <= 0:
        return 0
    # 降序排列箱子，保证大箱子先用，箱子数最少
    capacity.sort(reverse=True)
    for i,x in enumerate(capacity):
        apple_amount -= x
        if apple_amount <= 0:
            # 装完了，返回箱子序号+1，就是个数
            return i+1
    # 装不完，返回错误
    return -1