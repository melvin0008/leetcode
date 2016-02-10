from collections import deque
class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.qA=deque([])
        self.qB=deque([])

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if(not self.qA):
            self.qA.appendleft(x)
            while(self.qB):
                self.qA.appendleft(self.qB.pop())
        else:
            self.qB.appendleft(x)
            while(self.qA):
                self.qB.appendleft(self.qA.pop())
        

    def pop(self):
        """
        :rtype: nothing
        """
        if self.qA:
            self.qA.pop()
        elif self.qB:
            self.qB.pop()
        else:
            raise Exception('Haha')
        

    def top(self):
        """
        :rtype: int
        """
        if self.qA:
            return self.qA[-1]
        elif self.qB:
            return self.qB[-1]
        else:
            raise Exception('Haha')
        

    def empty(self):
        """
        :rtype: bool
        """
        if not self.qA and not self.qB:
            return True
        return False