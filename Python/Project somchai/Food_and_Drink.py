def Menu(filname):
    while True:
        h = f':{'Menu':^24}:'
        line = '-' * len(h)
        menu = f": {'1. Food':<23}:\n: {'2. Drink':<23}:\n: {'3. Snack':<23}:"
        print(line, h, line, menu, line, sep='\n')
        
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
        h = f':{'Menu (Food)':^24}:'
        line = '-' * len(h)
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

        print(line, h, line, sep='\n')

        choice = int(input('Please select 1 - 10 (0 to exit) : '))

        if choice == 0:
            break
        # elif choice == 1:
        # elif choice == 2:
        # elif choice == 3:
        # elif choice == 4:
        # elif choice == 5:
        # elif choice == 6:
        # elif choice == 7:
        # elif choice == 8:
        # elif choice == 9:
        # elif choice == 10:
        # else:
        #     print('Please select from the menu (1-3).')
        #     continue

        again = input('Do you want to return to the main menu? (y/n): ').strip().lower()
        if again != 'y':
            print('Thank you for visiting! Goodbye!')
            break

def drink_menu(filename):
    while True:
        h = f':{'Menu (Drink)':^24}:'
        line = '-' * len(h)
        menu = f": {'1. Food':<23}:\n: {'2. Drink':<23}:\n: {'3. Snack':<23}:"
        print(line, h, line, menu, line, sep='\n')

        choice = int(input('Please select 1 - 5 (0 to exit) : '))

        if choice == 0:
            break
        # elif choice == 1:
        # elif choice == 2:
        # elif choice == 3:
        # elif choice == 4:
        # elif choice == 5:
        # else:
        #     print('Please select from the menu (1-3).')
        #     continue

        again = input('Do you want to return to the main menu? (y/n): ').strip().lower()
        if again != 'y':
            print('Thank you for visiting! Goodbye!')
            break

def snack_menu(filename):
    while True:
        h = f':{'Menu (Snack)':^24}:'
        line = '-' * len(h)
        menu = f": {'1. Food':<23}:\n: {'2. Drink':<23}:\n: {'3. Snack':<23}:"
        print(line, h, line, menu, line, sep='\n')

        choice = int(input('Please select 1 - 7 (0 to exit) : '))

        if choice == 0:
            break
        # elif choice == 1:
        # elif choice == 2:
        # elif choice == 3:
        # elif choice == 4:
        # elif choice == 5:
        # elif choice == 6:
        # elif choice == 7:
        # else:
        #     print('Please select from the menu (1-3).')
        #     continue

        again = input('Do you want to return to the main menu? (y/n): ').strip().lower()
        if again != 'y':
            print('Thank you for visiting! Goodbye!')
            break

def sales_record(filename):
    print('Sales Record')
    # Add your implementation here

def total_summary(filename):
    print('Total Summary')
    # Add your implementation here