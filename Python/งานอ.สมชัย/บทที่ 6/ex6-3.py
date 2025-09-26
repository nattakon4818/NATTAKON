while True:
    text = input("Enter text(enter-exit) : ")
    text = text.lower()

    if text == "": break

    print(f"Text has 'a' : {text.count('a')}")
    print(f"Text has 'e' : {text.count('e')}")
    print(f"Text has 'i' : {text.count('i')}")
    print(f"Text has 'o' : {text.count('o')}")
    print(f"Text has 'u' : {text.count('u')}")