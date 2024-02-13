# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        iter=head
        lis=[]
        num=0
        while iter:
            lis.append(iter.val)
            iter=iter.next
        n=len(lis)-1
        for i in lis:
            num+=(i)*pow(2,n)
            n-=1
        return num
        
        