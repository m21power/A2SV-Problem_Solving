# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l=[]
        li=[]
        iter=head
        while iter:
            l.append(iter.val)
            iter=iter.next
        iter=head
        prev=None
        while iter:
            n=iter.next
            iter.next=prev
            prev=iter
            iter=n
        head=prev
        it=head
        while it:
            li.append(it.val)
            it=it.next
        if li==l:
            return True
        else:
            return False

        