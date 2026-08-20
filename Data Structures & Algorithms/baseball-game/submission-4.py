class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans=[]
        for i in operations:
            if i == "+" and len(ans)>=2:
                res=ans[-1]+ans[-2]
                ans.append(res)
            elif i=="D" and ans:
                res=2*ans[-1]
                ans.append(res)
            elif i=="C" and len(ans)>=1:
                ans.pop()
            else:
                ans.append(int(i))
        return sum(ans)