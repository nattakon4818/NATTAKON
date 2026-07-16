a, score, grade = 0, 0, 0
h = "Grade Summary"
l1, l2 = "=" * 10, "=" * 35
print(l1, h, l1)

a = int(input("please enter your score : "))

if 80 <= a <= 100: grade, score = "A", 4.00
elif 70 <= a <= 79: grade, score = "B+", 3.00
elif 70 <= a <= 79: grade, score = "B+", 3.00
elif 70 <= a <= 79: grade, score = "B+", 3.00
elif 70 <= a <= 79: grade, score = "B+", 3.00
elif 70 <= a <= 79: grade, score = "B+", 3.00
elif 70 <= a <= 79: grade, score = "B+", 3.00
else: grade, score = "B+", 3.00

print(f"{l2}\nyour score is   : {a} score\nyour grade is   : {score}\n{l2}")
