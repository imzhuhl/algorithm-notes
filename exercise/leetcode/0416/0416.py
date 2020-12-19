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


class Solution2:
    """动态规划
    """
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:
            return False
        target = s // 2
        dp = [[False for _ in range(target+1)] for _ in range(len(nums) + 1)]
        for i in range(len(nums)+1):
            dp[i][0] = True
        for i in range(1, len(nums)+1):
            for j in range(1, target+1):
                if j - nums[i-1] < 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]

        return dp[-1][-1]


class Solution3:
    """动态规划 状态压缩
    """
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:
            return False
        target = s // 2
        dp = [False for _ in range(target+1)]
        dp[0] = True
        for i in range(1, len(nums)+1):
            for j in range(target, 0, -1):
                if j - nums[i-1] >= 0:
                    dp[j] = dp[j] or dp[j-nums[i-1]]

        return dp[-1]         


if __name__ == '__main__':
    sl = Solution3()
    print(sl.canPartition([1, 5, 11, 5]))
