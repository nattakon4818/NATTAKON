print("Program Find Maximum Dight")
while True:
    number = input("Enter integer number(0-exit) : ")

    if number == "0":
        print("exit program")
        break

    max_digit = max(number)
    print("Maximum Digit of integer number", number, " : ", max_digit)