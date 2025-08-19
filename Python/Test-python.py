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
