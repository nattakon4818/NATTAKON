# name = "somchai"

# for i in range(0, len(name) + 1):
#     print(name[i:])

# for i in range(1, len(name)+1):
#     print(" " * (len(name)-i) + name[:i])

# for i in range(len(name), 0, -1):
#     print(name[:i])

# for i in range(len(name), 0, -1):
#     print(" " * (len(name)-i) + name[:i])


# ########################################################################


# name = "somchai"
# revers_name = name[::-1]

# for i in range(1, len(revers_name)+1):
#     print(" " * (len(revers_name)-i) + revers_name[:i])

# for i in range(len(revers_name), 0, -1):
#     print(revers_name[:i])

# for i in range(len(revers_name), 0, -1):
#     print(" " * (len(revers_name)-i) + revers_name[:i])


# ########################################################################

# name = input("Enter a string: ")
# reversed_name = name[::-1]

# for i in range(len(name)):
#     left = name[:len(name) - i]
#     right = reversed_name[i:]
#     spaces = " " * (2 * i)
#     print(left + spaces + right)

# name = input("Enter a string: ")
# reversed_name = name[::-1]
# n = len(name)

# # 🔻 ส่วนแรก: ลดลง
# for i in range(n):
#     left = name[:n - i]
#     right = reversed_name[i:]
#     space = " " * (2 * i)
#     print(left + space + right)

# # 🔼 ส่วนที่สอง: เพิ่มขึ้น
# for i in range(n - 2, -1, -1):  # ไล่กลับขึ้น โดยไม่ซ้ำบรรทัดกลาง
#     left = name[:n - i]
#     right = reversed_name[i:]
#     space = " " * (2 * i)
#     print(left + space + right)

# name = input("Enter a string: ")
# n = len(name)

# for i in range((n + 1) // 2):
#     spaces = " " * i
#     middle = name[i : n - i]
#     print(spaces + middle)


# name = input("Enter a string: ")
# n = len(name)
# half = (n + 1) // 2

# for i in range(half - 1, -1, -1):
#     print(" " * i + name[i:n - i])

# print(f"\n>>  Program Calculate Grade <<\n{'=' * 30}\n\nInput Data:")

# credit = 3
# s_points = 0
# total_credit = credit * 6

# for i in range(1, 7):
#     subject = input(f"Enter subject name({i}) : ")
#     score = float(input(f"Enter subject score({i}) : "))

#     if 80 <= score <= 100:
#         grade, gp = "A", 4.0
#     elif 70 <= score <= 79:
#         grade, gp = "B", 3.0
#     elif 60 <= score <= 69:
#         grade, gp = "C", 2.0
#     elif 50 <= score <= 59:
#         grade, gp = "D", 1.0
#     else:
#         grade, gp = "F", 0.0

#     points = gp * credit
#     s_points += points

# print(f":{i:^7}: {subject:<27}:{score:^6}:{grade:^7}:{credit:^6}:{points:>5} :")

# # Footer
# print("=" * 67)
# print(f":{'Total':>37}              :{total_credit:>3}  :{s_points:>5} :")
# print("=" * 67)
# print(f": {'Grade Point Average(GPA) : ':<26}{s_points / total_credit:<37}:")
# print("=" * 67)

########################################################################################

h = "| Main  Menu |"
l = "=" * len(h)

while True:
    print(l, h, l, " 1. Triangle 1", " 2. Triangle 2", " 3. Triangle 3", " 4. Triangle 4", " 5. Exit", sep='\n')
    choice = int(input("Enter Choice : "))

    if choice == 1:
        noc = int(input("\nEnter number of character : "))
        print()

        for i in range(noc):
            print("*" * (i + 1))
        print()
    
    elif choice == 2:
        noc = int(input("\nEnter number of character : "))
        print()

        for i in range(noc, 0, -1):
            print("*" * i)
        print()

    elif choice == 3:
        noc = int(input("\nEnter number of character : "))
        print()

        for i in range(1, noc + 1):
            print(" " * (noc - i) + "*" * i)
        print()

    elif choice == 4:
        noc = int(input("\nEnter number of character : "))
        print()

        for i in range(noc, 0, -1):
            print(" " * (noc - i) + "*" * i)
        print()
    
    elif choice == 5:
        print("\nExit Program ...")
        break
    else:
        print("\nInput error choice.\n")

########################################################################################

while True:
    text = input("Enter text(enter-exit) : ")
    if text == "":
        break
    
    if text.isalpha():
        print("Text is alphabetic")
        
    elif text.isdigit():
        print("Text is digit")
        
    elif text.isalnum():
        print("Text is alpha and numeric")
        
    else:
        print("Text is string")

########################################################################################

aeiou = 'aeiou'

while True:
    text = input("Enter text(enter-exit) : ")

    if text == "":
        break

    a, e, i, o, u = 0, 0, 0, 0, 0

    for n in text.lower():
        if n == 'a':
            a += 1
        elif n == 'e':
            e += 1
        elif n == 'i':
            i += 1
        elif n == 'o':
            o += 1
        elif n == 'u':
            u += 1

    print(f"Text has 'a' : {a}", f"Text has 'e' : {e}", f"Text has 'i' : {i}", f"Text has 'o' : {o}", f"Text has 'u' : {u}", sep='\n')

########################################################################################

import random

head, h = "Main  Menu", "|Grade| Total|"
line, l = "=" * len(head), "-" * len(h)
total, count_A, count_B, count_C, count_D, count_F  = 0, 0, 0, 0, 0, 0

while True:
    print(head, line, " 1. Input Number of Score", " 2. Random Score and Check Grade", " 3. Exit", sep='\n')

    choice = input("Enter Choice : ")

    if choice == '1':
        total = int(input("Enter number of score : "))

    elif choice == '2':
        count_A, count_B, count_C, count_D, count_F  = 0, 0, 0, 0, 0

        print("\nStart Random Score ...\nCheck Grade ...\n")

        for i in range(total):
            score = random.randint(40, 90)

            if score >= 80: count_A += 1
            elif score >= 70: count_B += 1
            elif score >= 60: count_C += 1
            elif score >= 50: count_D += 1
            else: count_F += 1

        print(l, h, l, f"|  A  | {count_A:>4} |", f"|  B  | {count_B:>4} |", f"|  C  | {count_C:>4} |", f"|  D  | {count_D:>4} |", f"|  F  | {count_F:>4} |", l, f"|Total| {total:>4} |", l, "\n", sep='\n')

    elif choice == '3':
        print("Exit Program")
        break


########################################################################################

name = input('Enter your name : ')
num = 5
print()
print(name * num)
print("Show Triangle")
print(num * "*")
print((num - 1) * "*")
print((num - 2) * "*")
print((num - 3) * "*")
print((num - 4) * "*")


name = input('Enter your name : ')
num = len(name)
print()
print(name * num)
print("Show Triangle name")
print(name[:num])
print(name[:num -1])
print(name[:num -2])
print(name[:num -3])
print(name[:num -4])
print(name[:num -5])
print(name[:num -6])
