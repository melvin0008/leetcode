# Definition for singly-linked list.

# class ListNode(object):

#     def __init__(self, x):

#         self.val = x

#         self.next = None



class Solution(object):

    def getIntersectionNode(self, headA, headB):

        """

        :type head1, head1: ListNode

        :rtype: ListNode

        """

        lA=0

        h=headA

        while(h):

            h=h.next

            lA+=1

        lB=0

        h=headB

        while(h):

            h=h.next

            lB+=1

        flag=0

        diff=abs(lA-lB)

        if lA > lB:

            for i in xrange(diff):

                headA=headA.next

        if lB > lA:

            for i in xrange(diff):

                headB=headB.next

        while headA and headB:

            if(headA==headB):

                return headA

            headA=headA.next

            headB=headB.next

        return None
