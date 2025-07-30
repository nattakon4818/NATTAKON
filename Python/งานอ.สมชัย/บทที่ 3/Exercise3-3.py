amount = float(input("Enter amount : "))
rate = float(input("Enter rate : "))
year = int(input("Enter year : "))

Rate = rate / 100
fv = amount * (1 + Rate) ** year

print("Future value = ", fv)