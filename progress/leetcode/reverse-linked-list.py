# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        iter=head
        while iter:
            next=iter.next
            iter.next=prev
            prev=iter
            iter=next
        head=prev
        return head
  