import datetime

# ===============================
# 1) เมนูอาหาร เครื่องดื่ม ขนม
# ===============================
food_menu = [
    {"name": "Shrimp Fried Rice", "price": 60},
    {"name": "Chicken Rice", "price": 50},
    {"name": "Garlic Pork Rice", "price": 55},
    {"name": "Basil Chicken Rice", "price": 55},
    {"name": "Green Curry Rice", "price": 65},
    {"name": "Duck Rice", "price": 70},
    {"name": "Red Pork Rice", "price": 60},
    {"name": "Crab Fried Rice", "price": 70},
    {"name": "Basil Seafood Rice", "price": 65},
    {"name": "Omelet Rice", "price": 45}
]

drink_menu = [
    {"name": "Water", "price": 10},
    {"name": "Coke", "price": 20},
    {"name": "Iced Tea", "price": 25},
    {"name": "Orange Juice", "price": 30},
    {"name": "Iced Coffee", "price": 35}
]

dessert_menu = [
    {"name": "Ice Cream", "price": 30},
    {"name": "Cake", "price": 40},
    {"name": "Cookie", "price": 20},
    {"name": "Donut", "price": 25},
    {"name": "Fruit Salad", "price": 35},
    {"name": "Pudding", "price": 30},
    {"name": "Bread Toast", "price": 25}
]


# ===============================
# 2) ฟังก์ชันแสดงเมนู
# ===============================
def show_menu(menu, title):
    print(f"\n=== {title} ===")
    for i, item in enumerate(menu, start=1):
        print(f"{i}. {item['name']} - {item['price']} Baht")


# ===============================
# 3) ฟังก์ชันเลือกอาหาร
# ===============================
def choose_items(menu, title):
    show_menu(menu, title)
    choices = input("Enter menu numbers (e.g. 1,3,5) or press Enter to skip: ")
    selected = []

    if choices.strip() == "":
        return selected

    for choice in choices.split(","):
        try:
            index = int(choice.strip()) - 1
            if 0 <= index < len(menu):
                qty = int(input(f"Quantity for {menu[index]['name']}: "))
                selected.append({
                    "name": menu[index]["name"],
                    "price": menu[index]["price"],
                    "qty": qty
                })
        except ValueError:
            print(f"Invalid input: {choice}")

    return selected


# ===============================
# 4) ฟังก์ชันบันทึกสมาชิก
# ===============================
def register_member():
    name = input("Enter member name: ")
    table = input("Enter table number: ")

    with open("member.txt", "a", encoding="utf-8") as f:
        f.write(f"{name},{table}\n")

    print(f"✅ Member '{name}' registered at Table {table}")
    return name, table


# ===============================
# 5) คำนวณราคาทั้งหมด + ส่วนลด
# ===============================
def calculate_total(orders, discount=0):
    total = sum(item["price"] * item["qty"] for item in orders)
    if discount > 0:
        total = total - (total * discount / 100)
    return total


# ===============================
# 6) บันทึกใบเสร็จ
# ===============================
def save_receipt(member_name, table, all_orders, total):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("sales.txt", "a", encoding="utf-8") as f:
        f.write(f"=== TABLE {table} | MEMBER: {member_name} | DATE: {now} ===\n")
        for item in all_orders:
            f.write(f"- {item['name']} x {item['qty']} = {item['price'] * item['qty']} Baht\n")
        f.write(f"Total Price: {total} Baht\n")
        f.write("-----------------------------\n")

    print("\n💾 Receipt saved to sales.txt")


# ===============================
# 7) ค้นหาข้อมูลใบเสร็จตามโต๊ะ
# ===============================
def find_table_sales(table_number):
    print(f"\n=== SALES FOR TABLE {table_number} ===")
    found = False

    with open("sales.txt", "r", encoding="utf-8") as f:
        for line in f:
            if f"TABLE {table_number}" in line:
                found = True
            if found:
                print(line.strip())
                if "-----------------------------" in line:
                    found = False


# ===============================
# 8) สรุปยอดขายรายวัน
# ===============================
def daily_sales_report(data):
    total_sales = 0
    today = datetime.datetime.now().strftime("%Y-%m-%d")

    try:
        with open("sales.txt", "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("Total Price:"):
                    price = int(line.replace("Total Price:", "").replace("Baht", "").strip())
                    total_sales += price

        print("\n=== DAILY SALES REPORT ===")
        print(f"Date: {today}")
        print(f"Total Sales: {total_sales} Baht")
    except FileNotFoundError:
        print("No sales data found.")
