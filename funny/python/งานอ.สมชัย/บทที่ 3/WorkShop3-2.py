num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))
print("Before swap num1 = ", num1, ", num2 = ", num2)
num2 = num1 + num2
num1 = num2 - num1
num2 = num2 - num1
print("After swap num1 = ", num1, ", num2 = ", num2)