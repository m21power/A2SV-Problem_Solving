# Problem: Merge Nodes in Between Zeros - https://leetcode.com/problems/merge-nodes-in-between-zeros

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.root = ListNode()
    def inserting(self,val,root):
        node = ListNode(val)
        root.next = node
        return node
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        iter = head
        sum = 0
        cur = self.root
        while iter:
            if iter.val == 0:
                cur = self.inserting(sum,cur)
                sum = 0
            else:
                sum += iter.val
            iter = iter.next
        return self.root.next.next


        

        