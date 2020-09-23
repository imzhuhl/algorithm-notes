'''
Author       : Zhu Honglin
Date         : 2020-09-15 15:51:09
LastEditTime : 2020-09-15 15:59:38
'''

from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        for i in range(n, 0, -1):
            self.down(nums, n, i)
        
        for i in range(1, k):
            nums[0], nums[n-1] = nums[n-1], nums[0]
            n -= 1
            self.down(nums, n, 1)

        return nums[0]
    
    def down(self, h, n, x):
        while x * 2 <= n:
            t = x * 2;
            if t + 1 <= n and h[t] > h[t-1]:
                t += 1
            if h[t-1] <= h[x-1]:
                break
            h[t-1], h[x-1] = h[x-1], h[t-1]
            x = t


if __name__ == '__main__':
    sl = Solution()
    nums = [3,2,1,5,6,4]
    k = 2
    print(sl.findKthLargest(nums, k))
