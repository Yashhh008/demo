print("MENU\n1.SUM\n2.Differencce\n3.Product\n4.Division")


print("Enter two NUMBERS")


a=float(input("Enter first number"))
b=float(input("Enter second number"))

add=a+b
difference=a-b
product=a*b
if b!=0:
    division=a/b
else:
    print("Not defined")

print("SUM",add)
print(difference)
print(product)
print(division)

