sales = []
menuStr = "Main Menu\n==========\n1. Input Sale\n2. Report Sale\n3. Exit\nEnter choice : "
while True:
    choice = input(menuStr)
    if choice == "1":
        while True:
            sale = float(input("Enter sale amount(0 - exit) : "))
            if sale == 0.0: break
            elif sale > 0.0: sales.append(sale)
    elif choice == "2":
        result = ("-" * 30) + "\n:Day: Sale Amount :Percant(%):\n" + ("-" * 30 ) + "\n"
        for n in range(len(sales)):
            result += f":{(n + 1):3}:{sales[n]:12.2f}:{'%'.center(10)}:\n"
        result += ("-" * 30) + "\nTotal Amount : %12.2f" % (sum(sales))
        print(result)
    elif choice == "3":
        break
    else: print("No choice, input again.")
print("Exit Program")