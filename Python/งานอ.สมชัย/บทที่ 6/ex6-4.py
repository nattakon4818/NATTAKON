import random

head, h = "Main  Menu", "|Grade| Total|"
line, l = "=" * len(head), "-" * len(h)
total, count_A, count_B, count_C, count_D, count_F  = 0, 0, 0, 0, 0, 0

while True:
    print(head, line, " 1. Input Number of Score", " 2. Random Score and Check Grade", " 3. Exit", sep='\n')

    choice = input("Enter Choice : ")

    if choice == '1':
        total = int(input("Enter number of score : "))

    elif choice == '2':
        count_A, count_B, count_C, count_D, count_F  = 0, 0, 0, 0, 0

        print("\nStart Random Score ...\nCheck Grade ...\n")

        for i in range(total):
            score = random.randint(40, 90)

            if score >= 80: count_A += 1
            elif score >= 70: count_B += 1
            elif score >= 60: count_C += 1
            elif score >= 50: count_D += 1
            else: count_F += 1

        print(l, h, l, f"|  A  | {count_A:>4} |", f"|  B  | {count_B:>4} |", f"|  C  | {count_C:>4} |", f"|  D  | {count_D:>4} |", f"|  F  | {count_F:>4} |", l, f"|Total| {total:>4} |", l, "\n", sep='\n')

    elif choice == '3':
        print("Exit Program")
        break
