#ACT3- percentage calculation


print("Enter Marks : ")
computer = int(input("Computer :"))
art = int(input("Art :"))
science = int(input("Science :"))

sum = computer+art+science
print("Sum:",sum)

per = (sum/300)*100

print("Percentage:", per, end=" %")
