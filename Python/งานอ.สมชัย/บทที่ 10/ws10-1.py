try:
    num1 = int(input("Enter value number1 : "))
    num2 = int(input("Enter value number2 : "))
    print('number1 + number2 =', num1 + num2)
    print('number1 - number2 =', num1 - num2)
    print('number1 * number2 =', num1 * num2)
    print('number1 / number2 =', num1 / num2)
except ValueError:
    print("You input data in correct, input again.")
except ZeroDivisionError:
    print('Number is not divide with zero.')
except NameError:
    print('Use variable not define.')
except:
    print('Error in pregram.')
print('This is test Exception.')