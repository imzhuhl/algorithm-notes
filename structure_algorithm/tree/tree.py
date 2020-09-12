'''
Author       : Zhu Honglin
Date         : 2020-09-12 21:08:40
LastEditTime : 2020-09-12 22:05:39
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
        pass

    def print_tree(self, root: TreeNode):
        queue = collections.deque()

        queue.append(root)
        while len(queue) > 0:
            node = queue.popleft()
            print(node, end=': ')
            if node.left is not None:
                queue.append(node.left)
                print(node.left, end=' ')
            
            if node.right is not None:
                queue.append(node.right)
                print(node.left, end=' ')

            print('')
        


