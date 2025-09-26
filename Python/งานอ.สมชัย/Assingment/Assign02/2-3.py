print(">> Program Change Number to Text <<")

while True:
    money = float(input("Enter your income( -1 to exit) : "))

    if money == -1:
        print("Exit Program...")
        break
    elif money >= 1000000:
        print(f"Net income : {money:,.2f}")
        print("Tax Pate(%) : 10.0%")
        print(f"Amount Tax : {money * 10 / 100:,.2f}")
    elif money >= 800001:
        print(f"Net income : {money:,.2f}")
        print("Tax Pate(%) : 7.5%")
        print(f"Amount Tax : {money * 7.5 / 100:,.2f}")
    elif money >= 500001:
        print(f"Net income : {money:,.2f}")
        print("Tax Pate(%) : 5.5%")
        print(f"Amount Tax : {money * 5.5 / 100:,.2f}")
    elif money >= 300001:
        print(f"Net income : {money:,.2f}")
        print("Tax Pate(%) : 4.0%")
        print(f"Amount Tax : {money * 4 / 100:,.2f}")
    elif money >= 150001:
        print(f"Net income : {money:,.2f}")
        print("Tax Pate(%) : 2.5%")
        print(f"Amount Tax : {money * 2.5 / 100:,.2f}")
    else:
        print(f"Net income : {money:,.2f}")
        print("Tax Pate(%) : 0%")
        print(f"Amount Tax : {money * 0 / 100:,.2f}")