import MyNattakon

while True:
    print("\nProgram Test Call Module")
    print("Main Menu")
    print("1. Find Max Number")
    print("2. Check Palindrome")
    print("3. Number to Text")
    print("4. Decimal to Binary")
    print("5. Exit")

    choice = input("Enter choice : ")

    if choice == '1':
        number = int(input("Enter number : "))
        result = MyNattakon.find_max_digit(number)
        print(f"Maximum digit {result} of number {number}")

    elif choice == '2':
        number = int(input("Enter number : "))
        if MyNattakon.is_palindrome(number):
            print(f"Number {number} is Palindrome.")
        else:
            print(f"Number {number} is not Palindrome.")

    elif choice == '3':
        number = int(input("Enter number : "))
        result = MyNattakon.number_to_text(number)
        print(f"Number : {number}")
        print(f"Text : {result}")

    elif choice == '4':
        number = int(input("Enter decimal number : "))
        result = MyNattakon.decimal_to_binary(number)
        print(f"Decimal number : {number}")
        print(f"Binary number : {result}")

    elif choice == '5':
        print("Exit Program.")
        break

    else:
        print("Invalid choice.")