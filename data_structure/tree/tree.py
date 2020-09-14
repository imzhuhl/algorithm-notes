'''
Author       : Zhu Honglin
Date         : 2020-09-12 21:08:40
LastEditTime : 2020-09-13 14:34:35
'''

from typing import List
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Utils:
    def build_tree_from_lst(self, val_lst: List[int]) -> TreeNode:
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

    def display_binary_tree(self, root: TreeNode):
        """
        输出二叉树
        """
        print('{:^8}|{:^8}|{:^8}'.format('father', 'left', 'right'))
        queue = collections.deque()
        queue.append(root)
        while len(queue) > 0:
            node = queue.popleft()
            fav = node.val
            lv = '#'
            rv = '#'
            if node.left:
                queue.append(node.left)
                lv = node.left.val
            
            if node.right:
                queue.append(node.right)
                rv = node.right.val
            
            print('{:^8}|{:^8}|{:^8}'.format(fav, lv, rv))


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
    utils = Utils()
    root = utils.build_tree_from_lst([10, 54, 234, -1, 9, -1, -1])
    utils.display_binary_tree(root)

    print('inorder traversal: {}'.format(inorder_traversal(root)))
    
