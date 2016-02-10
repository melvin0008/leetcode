class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """ 
        if not head:
            return None
        savehead=head
        while head.next:
            prev=head
            head=head.next
            if prev.val==head.val:
                prev.next=head.next
                head.next=None
                head=prev
        return savehead
