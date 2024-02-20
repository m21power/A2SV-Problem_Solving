# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.head=None
    def linking(self,data):
        new=ListNode(data)
        if self.head is None:
            self.head=new
            return
        iter=self.head
        while iter.next:
            iter=iter.next
        iter.next=new

    def partition(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        gr=[]
        ls=[]
        iter=head
        while iter:
            if iter.val<k:
                ls.append(iter.val)
            else:
                gr.append(iter.val)
            iter=iter.next
        lis=ls+gr
        for i in lis:
            self.linking(i)
        return self.head
        