from typing import List
import random


class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        
    def pick(self, target: int) -> int:
        i = 0
        rst = -1
        for idx, item in enumerate(self.nums):
            if target == item:
                i += 1
                if random.randint(1, i) == 1:
                    rst = idx
        return rst