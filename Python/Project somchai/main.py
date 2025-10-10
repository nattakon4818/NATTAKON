from Food_and_Drink import *
from members import *

DATAFILE = 'Members.txt'

def main():

    while True:
        h = f':{'Welcome to Restaurant':^24}:'
        line = '-' * len(h)
        menu = f": {'1. Menu':<23}:\n: {'2. Member':<23}:\n: {'3. Sales record':<23}:\n: {'4. Total summary':<23}:"
        print(line, h, line, menu, line, sep='\n')

        choice = int(input('Please select 1 - 4 (0 to exit): '))
        if choice == 0:
            print('Exit program.')
            break
        elif choice == 1:
            Menu('Menu.txt')
        elif choice == 2:
            members(DATAFILE)
        elif choice == 3:
            sales_record('Sales.txt')
        elif choice == 4:
            total_summary('Sales.txt')
        else:
            print('Please select from the menu 1 to 4 (0 to exit).')
            continue

        again = input('Do you want to return to the main menu? (y/n): ').strip().lower()
        if again != 'y':
            print('Thank you for visiting! Goodbye!')
            break


if __name__ == '__main__':
    main()