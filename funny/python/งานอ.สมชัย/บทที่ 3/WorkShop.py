# WorkShop 1

qty = int(input("จำนวนสินค้าที่ซื้อ : "))
price = float(input("ราคาต่อหน่วย : "))

total = price * qty
print("ราคาสินค้าที่ซื้อทั้งหมด : ", total)

pay = float(input("เงินที่รับ : "))
change = pay - total
print("เงินทอน : ", change)

##############################################################################

# WorkShop 2

qty = int(input("จำนวนสินค้าที่ซื้อ : "))
price = float(input("ราคาต่อหน่วย : "))

total = price * qty
print("ราคาสินค้าที่ซื้อทั้งหมด : ", total)

pay = float(input("เงินที่รับ : "))
change = pay - total
print("เงินทอน : ", change)

##############################################################################

# WorkShop 3

Score1 = int(input("Enter score 1 : "))
Score2 = int(input("Enter score 2 : "))
Score3 = int(input("Enter score 3 : "))
Score4 = int(input("Enter score 4 : "))

Total = Score1 + Score2 + Score3 + Score4
Average = Total / 4

print()
print("Total Score : ", Total)
print("Sverage Score : ", Average)

##############################################################################

# WorkShop 4

print("Program Calculate Area Circle.")
radius = float(input("Enter circle radius (float number) : "))
area = 3.14 * radius * radius
circum = 2 * 3.14 * radius
print("Area of circle with radius", radius, "is", area)
print("Circumference is", circum)