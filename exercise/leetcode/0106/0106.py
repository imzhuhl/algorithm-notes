from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        return self.dfs(inorder, postorder, 0, len(inorder)-1, 0, len(postorder)-1)

    def dfs(self, inorder, postorder, inleft, inright, postleft, postright) -> TreeNode:
        if inleft > inright:
            return None

        root_val = postorder[postright]
        inidx = inleft
        while inorder[inidx] != root_val:
            inidx += 1
        root = TreeNode(root_val)
        offset = inidx - inleft
        root.left = self.dfs(inorder, postorder, inleft, inidx-1, postleft, postleft+offset-1)
        root.right = self.dfs(inorder, postorder, inidx+1, inright, postleft+offset, postright-1)
        return root


class Solution2:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        inmap = {v: k for k, v in enumerate(inorder)}

        def dfs(inleft, inright, postleft, postright) -> TreeNode:
            if inleft > inright:
                return None
            val = postorder[postright]
            root = TreeNode(val)
            idx = inmap[val]
            root.left = dfs(inleft, idx-1, postleft, postleft+idx-inleft-1)
            root.right = dfs(idx+1, inright, postleft+idx-inleft, postright-1)
            return root
        
        return dfs(0, len(inorder)-1, 0, len(postorder)-1)
        