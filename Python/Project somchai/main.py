from Food_and_Drink import *
from members import *

DATAFILE = 'Members.txt'

def main():
    print('Login')
    mb = 'Enter your name : '
    membername = input(mb)
    if membername == str: member(DATAFILE)


    # h = f':{'Menu':^52}:'
    # line = '-' * len(h)
    # menu = f": {'1. Food':<51}:\n: {'2. Drink':<51}:\n: {'3. Dessert':<51}:\n: {'4. Exit':<51}:"
    # print(line, h, line, sep='\n')




if __name__ == '__main__':
    main()