def num_to_text(number):
    digit_words = {
        '0': 'ZERO',
        '1': 'ONE',
        '2': 'TWO',
        '3': 'THREE',
        '4': 'FOUR',
        '5': 'FIVE',
        '6': 'SIX',
        '7': 'SEVEN',
        '8': 'EIGHT',
        '9': 'NINE'
    }

    str_num = str(number)
    word_list = [digit_words[digit] for digit in str_num]
    return ' '.join(word_list)

# ทดสอบ
print(num_to_text(638342))
