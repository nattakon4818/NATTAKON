from Menu import * 

def main():
    while True:
        head = f'|{'Register Member':^30}|'
        print('', f'-' * len(head), head, f'-' * len(head), sep='\n')
        
        member_name, table = register_member()

        while True:
            h = f':{'WELCOME TO RESTAURANT':^30}:'
            line = '-' * len(h)
            ch = f": {'1. Menu':<29}:\n: {'2. Daily sales summary':<29}:\n: {'3. Exit program':<29}:"
            print('', line, h, line, ch, line, sep='\n')
            
            choice = int(input('Please select 1 - 2 (3 to exit) : '))

            if choice == 1:
                food = choose_items(food_menu, "FOOD MENU")
                drink = choose_items(drink_menu, "DRINK MENU")
                dessert = choose_items(dessert_menu, "DESSERT MENU")

                all_orders = food + drink + dessert
                
                discount = 0
                ans = input("\nApply member discount? (y/n) : ")
                if ans.lower() == "y":
                    try:
                        discount = int(input("Enter discount percentage: "))
                    except ValueError:
                        discount = 0
                        print("Invalid input. No discount applied.")
            
                total = calculate_total(all_orders, discount)

                print('\n=== ORDER SUMMARY ===')
                for item in all_orders:
                    print(f"{item['name']} x {item['qty']} = {item['price'] * item['qty']} .-")
                print(f"\nDiscount : {discount:<3}%{'':29}", f"Total : {total:>4,.2f} .-", sep='\n')

                save_receipt(member_name, table, all_orders, total)

            elif choice == 2:
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