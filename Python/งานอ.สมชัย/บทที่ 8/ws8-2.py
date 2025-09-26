def read_scores():
    scores = ()
    count = 1
    while True:
        score = int(input(f"Enter score #{count} ( -1 to exit) : "))
        if score >= 0 and score <= 100:
            scores += (score,)
            count += 1
        elif score == -1:
            break
    count -= 1
    return( scores )

def check_grades(scores):
    grades = ()
    for score in scores:
        grade = ""
        if score >= 80: grade = "A"
        elif score >= 70: grade = "B"
        elif score >= 60: grade = "C"
        elif score >= 50: grade = "D"
        else: grade = "F"
        grades += (grade,)
    return(grades)

def report_grades(scores, grades):
    result = ("=" * 24 + "\n| No. | Scores | Grade | \n" + ("=" * 24) + "\n")
    for n in range(len(scores)):
        result += f"| %2d  |   %3d  |   %s   |\n" % (n, scores[n], grades[n])
    result += ("=" * 24)
    print(result)

scores = read_scores()
grades = check_grades( scores )
report_grades( scores, grades)