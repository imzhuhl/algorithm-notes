from typing import List

class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        table = {}
        for v in nums:
            if v in table:
                return v
            else:
                table[v] = 1


class Solution2:
    def findRepeatNumber(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if i == nums[i]:
                i += 1
                continue
            v = nums[i]
            if v == nums[v]:
                return v
            nums[i], nums[v] = nums[v], nums[i]



if __name__ == '__main__':
    nums = [2, 3, 1, 0, 2, 5, 3]
    sl = Solution2()
    print(sl.findRepeatNumber(nums))
