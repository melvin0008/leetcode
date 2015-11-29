class MinStack(object):

    def __init__(self):

        """

        initialize your data structure here.

        """

        self.st=[]

        self.minst=[]

        



    def push(self, x):

        """

        :type x: int

        :rtype: nothing

        """

        self.st.append(x)

        if self.minst  :

            if x<=self.minst[-1]:

                self.minst.append(x)

        else:

            self.minst.append(x)

            

    def pop(self):

        """

        :rtype: nothing

        """

        if self.st:

            temp=self.st[-1]

            self.st.pop()

            if self.minst and temp==self.minst[-1]:

                self.minst.pop()

            

        



    def top(self):

        """

        :rtype: int

        """

        if self.st:

            return self.st[-1]

        



    def getMin(self):

        """

        :rtype: int

        """

        if self.minst:

            return self.minst[-1]

        
