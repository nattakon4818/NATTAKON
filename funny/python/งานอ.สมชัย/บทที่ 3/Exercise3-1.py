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