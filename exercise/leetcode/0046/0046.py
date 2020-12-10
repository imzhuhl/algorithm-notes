from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack():
            if len(path) == len(nums):
                rst.append(path[:])

            for i in nums:
                if i in path:
                    continue
                path.append(i)
                backtrack()
                path.pop()

        path = []
        rst = []
        backtrack()
        return rst
