# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        iter=head
        while iter:
            nod=iter
            while nod:
                if nod.next==iter.next:
                   nod=nod.next
                   continue
                if nod.val==iter.val:
                    iter.next=nod.next
                    nod=nod.next
                else:
                    break

            iter=iter.next
        return head