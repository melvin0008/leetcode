class Solution(object):
    def calcPrefix(self,n,prefix):
        i=1
        j=0
        while(i<len(n)):
            if(n[i]==n[j]):
                prefix[i]=j+1
                i+=1
                j+=1
            else:
                ##tricky1
                if j!=0:
                    j=prefix[j-1]
                    continue
                i+=1

    def strStr(self, h, n):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not h and not n:
            return 0
        prefix=[0]*len(n)
        self.calcPrefix(n,prefix)
        print prefix
        i=0
        j=0
        while i<len(h):
            savei=i-j
            while i<len(h) and j<len(n) and h[i]==n[j]:
                j+=1
                i+=1
            if(j==len(n)):
                return savei
            if i==len(h):
                return -1
            ##tricky2
            if j!=0 and h[i]!=n[j]:
                j=prefix[j-1]
            else:
                i+=1
        return -1
