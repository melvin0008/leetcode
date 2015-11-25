from collections import deque
st="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def excel(y):
	di=y/26
	mo=y%26
	q=deque([])
	while(di):
		if not(di==1 and mo==0):
			if(mo==0):
				q.appendleft(st[di-2])
			else:
				q.appendleft(st[di-1])
		di/=26
	q.append(st[mo-1])
	return "".join(q)
print excel(51)
print excel(52)
print excel(53)
print excel(676)
