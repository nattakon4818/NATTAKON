h = "| Main  Menu |"
l = "=" * len(h)

while True:
    print(l, h, l, " 1. Triangle 1", " 2. Triangle 2", " 3. Triangle 3", " 4. Triangle 4", " 5. Exit", sep='\n')
    choice = int(input("Enter Choice : "))

    if choice == 1:
        noc = int(input("\nEnter number of character : "))
        print()

        for i in range(noc):
            print("*" * (i + 1))
        print()
    
    elif choice == 2:
        noc = int(input("\nEnter number of character : "))
        print()

        for i in range(noc, 0, -1):
            print("*" * i)
        print()

    elif choice == 3:
        noc = int(input("\nEnter number of character : "))
        print()

        for i in range(1, noc + 1):
            print(" " * (noc - i) + "*" * i)
        print()

    elif choice == 4:
        noc = int(input("\nEnter number of character : "))
        print()

        for i in range(noc, 0, -1):
            print(" " * (noc - i) + "*" * i)
        print()
    
    elif choice == 5:
        print("\nExit Program ...")
        break
    else:
        print("\nInput error choice.\n")