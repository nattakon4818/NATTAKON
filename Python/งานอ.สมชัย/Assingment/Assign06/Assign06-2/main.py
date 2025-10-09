from ScoreModule import *

def main():
    while True:
        choice  = int(input(' Main Menu\n---------------\n 1. Add Score studednt\n 2. Report Score of Student\n 3. Exit\nEnter Choice : '))

        if choice == 1:
            add_score('score.txt')
        elif choice == 2:
            report_score('score.txt')
        elif choice == 3:
            print('Exit Program.')
            break
        else:
            print('Please Enter 1-3 only, Input again\n')

if __name__ == "__main__":
    main()