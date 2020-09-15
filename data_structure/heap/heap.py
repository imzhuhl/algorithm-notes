'''
Author       : Zhu Honglin
Date         : 2020-09-15 15:04:34
LastEditTime : 2020-09-15 15:12:50
'''

from typing import List


# 向上调整堆
def up(h: List[int], x: int):
    while x > 1 and h[x-1] > h[x//2-1]:
        h[x-1], h[x//2-1] = h[x//2-1], h[x-1]
        x = x // 2


# 向下调整堆
def down(h: List[int], x:int):
    while x * 2 <= len(h):
        t = x * 2;
        if t + 1 <= len(h) and h[t] > h[t-1]:
            t += 1
        if h[t-1] <= h[x-1]:
            break
        h[t-1], h[x-1] = h[x-1], h[t-1]
        x = t


if __name__ == '__main__':
    nums = [3, 2, 1, 5, 6, 4, 43, 5, 65, 90]
    
    # 用向下调整建堆
    for i in range(len(nums), 0, -1):
        down(nums, i)

    print(nums)
    

