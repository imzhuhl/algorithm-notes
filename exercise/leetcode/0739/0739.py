from typing import List
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        rst = [0 for _ in range(len(T))]
        for i in range(len(T)):
            while len(stack) != 0 and T[i] > stack[-1][1]:
                info = stack.pop()
                rst[info[0]] = i - info[0]
            stack.append((i, T[i]))
        
        for rest in stack:
            rst[rest[0]] = 0

        return rst