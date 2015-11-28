class Solution(object):
    def rank(self,s):
        return {
            "*":3,
            "/":3,
            "+":2,
            "-":2,
            "(":1
        }.get(s,0)
        
    def findk(self,op,op1,op2):
        if op=="*":
            return op1*op2
        elif op=="/":
            return op1/op2
        elif op=="+":
            return op1+op2
        elif op=="-":
            return op1-op2
    
    def infix_to_postfix(self,s):
        #1+2*3-4 123*+4-
        st=[]
        result=[]
        x=0
        flag=0
        temp=""
        while x < len(s):
            while x < len(s) and s[x] in "0123456789":
                flag=1
                temp+=s[x]
                x+=1
            if flag==1:
                result.append(int(temp))
                flag=0
                temp=""
                continue
            if s[x] =="(":
                st.append(s[x])
            elif s[x] in ['*','/','+','-']:
                while st and self.rank(s[x])<=self.rank(st[-1]):
                    result.append(st.pop())
                st.append(s[x])
            elif s[x] ==")":
                top=st.pop()
                while st and top != "(":
                    result.append(top)
                    top=st.pop()
            x+=1
        while st:
            result.append(st.pop())
        return result
    
    def evaluate_postfix(self,s):
        st=[]
        for x in s:
            if type(x)==int:
                st.append(x)
            elif x in ['*','/','+','-']:
                if len(st)>1:
                    f=st.pop()
                    v=st.pop()
                    node=self.findk(x,v,f)
                    st.append(node)
        return st[0]
        
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.evaluate_postfix(self.infix_to_postfix(s))

                    
                    
                    
