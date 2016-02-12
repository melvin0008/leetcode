def wordbreak(dictionary,string,cache,result):
	if string in cache:
		return cache[string]
	if not string:
		print result
	for i in xrange(len(string)):
		if(string[0:i+1] in dictionary):
		 	suffix=wordbreak(dictionary,string[i+1:],cache,result+" "+string[0:i+1])
			cache[string]=string[0:i+1]+" "+suffix
	return ""

d=["mobile","samsung","sam","sung","man","mango","icecream","and","go","i","like","ice","cream"]
cache={}
print wordbreak(d,"ilikesamsung",cache,"")
print wordbreak(d,"samsungandmangok",cache,"")