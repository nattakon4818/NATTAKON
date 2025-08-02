# A = 10
# B = 20
# print("Before Swap A = ", A, ", B = ", B)
# Z = A
# A = B
# B = Z
# print("After Swap A = ", A, ", B = ", B)

# print("*****")
# print("****")
# print("***")
# print("**")
# print("*")

# print()

# print("*")
# print("**")
# print("***")
# print("****")
# print("*****")

# print()

# print("*   *   ***   *   *   ****")
# print("**  *    *    **  *   *")
# print("* * *    *    * * *   ****")
# print("*  **    *    *  **   *")
# print("*   *   ***   *   *   ****")

# print()

# age = int(input("โปรดกรอกอายุของท่าน : "))
# ftage = age + 10
# print("อายุของท่านในอีก 10 ปีคือ", ftage)

# name = input("โปรดกรอกชื่อของคุณ : ")
# if name == 'Nattakon':
#     print('Your name is Nattakon')
# else:
#     print('I do not know you')
    
# print()
    
# print("Player 1 - Choose your move : 1 - Rock, 2 - Papper, 3 - Scissors ")
# player1 = int(input("Enter 1, 2, or 3 : "))

# print()

# print("Player 1 - Choose your move : 1 - Rock 2 - Papper 3 - Scissors ")
# player2 = int(input("Enter 1, 2, or 3 : "))

# if player1 == 1 and player2 == 1:
#     print("Player 1 chose: rock")
#     print("Player 2 chose: rock")
#     print("drew")
# elif player1 == 1 and player2 == 2:
#     print("Player 1 chose: rock")
#     print("Player 2 chose: papper")
#     print("Player 2 win")
# elif player1 == 1 and player2 == 3:
#     print("Player 1 chose: rock")
#     print("Player 2 chose: scissors")
#     print("Player 1 win")
# elif player1 == 2 and player2 == 1:
#     print("Player 1 chose: papper")
#     print("Player 2 chose: rock")
#     print("Player 1 win")
# elif player1 == 2 and player2 == 2:
#     print("Player 1 chose: papper")
#     print("Player 2 chose: papper")
#     print("drew")
# elif player1 == 2 and player2 == 3:
#     print("Player 1 chose: papper")
#     print("Player 2 chose: scissors")
#     print("Player 2 win")
# elif player1 == 3 and player2 == 1:
#     print("Player 1 chose: scissors")
#     print("Player 2 chose: rock")
#     print("Player 1 win")
# elif player1 == 3 and player2 == 2:
#     print("Player 1 chose: scissors")
#     print("Player 2 chose: papper")
#     print("Player 1 win")
# elif player1 == 3 and player2 == 3:
#     print("Player 1 chose: scissors")
#     print("Player 2 chose: scissors")
#     print("drew")
# else:
#     print("Error")

# ########################################################################

# for i in range(4):
#     print(" " * (4 - i) + "*" * (2 * i + 1))

# for i in range(5, 0, -1):
#     print(" " * (5 - i) + "*" * (2 * i - 1))

# ########################################################################

# text = str(input("Enter your name : "))
# text = 'ruksomchai'

# for i in range(len(text)):
#     space = ' ' * (len(text))
#     a = " ",
#     print(space + a)

# num = '123456'
# l = len(num)
# for i in range(l):
#     print(' ' * i, end='')

#     for i in range( l-1, -1, -1):
#         print(num[i], end='')
        
#     for i in range( 1, l):
#         print(num[i], end='')
        
#     print()
#     l -= 1
    
# ########################################################################

# num = int(input("Enter number : "))
# for i in range(12):
#     print(f" {num} x {i + 1} = {num * (i + 1)}")
    
# ########################################################################

# while True:
#     num = int(input("Enter number : "))
#     if num <= 0:
#         print("It's underflow. please try again.")
#     elif num >= 1000:
#         print("It's overfloe. please try again.")
#     else:
#         for i in range(12):
#             print(f"{num} x {i + 1} = {num * (i + 1)}")
#         break

# ########################################################################

# while True:
#     print(f"{"=" * 49}",f"{"|\t\tCurrency Convert\t\t|"}",f"{"=" * 49}",f"|{" 0. Exit":<47}|",f"|{" 1. Enter money":<47}|",f"|{" 2. Convert THB to USD(33 THB / 1 USD)":<47}|",f"|{" 3. Convert THB to USD(0.2 THB / 1 JPY)":<47}|",f"|{" 4. Convert THB to USD(37 THB / 1 EUR)":<47}|",f"{"=" * 49}", sep='\n')
#     c = int(input("\nEnter choice : "))
    
#     if c == 0:
#         print("exit.")
#         break
#     elif c == 1:
#         m = int(input("Enter money : "))
#         print(f"your money : {m:,.2f} (THB)" )
#     elif c == 2:
#         s = m / 33
#         print(f"{m:,.2f} (THB) => {s:,.2f} (USD)")
#     elif c == 3:
#         s = m / 0.2
#         print(f"{m:,.2f} (THB) => {s:,.2f} (JPY)")
#     elif c == 4:
#         s = m / 37
#         print(f"{m:,.2f} (THB) => {s:,.2f} (EUR)")
#     else:
#         print("No choice please try again.")
        
# #######################################################################

print(f"{"=" * 49}",f"{"|\t\tCurrency Convert\t\t|"}",f"{"=" * 49}",f"|{" 0. Exit":<47}|",f"|{" 1. Enter money":<47}|",f"|{" 2. Convert THB to USD(33 THB / 1 USD)":<47}|",f"|{" 3. Convert THB to USD(0.2 THB / 1 JPY)":<47}|",f"|{" 4. Convert THB to USD(37 THB / 1 EUR)":<47}|",f"{"=" * 49}", sep='\n')
# print(f"{"=" * 49}{"\n|Currency Convert|\n"}{"=" * 49}", sep='')

# print(len("|Currency Convert|"))
