#ACP- Tuple product

def productfun(num):
    list1 = list(num)
    mult = 1 
    for a in list1:
        mult=mult * a
    return mult

n = (18,2,-5,6)
print ("Tuple: ",n)

print("Product are:",productfun(n))



