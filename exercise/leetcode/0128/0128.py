from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
            
        s = set()
        for i, v in enumerate(nums):
            s.add(v)

        max_len = 1
        for i, v in enumerate(nums):
            if v-1 in s:
                continue
            t = v + 1
            cnt = 1
            while t in s:
                t += 1
                cnt += 1
            max_len = max(max_len, cnt)
        
        return max_len