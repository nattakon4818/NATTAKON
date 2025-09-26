from random import randint

def randomScores( scores ):
    for n in range(1, 11):
        scores[n] = randint(30, 100)

def checkGrade(scores, grades):
    GRADES = { 80: 'A', 70: 'B', 60: 'C', 50: 'D', 0: 'F'}
    for n, score in scores.items():
        for key, value in GRADES.items():
            if (score >= key):
                grades[n] = value
                break

def reportGrade(scores, grades):
    print('=' * 23)
    print("| No. | Score | Grade |")
    print('=' * 23)
    for n in scores:
        print(f"| %3d |  %3d  |   %s   |" % (n, scores[n], grades[n]))
    print('=' * 23)

scores = {}
grades = {}
randomScores(scores)
print(scores)
checkGrade(scores, grades)
print(grades)
reportGrade(scores, grades)