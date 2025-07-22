print("SIMPLE CALCULATOR")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter Secong number: "))

print("Select option :")
print("1.Addition")
print("2.subtraction")
print("3.Multiplication")
print("4.Division")

choice = input("enter (1/2/3/4): ")

if(choice == "1"):
    print("sum =", num1 + num2)
elif(choice == "2"):
    print("sub =", num1 - num2)
elif(choice == "3"):
    print("multiplication =", num1 * num2)
elif(choice == "4"):
    print("dividion =", num1 / num2)
else:
    print("invalid Inputs")

