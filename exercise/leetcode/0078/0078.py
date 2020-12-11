from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrace(cur_i):
            for i in range(cur_i, len(nums)):
                path.append(nums[i])
                rst.append(path[:])
                backtrace(i+1)
                path.pop()

        path = []
        rst = [[]]
        backtrace(0)
        return rst


if __name__ == '__main__':
    nums = [1,2,3]
    print(Solution().subsets(nums))