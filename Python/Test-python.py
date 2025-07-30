# Assignment02-1

# print(">> Program Palindrome Number <<")

# number = int(input("Enter integer number : "))
# number = str(number)

# for n in range(len(number)):
#     f = number[n]
#     b = number[-(n+1)]
#     if f == b:
#         print(f"Digit {f} equal to Digit {b}")
#     else:
#         print(f"Digit {f} not equai to Digit {b}")
#         break
# if f == b:
#     print(f"Your enter number : {number} is Palindrome Number.")
# else:
#     print(f"Your enter number : {number} is not Palindrome Number.")
# print("Exit Program")

##########################################################

# Assignment02-2

# print(">> Program Change Number to Text <<")
# number = input("Enter integer number : ")
# print("Text : ", end="")

# for i in number:
#     if i == '0':
#         print("zero ", end="")
#     elif i == '1':
#         print("one ", end="")
#     elif i == '2':
#         print("two ", end="")
#     elif i == '3':
#         print("three ", end="")
#     elif i == '4':
#         print("four ", end="")
#     elif i == '5':
#         print("five ", end="")
#     elif i == '6':
#         print("six ", end="")
#     elif i == '7':
#         print("seven ", end="")
#     elif i == '8':
#         print("eight ", end="")
#     elif i == '9':
#         print("nine ", end="")

# print("\nExit Program")

##########################################################

# Assignment02-3

# while True:
#     money = float(input("Enter your income( -1 to exit) : "))

#     if money == -1:
#         print("Exit Program...")
#         break
#     elif money >= 1000000:
#         print(f"Net income : {money:,.2f}")
#         print("Tax Pate(%) : 10.0%")
#         print(f"Amount Tax : {money * 10 / 100:,.2f}")
#     elif money >= 800001:
#         print(f"Net income : {money:,.2f}")
#         print("Tax Pate(%) : 7.5%")
#         print(f"Amount Tax : {money * 7.5 / 100:,.2f}")
#     elif money >= 500001:
#         print(f"Net income : {money:,.2f}")
#         print("Tax Pate(%) : 5.5%")
#         print(f"Amount Tax : {money * 5.5 / 100:,.2f}")
#     elif money >= 300001:
#         print(f"Net income : {money:,.2f}")
#         print("Tax Pate(%) : 4.0%")
#         print(f"Amount Tax : {money * 4 / 100:,.2f}")
#     elif money >= 150001:
#         print(f"Net income : {money:,.2f}")
#         print("Tax Pate(%) : 2.5%")
#         print(f"Amount Tax : {money * 2.5 / 100:,.2f}")
#     else:
#         print(f"Net income : {money:,.2f}")
#         print("Tax Pate(%) : 0%")
#         print(f"Amount Tax : {money * 0 / 100:,.2f}")

##########################################################

# Assignment02-4

# while True:
#     print("=" * 27)
#     print("::       Main Menu       ::")
#     print("=" * 27)
#     print("A. Get Integer Number")
#     print("B. Summation of Digit")
#     print("C. Conut Digit")
#     print("D. Exut")
    
#     choice = input("Enter Choice : ")

#     if choice == 'A' or choice == 'a':
#         num = input("\nEnter long number : ")
#         print()
    
#     elif choice == 'B' or choice == 'b':

#         if num:
#             total = 0
#             for ch in num:
#                 total += int(ch)
#             print(f"\nSummation of digits = {total}")

#         even_sum = 0
#         odd_sum = 0

#         for ch in num:
#             digit = int(ch)
#             if digit % 2 == 0:
#                 even_sum += digit
#             else:
#                 odd_sum += digit

#         print("Summation odd of digits :", odd_sum)
#         print("Summation even of digits :", even_sum)
#         print()

#     elif choice == 'C' or choice == 'c':
#         print(f"\nYour enter number : {num}")
#         sum = len(num)
#         print(f"This number has {sum} digits.")
#         print()

#     elif choice == 'D' or choice == 'd':
#         print("\nExit program...")
#         print()
#         break
