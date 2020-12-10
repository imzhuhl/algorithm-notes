from typing import List
import collections

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sums = [0 for _ in range(len(nums)+1)]
        for i in range(1, len(pre_sums)):
            pre_sums[i] = nums[i-1] + pre_sums[i-1]
        
        rst = 0
        for j in range(1, len(pre_sums)):
            for i in range(0, j):
                sum_i_j = pre_sums[j] - pre_sums[i]  # [i, j)
                if sum_i_j == k:
                    rst += 1

        return rst


class Solution2:
    """优化前缀和
    """
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sums = [0]
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            pre_sums.append(cur_sum)

        rst = 0
        pre_map = {}
        for j in range(0, len(pre_sums)):
            target = pre_sums[j] - k
            if target in pre_map:
                rst += pre_map[target]
            if pre_sums[j] in pre_map:
                pre_map[pre_sums[j]] += 1
            else:
                pre_map[pre_sums[j]] = 1

        return rst


if __name__ == '__main__':
    nums = [1, 1, 1]
    k = 2
    print(Solution2().subarraySum(nums, k))
