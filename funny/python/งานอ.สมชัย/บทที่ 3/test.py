A = 10
B = 20
print("Before Swap A = ", A, ", B = ", B)
Z = A
A = B
B = Z
print("After Swap A = ", A, ", B = ", B)

print("*****")
print("****")
print("***")
print("**")
print("*")

print()

print("*")
print("**")
print("***")
print("****")
print("*****")

print()

print("*   *   ***   *   *   ****")
print("**  *    *    **  *   *")
print("* * *    *    * * *   ****")
print("*  **    *    *  **   *")
print("*   *   ***   *   *   ****")

print()

age = int(input("โปรดกรอกอายุของท่าน : "))
ftage = age + 10
print("อายุของท่านในอีก 10 ปีคือ", ftage)

name = input("โปรดกรอกชื่อของคุณ : ")
if name == 'Nattakon':
    print('Your name is Nattakon')
else:
    print('I do not know you')
    
print()
    
print("Player 1 - Choose your move : 1 - Rock, 2 - Papper, 3 - Scissors ")
player1 = int(input("Enter 1, 2, or 3 : "))

print()

print("Player 1 - Choose your move : 1 - Rock 2 - Papper 3 - Scissors ")
player2 = int(input("Enter 1, 2, or 3 : "))

if player1 == 1 and player2 == 1:
    print("Player 1 chose: rock")
    print("Player 2 chose: rock")
    print("drew")
elif player1 == 1 and player2 == 2:
    print("Player 1 chose: rock")
    print("Player 2 chose: papper")
    print("Player 2 win")
elif player1 == 1 and player2 == 3:
    print("Player 1 chose: rock")
    print("Player 2 chose: scissors")
    print("Player 1 win")
elif player1 == 2 and player2 == 1:
    print("Player 1 chose: papper")
    print("Player 2 chose: rock")
    print("Player 1 win")
elif player1 == 2 and player2 == 2:
    print("Player 1 chose: papper")
    print("Player 2 chose: papper")
    print("drew")
elif player1 == 2 and player2 == 3:
    print("Player 1 chose: papper")
    print("Player 2 chose: scissors")
    print("Player 2 win")
elif player1 == 3 and player2 == 1:
    print("Player 1 chose: scissors")
    print("Player 2 chose: rock")
    print("Player 1 win")
elif player1 == 3 and player2 == 2:
    print("Player 1 chose: scissors")
    print("Player 2 chose: papper")
    print("Player 1 win")
elif player1 == 3 and player2 == 3:
    print("Player 1 chose: scissors")
    print("Player 2 chose: scissors")
    print("drew")
else:
    print("Error")
