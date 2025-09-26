from random import randint

def genData(std, sub):
    scores = []
    for r in range(std):
        scores.append([])
        for c in range(sub):
            scores[r].append( randint(30, 100) )
    return scores

def reportData( scores ):
    col = 6 * len(scores[0]) + 5
    line = '-' * col
    result = '|No.|'
    for n in range(1, len(scores[0]) + 1): result += f'Sub{n:2}|'
    result = line + "\n" + result + "\n" + line + "\n"
    n = 1
    for score in scores:
        result += f'|{n:2} |'
        for s in score: result += f' {s:3} |'
        result += '\n'
        n += 1
    result += line + "\n"
    print(result)

def Main():
    student = int(input("Enter number of studebt : "))
    subject = int(input("Enter number of subject : "))
    Scores = genData(student, subject)
    reportData(Scores);

if __name__ == "__main__":
    Main()