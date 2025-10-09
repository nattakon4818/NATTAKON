def member(filename):
    print('Member List')
    name = input('Enter name : ')
    fout = open(filename, 'a')
    fout.write(name + '\n')
    fout.close()

def read_member(filename):
    with open(filename, 'r') as fin:
        for data in fin:
            print(data, end='')

# member('Members.txt')