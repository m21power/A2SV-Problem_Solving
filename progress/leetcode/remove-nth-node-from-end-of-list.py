# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c=0
        prev=None
        iter=head
        while iter:
            c+=1
            iter=iter.next
        iter=head
        if c==n:
            head=iter.next
            return head
        else:
            i=0
            iter=head
            while iter:
                i+=1
                if i==(c-n+1):
                    prev.next=iter.next
                    return head
                prev=iter
                iter=iter.next

        

        