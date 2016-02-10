class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, A):
        neg=1
        A=A.lstrip()
        if A[0]=="-":
            neg=-1
            A=A[1:]
        corrected=""
        for x in A:
            if x=="+":
                continue
            if not x.isdigit():
                break
            corrected+=x
        b=0
        ans=0
        for x in reversed(corrected):
            ans+=int(x)*(10**b)
            if ans>2147483647:
                if neg==1:
                    return 2147483647
                else:
                    return -2147483648
            b+=1
        return ans*neg