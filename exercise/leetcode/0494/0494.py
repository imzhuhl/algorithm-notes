from typing import List
import collections

class Solution:
    """回溯 O(2^n)
    """
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        def backtrace(i, cur_sum):
            nonlocal rst
            if i > len(nums) - 1:
                if cur_sum == S:
                    rst += 1
                return

            backtrace(i+1, cur_sum+nums[i])
            backtrace(i+1, cur_sum-nums[i])

        rst = 0
        backtrace(0, 0)
        return rst


class Solution2:
    """动态规划 O(n*const)
    """
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        n = len(nums)
        memo = [collections.defaultdict(int) for _ in range(n)]

        memo[0][nums[0]] += 1
        memo[0][-nums[0]] += 1
        for i in range(1, n):
            v = nums[i]
            for key, val in memo[i-1].items():
                x1 = key + v
                x2 = key - v
                memo[i][x1] += memo[i-1][key]
                memo[i][x2] += memo[i-1][key]

        rst = memo[n-1][S]
        return rst


if __name__ == '__main__':
    # nums = [40,2,49,50,46,6,5,23,38,45,45,17,4,26,40,33,14,9,37,24]
    # S = 7
    nums = [1, 1, 1, 1, 1]
    S = 3
    print(Solution2().findTargetSumWays(nums, S))
