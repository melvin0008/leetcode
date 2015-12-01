from collections import defaultdict

class Solution(object):

    def isAnagram(self, s, t):

        """

        :type s: str

        :type t: str

        :rtype: bool

        """

        if len(s)!= len(t):

            return False

        c=defaultdict(int)

        d=defaultdict(int)

        for x in s:

            c[x]+=1

        for x in t:

            d[x]+=1

        for x in d:

            if x in c:

                if d[x] != c[x]:

                    return False

            else:

                return False

        return True

            

            

        
