while True:
    print("=" * 27)
    print("::       Main Menu       ::")
    print("=" * 27)
    print("A. Get Integer Number")
    print("B. Summation of Digit")
    print("C. Conut Digit")
    print("D. Exut")
    
    choice = input("Enter Choice : ")

    if choice == 'A' or choice == 'a':
        num = input("\nEnter long number : ")
        print()
    
    elif choice == 'B' or choice == 'b':

        even = 0
        odd = 0
        total = 0
        
        if num:
            for i in num:
                total += int(i)
            print(f"\nSummation of digits = {total}")


        for i in num:
            digit = int(i)
            if digit % 2 == 0:
                even += digit
            else:
                odd += digit

        print(f"Summation odd of digits : {odd}\nSummation even of digits : {even}")
        print()

    elif choice == 'C' or choice == 'c':

        sum = len(num)

        print(f"\nYour enter number : {num}")
        print(f"This number has {sum} digits.")
        print()

    elif choice == 'D' or choice == 'd':
        print("\nExit program...")
        print()
        break