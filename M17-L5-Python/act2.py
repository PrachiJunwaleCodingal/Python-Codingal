#Profit-Loss
CP =int(input("Enter the Cost Price of item: "))
SP =int(input("Enter the Selling Price of item: "))

if(SP > CP):
  profit=SP-CP
  print("Profit:",profit)
else:
  NoProfit=CP-SP
  print("You got no profit on this item. You got loss by ",NoProfit)