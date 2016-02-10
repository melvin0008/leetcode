# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        hare,tort=head,head
        prev=None
        i=1
        j=1
        while(i!=n):
            hare=hare.next
            i+=1
            j+=1
        while(hare.next):
            prev=tort
            hare=hare.next
            tort=tort.next
            j+=1
        
        if tort==head:
            head=head.next
            tort.next=None
        if prev:
            prev.next=tort.next
            tort.next=None
        
        return head
