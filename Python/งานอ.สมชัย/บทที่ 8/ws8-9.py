A = set()
menu = '\n1. Add Item\n2. Remove Item\n3. Display Set\n4. Exit\nEnter choice : '
while True:
    choice = int(input(menu))
    if choice == 1:
        print('Add Item')
        data = int(input('Enter number : '))
        A.add(data)
    elif choice == 2:
        print('Remove Item')
        data = int(input('Enter number to remove : '))
        A.remove(data)
    elif choice == 3:
        print(A)
    elif choice == 4:
        print('Exit Program')
        break
    else: print('No choice')