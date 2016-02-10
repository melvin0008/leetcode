# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        prev=None
        prevhead=head
        i=1
        while(i!=m and head):
            prev=head
            head=head.next
            i+=1
        p=head
        q=p.next
        while(i<n and q):
            i+=1
            temp=q.next
            q.next=p
            p=q
            q=temp
        head.next=q
        if prev:
            prev.next=p
        if m==1:
            prevhead.next=q
            return p
        return prevhead
        
            
