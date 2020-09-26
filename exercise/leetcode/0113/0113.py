# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        rst = []
        path = []

        def dfs(cur_sum, node):
            n = cur_sum+node.val
            path.append(node.val)

            if node.left is None and node.right is None:
                if n == sum:
                    rst.append(path.copy())
            
            if node.left is not None:
                dfs(n, node.left)
            
            if node.right is not None:
                dfs(n, node.right)
            
            path.pop()
        
        if root is None:
            return []
        dfs(0, root)
        return rst