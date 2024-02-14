# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        iter=head
        l=[]
        off=True
        of = True
        a=None
        i=0
        while iter and off:
            l.append(iter)
            iter=iter.next
            if iter in l:
                off=False
                a=iter
                it=head
                while it and of:
                    if it.next==a:
                        of=False
                        return a
                    it=it.next
                    i+=1
