# print(f"\n{"Grade Report":^65}",f"{"=" * 67}",f":{"Sub No.":^7}:{" Subject Name":<27}:{"Mark":^6}:{"Grade":^7}:{"Credite":^7}:{"Points":^6}:",f"{"=" * 67}", sep='\n')
# print(f":{"1":^7}: {'':<26}:{'':^6}:{'':^7}:{'':^7}:{"":^6}:", sep='\n')
# print(f":{"2":^7}: {'':<26}:{'':^6}:{'':^7}:{'':^7}:{"":^6}:", sep='\n')
# print(f":{"3":^7}: {'':<26}:{'':^6}:{'':^7}:{'':^7}:{"":^6}:", sep='\n')
# print(f":{"4":^7}: {'':<26}:{'':^6}:{'':^7}:{'':^7}:{"":^6}:", sep='\n')
# print(f":{"5":^7}: {'':<26}:{'':^6}:{'':^7}:{'':^7}:{"":^6}:", sep='\n')
# print(f":{"6":^7}: {'':<26}:{'':^6}:{'':^7}:{'':^7}:{"":^6}:",f"{"=" * 67}", sep='\n')

# g = 36, 40, 50, 80
# s_g = sum(g)

# print(f": {"Grade Point Average(GPA) : ":<26}{s_g:<37}:",f"{"=" * 67}", sep='\n')

head = ": Program Cal Grade :"
line, score, grade, result, total, Max, Min = "=" * len(head), 0, "", "", 0, 0, 0
print(line, head, line, sep='\n')
for i in range(1, 6):
    score = int(input(f"Enter score #{str(i)} : "))
    if score >= 80: grade = 'A'
    elif score >= 70: grade = 'B'
    elif score >= 60: grade = 'C'
    elif score >= 50: grade = 'D'
    else: grade = 'F'
    result += "|   " + str(i) + " |  " + format(score, ">3") + "  |   " + grade + "   |" + "\n"
    total += score
    if i == 1 : Max = Min = score
    else:
        Max = max(Max, score)
        Min = min(Min, score)

h1, h2 = "    Report Grade", "| No. | Score | Grade |"
l = "=" * len(h2)
print("", h1, l, h2, l, result,l, f"|Averang Score| {total / 5:.2f} |", f"|Maximum Score| {Max}    |", f"|Minimum Score| {Min}    |", l, sep='\n')



head = ": Program Cal Vat :"
line, amount, result, total, Max, Min = "=" * len(head), 0, "", 0, 0, 0
print(line, head, line, sep='\n')
for i in range(1, 2):
    amount = int(input(f"Enter amount of day {str(i)} : "))
    sales = amount // 1.07
    vat = amount - sales
    result += "|  " + str(i) + "  |    " + format(amount, ">3") + "    |   " + format(vat, ",.2f") + "    |    " + format(sales, ",.2f") + "  |" + "\n"

    total += amount
    if i == 1 : Max = Min = amount
    else:
        Max = max(Max, amount)
        Min = min(Min, amount)

h1, h2 = "                 Report Sale of Fitm Shop", "| day |     Amounts   |    Vat(7%)   |      Sales     |"
l = "=" * len(h2)
print("", h1, l, h2, l, result,l, f"Maximum Amount : {Max}", f"Minimum Amount :  {Min}", sep='\n')
