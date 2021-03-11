from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        st = []
        ln = len(height)
        cnt = 0
        for i in range(ln):
            while len(st) > 0 and height[st[-1]] < height[i]:
                d = height[st[-1]]
                st.pop()
                if len(st) == 0:
                    continue
                li = st[-1]
                mh = min(height[li], height[i])
                cnt += (mh - d) * (i - li - 1)
            st.append(i)

        return cnt