# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        '''iter1=headA
        off =True
        while iter1 and off:
            iter2=headB
            while iter2 and off:
                if iter1==iter2:
                    off=False
                    return iter1
                iter2=iter2.next
            iter1=iter1.next
        return None'''

        lis=set()
        iterA=headA
        iterB=headB
        while iterA:
            lis.add(iterA)
            iterA=iterA.next
        while iterB:
            if iterB in lis:
                return iterB
            iterB=iterB.next
        return None


        
        
