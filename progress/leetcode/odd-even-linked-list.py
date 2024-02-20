# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        oddptr=head
        evenptr=head.next
        even=head.next
        while evenptr and evenptr.next:
            oddptr.next=oddptr.next.next
            oddptr=oddptr.next
            evenptr.next=evenptr.next.next
            evenptr=evenptr.next

        oddptr.next=even
        return head 



        
        