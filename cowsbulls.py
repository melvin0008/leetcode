from collections import defaultdict

class Solution(object):

    def getHint(self, secret, guess):

        """

        :type secret: str

        :type guess: str

        :rtype: str

        """

        i,j,c,b=0,0,0,0

        lens=len(secret)

        d=defaultdict(int)

        for j,y in enumerate(guess):

            d[y]=d[y]+1

        while(i<lens):

            if(d[secret[i]]):

                d[secret[i]]-=1

                c+=1

            if(secret[i]==guess[i]):

                b+=1

            i+=1



        return "".join([str(b),"A",str(c-b),"B"])

                
