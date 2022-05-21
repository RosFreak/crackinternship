# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr= head
        c=0
        while(curr.next!=None):
            c+=1
            curr=curr.next
        c+=1
        curr=head
        for i in range(c//2):
            curr = curr.next
        return curr