# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow= head
        try:
            fast = head.next
        except:
            return False
        while(slow!= None and fast!=None):
            if slow == fast:
                return True
            slow=slow.next
            try:
                fast = fast.next.next
            except:
                return False
        return False