from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ln = len(nums)
        # 以 index 为有边界的最大连续数组的乘积 
        max_dp = [i for i in nums]
        min_dp = [i for i in nums]

        for i in range(1, ln):
            mul_max = nums[i] * max_dp[i-1]
            mul_min = nums[i] * min_dp[i-1]
            max_dp[i] = max(nums[i], mul_max, mul_min)
            min_dp[i] = min(nums[i], mul_max, mul_min)

        return max(max_dp)