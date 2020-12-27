from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda a: a[1])
        cur_end = intervals[0][1]
        count = 1
        for item in intervals:
            if item[0] >= cur_end:
                count += 1
                cur_end = item[1]

        return len(intervals) - count



if __name__ == '__main__':
    a = []
    b = None
    if a:
        print('if a')
    if a is not None:
        print('if a is not None')
    
