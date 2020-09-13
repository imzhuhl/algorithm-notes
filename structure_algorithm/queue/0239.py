'''
Author       : Zhu Honglin
Date         : 2020-09-13 19:39:31
LastEditTime : 2020-09-13 20:09:52
'''

from typing import List
import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = collections.deque()
        rst = []

        for i in range(k-1):
            while len(queue) > 0 and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
        
        for i in range(k-1, len(nums)):
            while len(queue) > 0 and queue[0] <= i-k:
                queue.popleft()

            while len(queue) > 0 and nums[queue[-1]] < nums[i]:
                queue.pop()
            
            queue.append(i)
            rst.append(nums[queue[0]])
        
        return rst