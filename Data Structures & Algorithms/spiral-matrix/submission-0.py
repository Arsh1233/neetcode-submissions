class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        top=0
        bottom=len(matrix)
        left=0
        right=len(matrix[0])
        while left<right and top<bottom:
            #left to right
            i=left
            while i<right:
                res.append(matrix[top][i])
                i+=1
            top+=1
            #top to bottom
            i=top
            while i<bottom:
                res.append(matrix[i][right-1])
                i+=1
            right-=1   
                #right to left
            if top<bottom:
                i=right-1
                while i>=left:
                    res.append(matrix[bottom-1][i])
                    i-=1
                bottom-=1
                #bottom to top
            if left<right:
                i=bottom-1
                while i>=top:
                    res.append(matrix[i][left])
                    i-=1
                left+=1  
        return res