#act2- Word matching
# checking first and last character of words is matching or not
def match(words):
	count = 0
	lst = []
    #x is a word in list
	for x in words:   
		if  x[0] == x[-1] and len(x)>1:
			count=count+ 1
			lst.append(x)
           
	
	print("Words matching are:", lst)
	return count
	
count = match(['121','aba',"xyzx","abcd","3421"])
print("count:", count)
