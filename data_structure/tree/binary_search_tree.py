
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.count = 1
        self.left = None
        self.right = None


def insert(node, x):
    """插入节点，节点值为 x
    """
    if node is None:
        return

    if node.val == x:
        node.count += 1
    elif node.val > x:  # left subtree
        if node.left is None:
            node.left = TreeNode(x)
        else:
            insert(node.left, x)
    else:
        if node.right is None:
            node.right = TreeNode(x)
        else:
            insert(node.right, x)


def search(node, x) -> bool:
    if node is None:
        return False
    
    if node.val == x:
        return True
    
    if node.val > x:  # left
        return search(node.left, x)
    else:
        return search(node.right, x)


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


def inorder_traversal(root: TreeNode) -> List[int]:
    """二叉树的中序遍历
    """
    def dfs(node: TreeNode):
        if node is None:
            return
        dfs(node.left)
        rst.append(node.val)
        dfs(node.right)

    rst = []
    dfs(root)
    return rst


if __name__ == '__main__':
    nums = [9, 4, 32, 98, 1, 23]

    root = TreeNode(nums[0])
    for i in range(1, len(nums)):
        x = nums[i]
        insert(root, x)
    
    print(inorder_traversal(root))

    