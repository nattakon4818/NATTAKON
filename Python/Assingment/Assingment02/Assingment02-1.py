print(">> Program Palindrome Number <<")

number = int(input("Enter integer number : "))
number = str(number)

for n in range(len(number)):
    f = number[n]
    b = number[-(n+1)]
    if f == b:
        print(f"Digit {f} equal to Digit {b}")
    else:
        print(f"Digit {f} not equai to Digit {b}")
        break
if f == b:
    print(f"Your enter number : {number} is Palindrome Number.")
else:
    print(f"Your enter number : {number} is not Palindrome Number.")
print()