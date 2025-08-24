print(f"\n>>  Program Calculate Grade <<\n{'=' * 30}\n\nInput Data:")

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

if 80 <= score1 <= 100: grade1, gp1 = "A", 4.0
elif 70 <= score1 <= 79: grade1, gp1 = "B", 3.0
elif 60 <= score1 <= 69: grade1, gp1 = "C", 2.0
elif 50 <= score1 <= 59: grade1, gp1 = "D", 1.0
else: grade1, gp1 = "F", 0.0
points1 = gp1 * credit

if 80 <= score2 <= 100: grade2, gp2 = "A", 4.0
elif 70 <= score2 <= 79: grade2, gp2 = "B", 3.0
elif 60 <= score2 <= 69: grade2, gp2 = "C", 2.0
elif 50 <= score2 <= 59: grade2, gp2 = "D", 1.0
else: grade2, gp2 = "F", 0.0
points2 = gp2 * credit

if 80 <= score3 <= 100: grade3, gp3 = "A", 4.0
elif 70 <= score3 <= 79: grade3, gp3 = "B", 3.0
elif 60 <= score3 <= 69: grade3, gp3 = "C", 2.0
elif 50 <= score3 <= 59: grade3, gp3 = "D", 1.0
else: grade3, gp3 = "F", 0.0
points3 = gp3 * credit

if 80 <= score4 <= 100: grade4, gp4 = "A", 4.0
elif 70 <= score4 <= 79: grade4, gp4 = "B", 3.0
elif 60 <= score4 <= 69: grade4, gp4 = "C", 2.0
elif 50 <= score4 <= 59: grade4, gp4 = "D", 1.0
else: grade4, gp4 = "F", 0.0
points4 = gp4 * credit

if 80 <= score5 <= 100: grade5, gp5 = "A", 4.0
elif 70 <= score5 <= 79: grade5, gp5 = "B", 3.0
elif 60 <= score5 <= 69: grade5, gp5 = "C", 2.0
elif 50 <= score5 <= 59: grade5, gp5 = "D", 1.0
else: grade5, gp5 = "F", 0.0
points5 = gp5 * credit

if 80 <= score6 <= 100: grade6, gp6 = "A", 4.0
elif 70 <= score6 <= 79: grade6, gp6 = "B", 3.0
elif 60 <= score6 <= 69: grade6, gp6 = "C", 2.0
elif 50 <= score6 <= 59: grade6, gp6 = "D", 1.0
else: grade6, gp6 = "F", 0.0
points6 = gp6 * credit

s_points = points1 + points2 + points3 + points4 + points5 + points6
total_credit = credit * 6
gpa = s_points / total_credit

h = ":Sub No.: Subject Name               : Mark : Grade :Credit:Points:"
l = "=" * len(h)

print(f"\n{"Grade Report ":>37}", l, h, l, 
      f":{"1":^7}: {sub1:<27}:{score1:^6}:{grade1:^7}:{credit:^6}:{points1:>5} :", 
      f":{"2":^7}: {sub2:<27}:{score2:^6}:{grade2:^7}:{credit:^6}:{points2:>5} :", 
      f":{"3":^7}: {sub3:<27}:{score3:^6}:{grade3:^7}:{credit:^6}:{points3:>5} :", 
      f":{"4":^7}: {sub4:<27}:{score4:^6}:{grade4:^7}:{credit:^6}:{points4:>5} :", 
      f":{"5":^7}: {sub5:<27}:{score5:^6}:{grade5:^7}:{credit:^6}:{points5:>5} :", 
      f":{"6":^7}: {sub6:<27}:{score6:^6}:{grade6:^7}:{credit:^6}:{points6:>5} :", 
      f"{"=" * 67}",f":{"Total":>37}              :{"18":>3}  :{s_points:>5} :", 
      f"{"=" * 67}",f": {"Grade Point Average(GPA) : ":<26}{gpa:<37}:", l, sep='\n')
