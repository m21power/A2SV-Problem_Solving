# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        iter=head
        l=0
        while iter:
            l+=1
            iter=iter.next
        res=[]
        curr=head
        base,remainder=l//k,l%k
        for i in range(k):
            res.append(curr)
            for j in range(base-1+(1 if remainder else 0)):
                if not curr:
                    break
                else:
                    curr=curr.next
            remainder-=(1 if remainder else 0)
            if curr:
                curr.next,curr=None,curr.next
                #curr,curr.next = curr.next,None are not the same 
        return res

