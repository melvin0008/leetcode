def maxSumSubsequence(A,n):
	s=[0]*n
	for c, val in enumerate(A):
		if(s[c-1]+val)<0:
			s[c]=0
		else:
			s[c]=s[c-1]+val
	return max(s)

a=[-2,11,-4,13,-8,6]
print maxSumSubsequence(a,len(a))
