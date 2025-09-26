import random

def grade(total):
    if total >= 80: return "A"
    elif total >= 75: return "B+"
    elif total >= 70: return "B+"
    elif total >= 65: return "C+"
    elif total >= 60: return "C"
    elif total >= 55: return "D+"
    elif total >= 50: return "D"
    else: return "F"

def g_students(number):
    stus = []
    sum_hw = 0
    sum_mid = 0
    sum_final = 0
    sum_total = 0

    for i in range(number):
        hw = random.randint(0, 30)
        mid = random.randint(0, 35)
        final = random.randint(0, 35)
        total = hw + mid + final
        grades = grade(total)

        stus.append([hw, mid, final, total, grades])

        sum_hw += hw
        sum_mid += mid
        sum_final += final
        sum_total += total

    avg = [sum_hw / number, sum_mid / number, sum_final / number, sum_total / number]

    h1 = "                    Report of Sales"
    h2 = "| No.|  HW(30)  |  MID(35) | FINAL(35)|TOTAL(100)|GRADE|"
    l = "-" * len(h2)

    print(h1, l, h2, l, sep='\n')

    for i, s in enumerate(stus, 1):
        hw, mid, final, total, grades = s
        print(f"| {i:>2} : {hw:8.2f} | {mid:8.2f} | {final:8.2f} | {total:8.2f} | {grades:^3} |")

    print(l, f"| AVG| {avg[0]:8.2f} | {avg[1]:8.2f} | {avg[2]:8.2} | {avg[3]:8.2f} | {' ':^3} |", l, sep='\n')
