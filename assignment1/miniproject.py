

print("1. Bill Generator")

item = input("Enter item name: ")
price = float(input("Enter price of one item: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

print("\n----------- BILL -----------")
print("Item Name :", item)
print("Price     :", price)
print("Quantity  :", quantity)
print("----------------------------")
print("Total Bill:", total)
print("----------------------------")


##output
#----------- BILL -----------
#Item Name : pencil
#Price     : 50.0
#Quantity  : 6
#----------------------------
#Total Bill: 300.0
#----------------------------