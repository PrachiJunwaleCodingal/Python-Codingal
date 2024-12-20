#ACP- Tuple average

def avgfun(num):
    list1 = list(num)
    sum = 0 
    for x in list1:
        sum=sum+x
    return sum/4

n = (18,2,5,6)
print ("Tuple: ",n)

print("Average are:",avgfun(n))



