print(f"\n>>  Program Calculate Grade <<\n{("=" * 30)}\n\nInput Data:")

credit = 3

sub1 = input("Enter subject name(1) : ")
score1 = float(input("Enter subject score(1) : "))
sub2 = input("\nEnter subject name(2) : ")
score2 = float(input("Enter subject score(2) : "))
sub3 = input("\nEnter subject name(3) : ")
score3 = float(input("Enter subject score(3) : "))
sub4 = input("\nEnter subject name(4) : ")
score4 = float(input("Enter subject score(4) : "))
sub5 = input("\nEnter subject name(5) : ")
score5 = float(input("Enter subject score(5) : "))
sub6 = input("\nEnter subject name(6) : ")
score6 = float(input("Enter subject score(6) : "))

if 80 <= score1 and score2 and score3 and score4 and score5 and score6 <= 100:
    grade, gp = "A", 4.0
elif 70 <= score1 and score2 and score3 and score4 and score5 and score6 <= 79:
    grade, gp = "B", 3.0
elif 60 <= score1 and score2 and score3 and score4 and score5 and score6 <= 69:
    grade, gp = "C", 2.0
elif 50 <= score1 and score2 and score3 and score4 and score5 and score6 <= 59:
    grade, gp = "D", 1.0
else:
    grade, gp = "F", 0.0

points = gp * credit
s_points = sum(points)
gpa = points / credit

print(f"\n{"Grade Report":^65}",f"{"=" * 67}",f":{"Sub No.":^7}:{" Subject Name":<27}:{"Mark":^6}:{"Grade":^7}:{"Credite":^7}:{"Points":^6}:",f"{"=" * 67}",f":{"1":^7}: {sub1:<26}:{score1:^6}:{grade:^7}:{credit:^7}:{points:^6}:",f":{"2":^7}: {sub2:<26}:{score2:^6}:{grade:^7}:{credit:^7}:{points:^6}:",f":{"3":^7}: {sub3:<26}:{score3:^6}:{grade:^7}:{credit:^7}:{points:^6}:",f":{"4":^7}: {sub4:<26}:{score4:^6}:{grade:^7}:{credit:^7}:{points:^6}:",f":{"5":^7}: {sub5:<26}:{score5:^6}:{grade:^7}:{credit:^7}:{points:^6}:",f":{"6":^7}: {sub6:<26}:{score6:^6}:{grade:^7}:{credit:^7}:{points:^6}:",f"{"=" * 67}",f":{"Total":^50}:{"18":^7}:{s_points:^6}:",f"{"=" * 67}",f": {"Grade Point Average(GPA) : ":<26}{gpa:<37}:",f"{"=" * 67}", sep='\n')