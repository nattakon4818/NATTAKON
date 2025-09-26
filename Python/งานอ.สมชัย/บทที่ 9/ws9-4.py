def main():
    print('Test open file for read.')
    fin = open('mydata.txt', encoding='utf-8')
    print('Open file mydata.txt')
    print('Use read to read data from file.')
    data = fin.read()
    print(data)
    fin.close
    print('NOw closed file')

if __name__ == "__main__":
    main()