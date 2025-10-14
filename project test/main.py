from Menu import *

def main():
    print("=== WELCOME TO RESTAURANT SYSTEM ===")

    # 1) ลงทะเบียนสมาชิก
    member_name, table = register_member()

    # 2) เลือกอาหาร เครื่องดื่ม และของหวาน
    food = choose_items(food_menu, "FOOD MENU")
    drink = choose_items(drink_menu, "DRINK MENU")
    dessert = choose_items(dessert_menu, "DESSERT MENU")

    # รวมรายการทั้งหมด
    all_orders = food + drink + dessert

    # ถ้าไม่มีการสั่งอะไรเลย
    if len(all_orders) == 0:
        print("\n⚠️ No items selected. Exiting program.")
        return

    # 3) ส่วนลดสมาชิก
    discount = 0
    ans = input("Apply member discount? (y/n): ")
    if ans.lower() == "y":
        try:
            discount = int(input("Enter discount percentage: "))
        except ValueError:
            discount = 0
            print("Invalid input. No discount applied.")

    # 4) คำนวณยอดรวม
    total = calculate_total(all_orders, discount)

    # 5) แสดงผลลัพธ์
    print("\n=== ORDER SUMMARY ===")
    for item in all_orders:
        print(f"{item['name']} x {item['qty']} = {item['price'] * item['qty']} Baht")
    print(f"Discount: {discount}%")
    print(f"Total: {total} Baht")

    # 6) บันทึกใบเสร็จ
    save_receipt(member_name, table, all_orders, total)

    # 7) ถามว่าต้องการดูยอดขายหรือไม่
    check = input("\nView daily sales summary? (y/n): ")
    if check.lower() == "y":
        daily_sales_report()

    # 8) ค้นหาโต๊ะใดโต๊ะหนึ่ง
    search = input("\nSearch sales by table number (Enter to skip): ")
    if search.strip():
        find_table_sales(search)


# ===============================
# จุดเริ่มต้นของโปรแกรม
# ===============================
if __name__ == "__main__":
    main()