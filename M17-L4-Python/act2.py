#ACT2-Count the notes

amt =int(input("Please Enter Amount:"))

# find no. of notes
n1 = amt//100                      # returens quotient(floor)
n2 = (amt%100)//50                 #% for remainder
n3 = ((amt%100)%50)//10


print( "100 rupees notes: " , n1)
print( "50 rupees notes: " , n2)
print( "10 rupees notes: " , n3)
