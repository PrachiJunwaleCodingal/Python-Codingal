# ACT2- Flip-flop means palindrome or not
def pal(tup):
	end = len(tup) -1
	start = 0
	while(start < end):
		if(tup[start] != tup[end]):
			return False
		start=start+1
		end=end-1
	return True


tup = (9,8,7,7,8,9)

if(pal(tup)):
	print("Palendrome")
else:
	print("Not Palendrome")