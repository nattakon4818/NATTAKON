def enter_data():
    global total, num
    total = num = value = 0
    while value != -1:
        value = int(input(f"Enter value {num + 1} : "))
        if (value != -1):
            total += value
            num += 1

total = 0
num = 0
enter_data()
print("Number of value : ", num)
print("Total number : ", total)
print("Average value : ", total / num)