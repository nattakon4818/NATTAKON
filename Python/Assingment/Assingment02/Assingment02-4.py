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

        if num:
            total = 0
            for ch in num:
                total += int(ch)
            print(f"\nSummation of digits = {total}")

        even_sum = 0
        odd_sum = 0

        for ch in num:
            digit = int(ch)
            if digit % 2 == 0:
                even_sum += digit
            else:
                odd_sum += digit

        print("Summation odd of digits :", odd_sum)
        print("Summation even of digits :", even_sum)
        print()

    elif choice == 'C' or choice == 'c':
        print(f"\nYour enter number : {num}")
        sum = len(num)
        print(f"This number has {sum} digits.")
        print()

    elif choice == 'D' or choice == 'd':
        print("\nExit program...")
        print()
        break