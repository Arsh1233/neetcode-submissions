class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        R=len(matrix)
        C=len(matrix[0])
        for i in range(R):
            for j in range(i,C):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(R):
            matrix[i][::]=matrix[i][::-1]
