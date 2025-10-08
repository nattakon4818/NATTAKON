from random import randint

def random_and_save(filename, colum, day):
    file = open(filename, 'w')

    for i in range(1, colum + 1):
        total = 0
        for j in range(2, day + 1):
            sale = randint(500, 5000)
            total += sale
            file.write(str(sale))
            if j < day:
                file.write(", ")
        file.write(", " + str(total) + "\n")

    file.close()

def report_sale(filename):
    
    print(f'{"Report Sale":>40}')


random_and_save('sale.txt', 5, 3)
report_sale('sale.txt')