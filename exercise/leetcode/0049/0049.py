from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tb = {}
        for i, s in enumerate(strs):
            tmp = list(s)
            tmp.sort()
            tmp = ''.join(tmp)
            if tmp in tb:
                tb[tmp].append(i)
            else:
                tb[tmp] = [i]
        rst = []
        for k, lst in tb.items():
            tmp = []
            for i in lst:
                tmp.append(strs[i])
            rst.append(tmp)
        return rst