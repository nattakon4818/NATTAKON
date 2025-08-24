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

print(f"\n>>  Program Calculate Grade <<\n{'=' * 30}\n\nInput Data:")

credit = 3
s_points = 0
total_credit = credit * 6

for i in range(1, 7):
    subject = input(f"Enter subject name({i}) : ")
    score = float(input(f"Enter subject score({i}) : "))

    if 80 <= score <= 100:
        grade, gp = "A", 4.0
    elif 70 <= score <= 79:
        grade, gp = "B", 3.0
    elif 60 <= score <= 69:
        grade, gp = "C", 2.0
    elif 50 <= score <= 59:
        grade, gp = "D", 1.0
    else:
        grade, gp = "F", 0.0

    points = gp * credit
    s_points += points

print(f":{i:^7}: {subject:<27}:{score:^6}:{grade:^7}:{credit:^6}:{points:>5} :")

# # Footer
# print("=" * 67)
# print(f":{'Total':>37}              :{total_credit:>3}  :{s_points:>5} :")
# print("=" * 67)
# print(f": {'Grade Point Average(GPA) : ':<26}{s_points / total_credit:<37}:")
# print("=" * 67)
