def add_score(filename):
    print('\nAdd Score Student')

    project = input('Enter score Project : ')
    homework = input('Enter score homework : ')
    midterm = input('Enter score midterm : ')
    final = input('Enter score final : ')

    with open("score.txt", 'a') as file:
        file.write(f"{project},{homework},{midterm},{final}\n")
    print('Save data already.\n')

def report_score(filename):
    with open("score.txt", 'r') as file:
        data = file.readlines()
    
    total_project = total_hw = total_mid = total_final = total_all = 0

    h = "Report of Score Student"
    header = f"| No.|Project(15)|  HW(25)   |  Mid(30)  | Final(30) |Total(100) |GRADE|"
    line = "-" * len(header)

    print(f"\n{h:^{len(header)}}", line, header, line, sep='\n')

    for i, l in enumerate(data, start=1):
        l = l.strip().split(",")
        project = float(l[0])
        hw = float(l[1])
        mid = float(l[2])
        final = float(l[3])
        total = project + hw + mid + final

        if total >= 80: grade = "A"
        elif total >= 75: grade = "B+"
        elif total >= 70: grade = "B"
        elif total >= 65: grade = "C+"
        elif total >= 60: grade = "C"
        elif total >= 55: grade = "D+"
        elif total >= 50: grade = "D"
        else: grade = "F"
    
        print(f"|{i:>3} :{project:>10.2f} |{hw:>10.2f} |{mid:>10.2f} |{final:>10.2f} |{total:>10.2f} |  {grade:<3}|")

        total_project += project
        total_hw += hw
        total_mid += mid
        total_final += final
        total_all += total
    
    n = len(data)
    avg_project = total_project / n
    avg_hw = total_hw / n
    avg_mid = total_mid / n
    avg_final = total_final / n
    avg_total = total_all / n

    print(line, f"| Avg|{avg_project:>10.2f} |{avg_hw:>10.2f} |{avg_mid:>10.2f} |{avg_final:>10.2f} |{avg_total:>10.2f} |{'':^5}|", line, '', sep='\n')