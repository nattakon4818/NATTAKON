while True:
    print(f"{"=" * 27}",f"{"::\tMain Menu\t::"}",f"{"=" * 27}",f"{"A. Get Integer Number"}",f"{"B. Summation of Digit"}",f"{"C. Conut Digit"}",f"{"D. Exut"}", sep='\n')
    
    choice = input("Enter Choice : ")

    if choice == 'A' or choice == 'a':
        num = input("\nEnter long number : ")
        print()
    
    elif choice == 'B' or choice == 'b':
        even = 0
        odd = 0
        total = 0

        for i in num:
            total += int(i)
            digit = int(i)
            if digit % 2 == 0:
                even += digit
            else:
                odd += digit

        print(f"\nYour enter number : {num}\nSummation of digits = {total}\nSummation odd of digits : {odd}\nSummation even of digits : {even}\n")

    elif choice == 'C' or choice == 'c':
        sum = len(num)
        print(f"\nYour enter number : {num}\nThis number has {sum} digits.\n")

    elif choice == 'D' or choice == 'd':
        print("\nExit program...\n")
        break