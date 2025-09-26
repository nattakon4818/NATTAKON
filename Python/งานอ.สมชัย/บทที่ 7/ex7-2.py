def check_palindrome(number):
    str_num = str(number)
    return str_num == str_num[::-1]

# ทดสอบ
print(check_palindrome(12344321))  # ผลลัพธ์: True
