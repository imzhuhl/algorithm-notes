from typing import List

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        rst = 0
        for i in range(len(nums)):
            cnt = 0
            for j in range(i, len(nums)):
                cnt += nums[j]
                if cnt >= lower and cnt <= upper:
                    rst += 1
        return rst


class Solution1:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        pass

