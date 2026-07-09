class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows=len(matrix)
        coulmn=len(matrix[0])
        if rows==coulmn:
            for r in range(rows):
                for c in range(coulmn):
                    if r<=c:
                        matrix[r][c],matrix[c][r]=matrix[c][r],matrix[r][c]
            return matrix
        
        ans = [[0] * rows for _ in range(coulmn)]
        for r in range(rows):
            for c in range(coulmn):
                    ans[c][r]=matrix[r][c]
        return ans 