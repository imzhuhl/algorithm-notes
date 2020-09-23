'''
Author       : Zhu Honglin
Date         : 2020-09-14 21:37:04
LastEditTime : 2020-09-14 21:37:50
'''

from typing import List

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        def find(x):
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]
        
        def union(x, y):
            x = find(x)
            y = find(y)
            if x != y:
                fa[x] = y

        fa = [i for i in range(len(M))]
        
        for i in range(len(M)):
            for j in range(i+1, len(M)):
                if M[i][j] == 1:
                    union(i, j)
        
        cnt = 0
        for i in range(len(M)):
            if fa[i] == i:
                cnt += 1
        
        return cnt