class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def convert(self, A, B):
        if B==1:
            return A
        arr=[]
        for __ in xrange(B):
            arr.append([])
        flag=0
        rev=0
        i=0
        A=A.strip()
        for x in A:
            arr[i].append(x)
            if rev==0:
                i+=1
                if i==B:
                    rev=1
                    i-=2
            else:
                if i==0:
                    rev=0
                    i+=1
                else:
                    i-=1
        ret=""
        for x in arr:
            for y in x:
                ret+=y
        return ret