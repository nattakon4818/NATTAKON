from random import randint

def inputSale( Sales ):
    for n in range(1, 5):
        key = input('Enter branch name : ')
        value = []
        for m in range(1, 5):
            data = float(input(f'Enter sales in Quarter {m} : '))
            value.append(data)
        Sales[key] = value

def calTotalSale(Sales):
    for key in Sales:
        Sales[key].append(sum(Sales[key]))

def reportSale(Sales):
    result = ('=' * 74) + "\n"
    result += "|No.| Branch Name | Quarter1 | Quarter2 | Quarter3 | Quarter4 |   Total  |"
    result += "\n" + ('=' * 74) + "\n"
    n = 1
    for key in Sales:
        result += "|%2d | %11s |" % (n, key)
        for sale in Sales[key]:
            result += " %8.2f |" % (sale)
        result += "\n"
    result += ('=' * 74) + "\n"
    print(result)

Sales = {}
inputSale(Sales)
calTotalSale(Sales)
reportSale(Sales)
for key in Sales:
    print(key, Sales[key])