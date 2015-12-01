# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 1 2 3 3 2 1
# 1 2 3 1 2 3
class Solution(object):
    def reverse(self,head):
        p=None
        q=head
        while(q):
            temp=q.next
            q.next=p
            p=q
            q=temp
        return p
    
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        if not head.next:
            return True
        temp=head
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next
            fast=fast.next
        saveslow=slow
        mid=slow.next
        newmid=self.reverse(mid)
        saveslow.next=None
        while newmid and temp:
            if newmid.val!=temp.val:
                return False
            newmid=newmid.next
            temp=temp.next
        if (temp and temp.next) or newmid:
            return False
        return True
        
        
        
        
            
        
