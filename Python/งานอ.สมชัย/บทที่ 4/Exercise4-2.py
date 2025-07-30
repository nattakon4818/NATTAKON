print("Program Find Maximum Vulue")
num = int(input("Enter number of value(>=) : "))

if num < 1:
    print("Value input not correct.""\nExit program")
else:
    numbers = []

    print(f"\nProgram get value {num} numbers.")

    for i in range(1, num + 1):
        number = int(input(f"Enter value Number #{i} : "))
        numbers.append(number)

    print("Your enter number : ", ", ".join(str(n) for n in numbers))
        
    max_value = max(numbers)

    print("Maximum value number is", max_value)
    print("Exit Program")