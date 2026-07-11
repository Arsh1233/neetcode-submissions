class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top,low= 0,0
        bot,high=len(matrix)-1,len(matrix[0])-1
        while top<=bot:
            row=int((top+bot)/2)
            if matrix[row][high]<target:
                top=row+1
            elif matrix[row][low]>target:
                bot=row-1
            else:
                break
        while low<=high:
            mid=int((low+high)/2)
            if matrix[row][mid]==target:
                return True
            elif matrix[row][mid]<target:
                low=mid+1
            else:
                high=mid-1
        return False                
