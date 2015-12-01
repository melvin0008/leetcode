class Solution(object):

    def countPrimes(self, n):

        """

        :type n: int

        :rtype: int

        2 3 5  7   

        """

        c=0

        if n<=1:

            return 0

        l=[True]*n

        for i in xrange(2,n):

            if l[i]==True:

                c+=1

                for j in xrange(2*i,n,i):

                    l[j]=False

        return c
