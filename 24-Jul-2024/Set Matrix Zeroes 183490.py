# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def fun(row,col):
            for i in range(len(matrix[0])):
                if matrix[row][i] != 0:
                    matrix[row][i] = True
            for j in range(len(matrix)):
                if matrix[j][col] != 0:
                    matrix[j][col] = True
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] != True and matrix[r][c] == 0:
                    fun(r,c)
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if isinstance(matrix[r][c],bool):
                    matrix[r][c] = 0
        
        