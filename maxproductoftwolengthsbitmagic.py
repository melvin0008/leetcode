

class Solution(object):

    def maxProduct(self, words):

        """

        :type words: List[str]

        :rtype: int

        """

        numList=[]

        for word in words:

            num=0

            for x in word:

                num|=1<<(ord(x)-ord('a'))

            numList.append(num)

        print numList

        maxvalue=0

        for i in xrange(len(words)):

            for j in xrange(i,len(words)):

                if numList[i]&numList[j]==0:

                    maxvalue=max(maxvalue,len(words[i])*len(words[j]))

        return maxvalue
