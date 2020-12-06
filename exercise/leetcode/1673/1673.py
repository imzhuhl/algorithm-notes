from typing import List

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        abandon = len(nums) - k

        for x in nums:
            while len(stack) > 0 and stack[-1] > x and abandon > 0:
                stack.pop()
                abandon -= 1
            stack.append(x)
        return stack[:k]

if __name__ == '__main__':
    nums = [2,4,3,3,5,4,9,6]
    k = 2
    Solution().mostCompetitive(nums, k)
