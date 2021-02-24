from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.flip1(matrix)
        self.flip2(matrix)

    
    def flip1(self, matrix: List[List[int]]):
        """斜对角线翻转"""
        n = len(matrix)
        for i in range(n):
            for j in range(n-i):
                matrix[i][j], matrix[n-1-j][n-1-i] = matrix[n-1-j][n-1-i], matrix[i][j]
    
    def flip2(self, matrix):
        n = len(matrix)
        start, end = 0, n-1
        while start < end:
            for j in range(n):
                matrix[start][j], matrix[end][j] = matrix[end][j], matrix[start][j]
            start += 1
            end -= 1