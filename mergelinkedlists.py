# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        headA,headB=l1,l2
        Chead=None
        headC=None
        if not headA:
            return headB
        if not headB:
            return headA
        if headA.val <headB.val:
            headC=headA
            headA=headA.next
        else:
            headC=headB
            headB=headB.next
        
        Chead=headC
            
        while(headA and headB):
            if(headA.val<headB.val):
            	headC.next=headA
            	headC=headC.next
                headA=headA.next
            else:
            	headC.next=headB
            	headC=headC.next
                headB=headB.next
        while headA:
    		headC.next=headA
    		headA=headA.next
    		headC=headC.next
    	while headB:
    		headC.next=headB
    		headB=headB.next
    		headC=headC.next
        	
        return Chead# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        headA,headB=l1,l2
        Chead=None
        headC=None
        if not headA:
            return headB
        if not headB:
            return headA
        if headA.val <headB.val:
            headC=headA
            headA=headA.next
        else:
            headC=headB
            headB=headB.next
        
        Chead=headC
            
        while(headA and headB):
            if(headA.val<headB.val):
            	headC.next=headA
            	headC=headC.next
                headA=headA.next
            else:
            	headC.next=headB
            	headC=headC.next
                headB=headB.next
        while headA:
    		headC.next=headA
    		headA=headA.next
    		headC=headC.next
    	while headB:
    		headC.next=headB
    		headB=headB.next
    		headC=headC.next
        	
        return Chead
