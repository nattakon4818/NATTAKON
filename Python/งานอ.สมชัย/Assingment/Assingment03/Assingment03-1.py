import random

while True:
    print(f"\nMain Menu\n{("=") * 12}\n1. Play game\n2. Exit")

    choice = input("Enter choice : ")

    if choice == "1":
        random_number = random.randint(1, 99)
        limit = 6

        print("\nNow Play game")

        for round in range(1, limit + 1):
            guess = int(input(f"Enter guess number(#{round}) : "))

            if guess == random_number:
                print(f"\nYou win, use guess {limit} times.\nNumber guess is {random_number}.")
                break
            elif guess > random_number:
                print("Your value is more than")
            else:
                print("Youe value is less than")

        else:
            print(f"\nYou lose, random number is {random_number}.")

    elif choice == "2":
        print("Exit Program...\n\nPress any key to continue ...")
        break
    else:
        print("No choice, enter again.")