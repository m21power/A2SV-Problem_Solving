# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.head=None
    def linking(self,val):
        new=ListNode(val)
        if self.head is None:
            self.head=new
            return
        iter=self.head
        while iter.next:
            iter=iter.next
        iter.next=new

    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lis=[]
        while head:
            lis.append(head.val)
            head=head.next
        lis.sort()
        for i in lis:
            self.linking(i)
        return self.head