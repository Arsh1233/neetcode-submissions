class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def rev(nums,i,j):
            while i<=j:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1
            return nums
        i=0
        j=len(nums)-1
        k=(len(nums)-k)%len(nums)
        rev(nums,0,k-1)
        rev(nums,k,j)
        rev(nums,i,j)
        return nums
        