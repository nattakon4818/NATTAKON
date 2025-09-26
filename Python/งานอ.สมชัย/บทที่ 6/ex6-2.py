while True:
    text = input("Enter text(enter-exit) : ")
    
    if text == "":
        break
    
    if text.isalpha():
        print("Text is alphabetic")

    elif text.isdigit():
        print("Text is digit")

    elif text.isalnum():
        print("Text is alpha and numeric")

    else:
        print("Text is string")
