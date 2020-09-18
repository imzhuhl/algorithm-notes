# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        queue = collections.deque()
        queue.append(root)
        rst = []
        while len(queue) != 0:
            cur_level = []
            level_cnt = len(queue)
            for i in range(level_cnt):
                node = queue.popleft()
                cur_level.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            rst.append(cur_level)
        return rst[::-1]