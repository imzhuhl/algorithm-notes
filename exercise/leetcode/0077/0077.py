from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        rst = []
        path = []

        def backtrace(cur_num):
            if len(path) + n - cur_num + 1 < k:  # 剪枝
                return

            if len(path) == k:
                rst.append(path[:])
            
            for i in range(cur_num, n+1):
                path.append(i)
                backtrace(i+1)
                path.pop()
            
        backtrace(1)
        return rst


if __name__ == '__main__':
    print(Solution().combine(n=4, k=2))
