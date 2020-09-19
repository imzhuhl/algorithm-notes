"""
这题用拓扑排序的解法
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[0 for i in range(numCourses)] for i in range(numCourses)]
        indegree = [0 for i in range(numCourses)]

        for item in prerequisites:
            start = item[1]
            end = item[0]
            graph[start][end] = 1
            indegree[end] += 1
        
        s = set()
        for i in range(numCourses):
            if indegree[i] == 0:
                s.add(i)
        
        rst = []
        while len(s) != 0:
            n = s.pop()
            rst.append(n)
            for i in range(numCourses):
                if graph[n][i] != 0:
                    graph[n][i] = 0
                    indegree[i] -= 1
                    if indegree[i] == 0:
                        s.add(i)
        
        if len(rst) != numCourses:
            return False
        return True
