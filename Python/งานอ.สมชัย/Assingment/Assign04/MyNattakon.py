def find_max_digit(number):
    return max([int(d) for d in str(number)])

def is_palindrome(number):
    return str(number) == str(number)[::-1]

def number_to_text(number):
    digits = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    return " ".join([digits[int(d)] for d in str(number)])

def decimal_to_binary(number):
    return bin(number)[2:]