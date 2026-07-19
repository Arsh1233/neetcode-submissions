class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        m = max(people)
        count = [0] * (m + 1)
        for p in people:
            count[p] += 1

        idx, i = 0, 1
        while idx < len(people):
            while count[i] == 0:
                i += 1
            people[idx] = i
            count[i] -= 1
            idx += 1
        l=0
        r=len(people)-1
        cnt=0
        while l<=r:
            if (people[l]+people[r])<=limit:
                cnt+=1
                l+=1
                r-=1
            elif (people[l]+people[r])>limit and people[r]<=limit:
                cnt+=1
                r-=1
            else:
                cnt+=1
                l+=1
        return cnt
            