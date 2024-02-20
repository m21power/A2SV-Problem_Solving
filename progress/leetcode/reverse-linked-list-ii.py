# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        prev,cur=dummy,head
        for i in range(left-1):
            prev,cur=cur,cur.next
        p=None
        for i in range(right-left+1):
            temp=cur.next
            cur.next=p
            p,cur=cur,temp
        prev.next.next=cur
        prev.next=p
        return dummy.next