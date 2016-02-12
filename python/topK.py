from random import randint

def randomselection(a,low,high,k):
	p=randint(low,high)
	j=partition(a,low,high,p)
	if(j==k):
		return
	elif k<j:
		randomselection(a,low,j-1,k)
	else:
		randomselection(a,j+1,high,k)
	

def partition(a,l,r,rand):
	a[l],a[rand]=a[rand],a[l]
	pivot, i = a[l],l
	for j in range(l+1, r+1):
		if a[j] >= pivot:
			i += 1
			if i<j:
				a[i],a[j] = a[j],a[i]
			
			# swap pivot to its correct place
	a[l], a[i] = a[i], a[l]
	return i

arr=[8,5,7,6,2,4,1,3,9]
print randomselection(arr,0,len(arr)-1,5)

print arr[:5]