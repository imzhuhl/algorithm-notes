

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_val = [-1000]

        def dfs(r):
            if r is None:
                return 0

            l_p_val = max(0, dfs(r.left))
            r_p_val = max(0, dfs(r.right))
            cur_val = r.val
            max_val[0] = max(max_val[0], l_p_val+r_p_val+cur_val)

            return cur_val + max(r_p_val, l_p_val)

        dfs(root)
        return max_val[0]