# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        s=0
        curr=head
        while(curr!=None):
            s=s*10 + curr.val
            curr=curr.next
        ans=0
        i=0
        while(s):
            ans+= (s%10)*(2**i)
            i+=1
            s=s//10
        return ans
