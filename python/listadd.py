class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry=0
        start=1
        head=ListNode(0)
        while(l1 or l2 or carry):
            sum1=carry
            if l1:
                sum1+=l1.val
                l1=l1.next
            if l2:
                sum1+=l2.val
                l2=l2.next
            s,carry=sum1%10,sum1/10
            if(start!=1):
                head.next=ListNode(s)
            else:
                head=ListNode(s)
                start+=1
        return head    
