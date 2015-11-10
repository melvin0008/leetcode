def reverse(i):
	r=0
	a=i
	while(a>0):
		r=(r<<1)|(a&1)
		a=a>>1
	print r
	return True if r==i else False

print reverse(252)
print reverse(855)
