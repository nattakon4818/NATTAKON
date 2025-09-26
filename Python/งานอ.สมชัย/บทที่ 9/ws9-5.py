def read_data(filename):
    datas = []
    fin = open(filename, encoding='utf-8')
    data = fin.readline()
    while data != "":
        datas.append(data)
        data = fin.readline()
    fin.close()
    return(datas)

def main():
    fin = open('mydata.txt', encoding='utf-8')
    print('Open file mydata.txt')
    print('Use readline to read from file.')
    data1 = fin.readline(5)
    data2 = fin.readline()
    print(data1 + '+' + data2)
    fin.close()
    print('Now closed file.')
    scores = read_data('myscore.txt')
    print(scores)

if __name__ == "__main__":
    main()