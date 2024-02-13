# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''iter=head
        l=[]
        off=True
        while iter and off:
            l.append(iter)
            iter=iter.next
            if iter in l:
                off=False
                return True
        return False
        '''
        tor=head
        rab=head
        while rab and rab.next:
            tor=tor.next
            rab=rab.next.next
            if tor==rab:
                return True
        return False