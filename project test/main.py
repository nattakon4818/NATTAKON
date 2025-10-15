from Menu import * 

def main():
    while True:
        head = f'|{'Register Member':^30}|'
        print(f'-' * len(head), head, f'-' * len(head), sep='\n')
        
        member_name, table = register_member()  # 1) ลงทะเบียนสมาชิก

        h = f':{'WELCOME TO RESTAURANT':^30}:'
        line = '-' * len(h)
        ch = f": {'1. Menu':<29}:\n: {'2. Daily sales summary':<29}:\n: {'3. Exit program':<29}:"
        print('', line, h, line, ch, line, sep='\n')
        
        choice = int(input('Please select 1 - 2 (3 to exit) : '))

        if choice == 1:
            food = choose_items(food_menu, "FOOD MENU") # เลือกอาหาร
            drink = choose_items(drink_menu, "DRINK MENU") # เลือกเครื่องดื่ม
            dessert = choose_items(dessert_menu, "DESSERT MENU") # เลือกของหวาน

            # รวมรายการทั้งหมด
            all_orders = food + drink + dessert

            # ถ้าไม่มีการสั่งอะไรเลย
            # if len(all_orders) == 0:
            #     print("\n⚠️ No items selected. Exiting program.")
            #     return
            
            # ส่วนลดสมาชิก
            discount = 0
            ans = input("\nApply member discount? (y/n) : ")
            if ans.lower() == "y":
                try:
                    discount = int(input("Enter discount percentage: "))
                except ValueError:
                    discount = 0
                    print("Invalid input. No discount applied.")
        
            # คำนวณยอดรวม
            total = calculate_total(all_orders, discount)

            # แสดงผลลัพธ์
            h1 = f'|{'ORDER SUMMARY':^45}|'
            l1 = '-' * len(h1)
            print('', l1, h1, l1, sep='\n')
            for item in all_orders:
                print(f"| {item['name']:<22} x {item['qty']:^2} = {item['price'] * item['qty']:^3}.-      |")
            print(l1, f"| Discount : {discount:<3}%{'':29}|", f"| Total : {total:>4,.2f} .-{'':28}|", l1, sep='\n')

            # บันทึกใบเสร็จ
            save_receipt(member_name, table, all_orders, total)

            # ค้นหาโต๊ะใดโต๊ะหนึ่ง
            # search = input("\nSearch sales by table number (Enter to skip): ")
            # if search.strip():
            #     find_table_sales(search)

        elif choice == 2:
            # 7) ถามว่าต้องการดูยอดขายหรือไม่
            check = input("\nView daily sales summary? (y/n): ")
            if check.lower() == "y":
                daily_sales_report()

        elif choice == 3:
            print('Exit program.')
            break
                
        again = input('\nDo you want to return to the main menu? (y/n): ').strip().lower()
        if again != 'y':
            print('Thank you for visiting! Goodbye!')
            break

if __name__ == "__main__":
    main()