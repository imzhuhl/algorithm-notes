from typing import List
import bisect

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        zero = []
        lake_day = {}
        rst = [-1 for _ in range(len(rains))]

        for i, v in enumerate(rains):
            if v == 0:
                zero.append(i)
                rst[i] = 1
            else:
                if v in lake_day:
                    idx = bisect.bisect_left(zero, lake_day[v])
                    if idx == len(zero):
                        return []
                    rst[zero[idx]] = v
                    zero.pop(idx)
                lake_day[v] = i
        
        return rst


if __name__ == '__main__':
    rains = [1, 2, 0, 0, 2, 1]
    sl = Solution()
    print(sl.avoidFlood(rains))


            