qty = int(input("จำนวนสินค้าที่ซื้อ : "))
price = float(input("ราคาต่อหน่วย : "))

total = price * qty
print("ราคาสินค้าที่ซื้อทั้งหมด : ", total)

pay = float(input("เงินที่รับ : "))
change = pay - total
print("เงินทอน : ", change)