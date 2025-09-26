def find_max(number):
    return max(int(digit) for digit in str(number))

# ทดสอบ
print(find_max(6378942))  # Output: 9