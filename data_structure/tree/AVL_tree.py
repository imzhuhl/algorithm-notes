'''
Author       : Zhu Honglin
Date         : 2020-09-23 21:11:09
LastEditTime : 2020-09-24 15:12:24
'''

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.count = 1
        self.left = None
        self.right = None
        self.height = 1


def height(node: TreeNode) -> int:
    if node is None:
        return 0
    return node.height


def left_rotate(node: TreeNode) -> TreeNode:
    k = node.left
    node.left = k.right
    k.right = node
    
    node.height = max(height(node.left), height(node.right)) + 1
    k.height = max(height(k.left), height(k.right)) + 1
    return k


def right_ratate(node: TreeNode) -> TreeNode:
    k = node.right
    node.right = k.left
    k.left = node
    
    node.height = max(height(node.left), height(node.right)) + 1
    k.height = max(height(k.left), height(k.right)) + 1
    return k


def insert(node, x) -> TreeNode:
    if node is None:
        return TreeNode(x)

    if node.val == x:
        node.count += 1
    elif node.val > x:  # left subtree
        node.left = insert(node.left, x)
        if height(node.left) - height(node.right) >= 2:
            if x < node.left.val:  # LL
                node = left_rotate(node)
            else:
                node.left = right_ratate(node.left)
                node = left_rotate(node)
    else:
        node.right = insert(node.right, x)
        if height(node.right) - height(node.left) >= 2:
            if x > node.right.val:  ## RR
                node = right_ratate(node)
            else:
                node.right = left_rotate(node.right)
                node = right_ratate(node)
                
    node.height = max(height(node.left), height(node.right)) + 1
    return node


def find(node, x):
    pass


def build_tree_from_lst(val_lst: List[int]) -> TreeNode:
    """
    根据数组创建一颗二叉树, 该数组是二叉树的层序遍历序列.
    数组的每一个元素是表示节点的 value (正整数), 不存在的节点用 -1 表示.
    """
    def create_tree(cur_id: int) -> TreeNode:
        if cur_id > len(val_lst):
            return None
        if val_lst[cur_id-1] == -1:
            return None
        node = TreeNode(val_lst[cur_id-1])
        left_id = cur_id * 2
        right_id = left_id + 1
        node.left = create_tree(left_id)
        node.right = create_tree(right_id)
        return node
    
    if len(val_lst) == 0:
        return None
    root = create_tree(1)
    return root


def traversal(root: TreeNode) -> List[int]:
    def dfs(node: TreeNode):
        if node is None:
            return
        preorder.append(node.val)
        dfs(node.left)
        inorder.append(node.val)
        dfs(node.right)

    preorder = []
    inorder = []
    
    dfs(root)
    return [preorder, inorder]


if __name__ == '__main__':
    nums = [9, 4, 8, 12, 1, 23]
    root = None
    for x in nums:
        root = insert(root, x)
        
    ret = traversal(root)
    print('preorder: {}'.format(ret[0]))
    print('inorder: {}'.format(ret[1]))

    