# ACP-Square it out 
def Square(s,e):
	lst = []
	
	for i in range(s,e):
		lst.append(i**2)

	even = []
	odd = []
	for i in lst:
		if i%2==0:
			even.append(i)
		else:
			odd.append(i)
	
	print("Even Square:", even)
	print("Odd Square:", odd)
	
Square(1,10)


