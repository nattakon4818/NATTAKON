print(f"\n>>  Program Calculate Grade <<\n{'=' * 30}\n\nInput Data:")

score, sub, grade, total, total_p, pooint, credit = 0, "", "", 0, 0, 0, 3
heade = f"{"Grade Report ":>37}"
h = ":Sub No.: Subject Name               : Mark : Grade :Credit:Points:"
l = "=" * len(h)
result = ""

for i in range(1, 7):
    sub = input(f"Enter subject name({i}) : ")
    score = float(input(f"Enter subject score({i}) : "))
    print()

    if 80 <= score <= 100: grade, pooint = "A", 4.0
    elif 70 <= score <= 79: grade, pooint = "B", 3.0
    elif 60 <= score <= 69: grade, pooint = "C", 2.0
    elif 50 <= score <= 59: grade, pooint = "D", 1.0
    else: grade, pooint = "F", 0.0

    total += credit
    total_p += pooint
    result += ":   " + str(i) + "   : " + format(sub, '<27') + ":" + format(score, '^6') + ":" + format(grade, '^7') + ":" + format(credit, '^6') + ":" + format(pooint, '>5') + " :\n"
result += format(l) + "\n:" + format("Total", '>37') + "              :" + format(total, '>3') + "   :" + format(total_p, '>5') + " :\n" + format(l) + "\n: " + format("Grade Point Average(GPA) : ", '<26') + format(total_p / 6, '<37') + ":\n" + format(l)

print(heade, l, h, l, result, sep='\n')