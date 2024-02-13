# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pt=ListNode()
        ptr=pt
        
        iter1=list1
        iter2=list2
        while iter1 and iter2:
            if iter1.val < iter2.val:
                ptr.next=iter1
                iter1=iter1.next
            else:
                ptr.next=iter2
                iter2=iter2.next
            ptr=ptr.next
        if iter1:
            ptr.next=iter1
        elif iter2:
            ptr.next=iter2
        return pt.next