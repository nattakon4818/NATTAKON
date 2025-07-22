# Exercise 1

money = float(input("Enter number money withdraw : "))
print()  # มีหรือไม่มีก็ได้

b1000 = money // 1000
money %= 1000

b500 = money // 500
money %= 500

b100 = money // 100
money %= 100

print("Cash B1000 : ", b1000)
print("Cash B500  : ", b500)
print("Cash B100  : ", b100)

##############################################################################

# Exercise 2

num = int(input("Enter integer number :  "))

a = num // 1000
b = (num % 1000) // 100
c = (num % 100)  //10
d = num % 10

print(a)
print(b)
print(c)
print(d)

##############################################################################

# Exercise 3

amount = float(input("Enter amount : "))
rate = float(input("Enter rate : "))
year = int(input("Enter year : "))

Rate = rate / 100
fv = amount * (1 + Rate) ** year

print("Future value = ", fv)

##############################################################################

# Exercise 4

net_price = int(input("Enter net price product : "))

price = net_price / (1 + 7 / 100)
vat   = net_price - price

print(f"Price product : {price:.1f}")
print(f"Vat product : {vat:.1f}")