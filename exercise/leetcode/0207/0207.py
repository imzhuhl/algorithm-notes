"""
两种思路：
1. 使用 BFS 
2. 使用 DFS
"""

import collections

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """BFS + queue
        """
        graph = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]

        for item in prerequisites:
            graph[item[1]].append(item[0])
            indegree[item[0]] += 1
        
        s = collections.deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                s.append(i)

        cnt = 0
        while s:
            n = s.popleft()
            cnt += 1
            for v in graph[n]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    s.append(v)
                
        return cnt == numCourses

    def canFinish2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """DFS + visit
        1. 为什么 visit 需要 -1，0，1 三种状态：
            暴力的 dfs 只需要两种状态 0 和 1，记录是否遍历过，但是为了节省时间，防止重复遍历，
            用第三种状态表示该节点在以前被遍历过，从该节点出发之后不可能有环，相当于已经被 check，
            就不用往下遍历了。
        """
        def dfs(cur) -> bool:
            if visit[cur] == 1:
                return False
            if visit[cur] == -1:
                return True
            
            visit[cur] = 1
            for v in graph[cur]:
                ret = dfs(v)
                if not ret:
                    return False
            visit[cur] = -1
            return True

        graph = [[] for _ in range(numCourses)]
        visit = [0 for _ in range(numCourses)]
        for item in prerequisites:
            graph[item[1]].append(item[0])

        for i in range(numCourses):
            ret = dfs(i)
            if not ret:
                return False
        return True