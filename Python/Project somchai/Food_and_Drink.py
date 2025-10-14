def Menu(filname):
    while True:
        h = f':{'Menu':^24}:'
        line = '-' * len(h)
        ch = f": {'1. Food':<23}:\n: {'2. Drink':<23}:\n: {'3. Snack':<23}:"
        print('', line, h, line, ch, line, sep='\n')
        
        choice = int(input('Please select 1 - 3 (0 to exit) : '))

        if choice == 0:
            break
        elif choice == 1:
            food_menu('Food.txt')
        elif choice == 2:
            drink_menu('Drink.txt')
        elif choice == 3:
            snack_menu('Snack.txt')
        else:
            print('Please select from the menu (1-3).')
            continue

        again = input('Do you want to return to the main menu? (y/n): ').strip().lower()
        if again != 'y':
            print('Thank you for visiting! Goodbye!')
            break

def food_menu(filename):
    while True:
        h = f':{'Menu (Food)':^32}:'
        line = '-' * len(h)
        print('', line, h, line, sep='\n')

        food = [
            {"name": "Shrimp Fried Rice", "price": 60},
            {"name": "Chicken Rice", "price": 50},
            {"name": "Garlic Pork Rice", "price": 55},
            {"name": "Basil Chicken Rice", "price": 55},
            {"name": "Green Curry Rice", "price": 65},
            {"name": "Duck Rice", "price": 70},
            {"name": "Red Pork Rice", "price": 60},
            {"name": "Crab Fried Rice", "price": 80},
            {"name": "Basil Seafood Rice", "price": 75},
            {"name": "Omelet Rice", "price": 50}
        ]

        for i in food:
            print(f': {i["name"]:<25}:{i["price"]:^5}:')
        print(line)

        choice = int(input('Please select 1 - 10 (0 to exit) : '))

        again = input('Do you want to return to the main menu? (y/n): ').strip().lower()
        if again != 'y':
            print('Thank you for visiting! Goodbye!')
            break

def drink_menu(filename):
    while True:
        h = f':{'Menu (Drink)':^32}:'
        line = '-' * len(h)
        print('', line, h, line, sep='\n')

        drink = [
            {"name": "Water", "price": 10},
            {"name": "Coke", "price": 20},
            {"name": "Iced Tea", "price": 25},
            {"name": "Orange Juice", "price": 30},
            {"name": "Iced Coffee", "price": 35}
        ]

        for i in drink:
            print(f': {i["name"]:<25}:{i["price"]:^5}:')
        print(line)

        choice = int(input('Please select 1 - 10 (0 to exit) : '))

        again = input('Do you want to return to the main menu? (y/n): ').strip().lower()
        if again != 'y':
            print('Thank you for visiting! Goodbye!')
            break

def snack_menu(filename):
    while True:
        h = f':{'Menu (Snack)':^32}:'
        line = '-' * len(h)
        print('', line, h, line, sep='\n')

        snack = [
            {"name": "Ice Cream", "price": 30},
            {"name": "Cake", "price": 40},
            {"name": "Cookie", "price": 20},
            {"name": "Donut", "price": 25},
            {"name": "Fruit Salad", "price": 35},
            {"name": "Pudding", "price": 30},
            {"name": "Bread Toast", "price": 25}
        ]

        for i in snack:
            print(f': {i["name"]:<25}:{i["price"]:^5}:')
        print(line)

        choice = int(input('Please select 1 - 10 (0 to exit) : '))

        again = input('Do you want to return to the main menu? (y/n): ').strip().lower()
        if again != 'y':
            print('Thank you for visiting! Goodbye!')
            break

def sales_record(filename):
    print('Sales Record')
    # Add your implementation here

def total_summary(filename):
    filename = "sales.txt"
    total_sales = 0  # เก็บยอดขายรวมทั้งหมด
    receipt_count = 0  # นับจำนวนใบเสร็จ
    
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()  # ตัดช่องว่างหัวท้ายออก

            # ถ้าพบบรรทัดที่มีคำว่า "Total Price:"
            if line.startswith("Total Price:"):
                # ดึงเฉพาะตัวเลขออกมา เช่น "190 Baht" -> 190
                parts = line.replace("Total Price:", "").replace("Baht", "").strip()
                total_sales += int(parts)  # แปลงเป็นจำนวนเต็มแล้วบวกเข้าไป
                receipt_count += 1

    # แสดงผลสรุป
    print("=== SALES SUMMARY ===")
    print(f"Total Receipts: {receipt_count} order(s)")
    print(f"Total Sales: {total_sales} Baht")
