# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None
        savehead=head
        while head.next:
            prev=head
            head=head.next
            if head.val==val:
                prev.next=head.next
                head.next=None
                head=prev
        if savehead.val==val:
            return savehead.next
        return savehead
                
            
