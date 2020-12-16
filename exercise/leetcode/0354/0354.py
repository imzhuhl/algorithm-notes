from typing import List

class Solution:
    def bigger_than(self, a: List[int], b: List[int]):
        if a[0] > b[0] and a[1] > b[1]:
            return True
        return False

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        is_head = [1 for i in range(len(envelopes))]
        tree = {}

        for i in range(len(envelopes)):
            tree[i] = []

        for i in range(len(envelopes)):
            a = envelopes[i]
            for j in range(len(envelopes)):
                b = envelopes[j]
                if self.bigger_than(a, b):
                    tree[i].append(j)
                    is_head[j] = 0
        
        dp = [0 for _ in range(len(envelopes))]
        
        def rec(x):
            if dp[x] != 0:
                return dp[x]
            max_len = 0
            for val in tree[x]:
                max_len = max(max_len, rec(val))
            dp[x] = max_len + 1
            return dp[x]
        
        rst = 0
        for i in range(len(is_head)):
            if is_head[i] == 1:
                rst = max(rst, rec(i))
        return rst


class Solution2:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        height = [i[1] for i in envelopes]
        dp = [1 for _ in range(len(height))]
        rst = 0
        for i in range(len(dp)):
            for j in range(i):
                if height[i] > height[j]:
                    dp[i] = max(dp[j]+1, dp[i])
            if rst < dp[i]:
                rst = dp[i]
        return rst


if __name__ == '__main__':
    envelopes = [[5,4],[6,4],[6,7],[2,3]]
    print(Solution2().maxEnvelopes(envelopes))
