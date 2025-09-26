def getPoint(grade):
    grades = ['A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'F']
    values = [4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]
    for n in range(len(grades)):
        if grade == grades[n]:
            return(values[n])

grades = []
while True:
    grade = input("Enter grade (Q-exit) : ").upper()
    if grade == "Q":
        break
    else:
        grades.append(grade)

result = ("=" * 23) + "\n|No.|Grade|Point|Total|\n" + ("=" * 23) + "\n"
totalPoint = 0.0
for n in range(len(grades)):
    point = getPoint(grades[n])
    total = point * 3
    totalPoint += total
    result += f"|{n + 1:2} |{grades[n].center(5)}| {point:3.1f} |{total:5.2f}|\n"
result += ("=" * 23) + "\n"
gpa = totalPoint / (len(grades) * 3)
result += f"Grade Point Average(GPA) : {gpa:5.2f}\n"
print(result)
print("End Program.")