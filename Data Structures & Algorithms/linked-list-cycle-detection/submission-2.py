# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hasmap={}
        curr=head
        while curr:
            if curr.val in hasmap and curr.next:
                return True
                break
            hasmap[curr.val]= 1
            curr=curr.next
        return False