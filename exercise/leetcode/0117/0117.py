

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        self.pre_node = None
        target = 1
        while True:
            self.dfs(1, target, root)
            if self.pre_node is None:
                break
            self.pre_node = None
            target += 1
        return root

    def dfs(self, level, target, node):
        if level == target:
            if self.pre_node is None:
                self.pre_node = node
            else:
                self.pre_node.next = node
                self.pre_node = node
            return
        
        if node.left is not None:
            self.dfs(level+1, target, node.left)
        if node.right is not None:
            self.dfs(level+1, target, node.right)


class Solution2:
    def connect(self, root: 'Node') -> 'Node':
        fa = root
        last = None
        newstart = None
        while fa is not None:
            while fa is not None:
                if fa.left is not None:
                    if newstart is None:
                        newstart = fa.left
                    if last is not None:
                        last.next = fa.left
                    last = fa.left    
                if fa.right is not None:
                    if newstart is None:
                        newstart = fa.right
                    if last is not None:
                        last.next = fa.right
                    last = fa.right
                fa = fa.next
            fa = newstart
            newstart = None
            last = None


