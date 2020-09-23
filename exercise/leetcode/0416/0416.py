'''
Author       : Zhu Honglin
Date         : 2020-09-14 17:14:18
LastEditTime : 2020-09-14 19:13:23
'''

from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort()
        s = sum(nums)
        if s % 2 != 0:
            return False
        target = s // 2
        return self.dfs(0, target, nums)

    def dfs(self, cur, rest, nums):
        for i in range(cur, len(nums)):
            if i > cur and nums[i] == nums[i-1]:
                continue
            if nums[i] > rest:
                break
            if nums[i] == rest:
                return True
            ret = self.dfs(i+1, rest-nums[i], nums)
            if ret:
                return True

        return False


if __name__ == '__main__':
    sl = Solution()
    print(sl.canPartition([1, 2, 5]))
