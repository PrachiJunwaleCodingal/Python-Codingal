#act3-play with list

Lst = [10,23,42,4,8,45]
print("List :", Lst)
  
sum = 0
  
# Find sum and Avg
for i in Lst:
    sum =sum + i
      
avg = sum /len(Lst)
  
print("sum = ", sum)
print("average = ", avg)

#sort list
Lst.sort()
print("Smallest No.:", Lst[0])
print("Largest No.:", Lst[-1])
