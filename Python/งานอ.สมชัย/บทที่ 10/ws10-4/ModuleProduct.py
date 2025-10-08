def add_product(filename):
    print('Enter data product.')
    prod_id = input('Input product id : ')
    prod_name = input('Input product name : ')
    prod_price = input('Input product price : ')
    prod_qty = input('Input product quantity : ')
    try:
        fout = open(filename, 'a')
        fout.write(f"{prod_id},{prod_name},{prod_price},{prod_qty}\n")
        fout.close()
    except FileNotFoundError:
        print(f'{filename} is not found')
    else:
        print('Save Data Product allready.\n')

def report_from_file(filename):
    n = 0
    try:
        with open(filename) as fin:
            for prod in fin:
                n += 1
                prod_list = prod.rstrip('\n').split(',')
                prod_str = ':'.join(f'{data:>5}' for data in prod_list)
                print(f'Product {n:2} : ' + prod_str + ':')
            print('Total product : ', n, '\n')
    except FileNotFoundError:
        print(f'{filename} is not found')

def read_product(filename):
    products = []
    try:
        with open(filename) as fin:
            for prod in fin:
                prod = prod.rstrip('\n')
                products.append(prod.split(','))
    except FileNotFoundError:
        print(f'{filename} is not found')
    else:
        return(products)

def report_product(products):
    mess = 'Report Product'.center(62) + '\n'
    mess += ('-' * 62) + '\n'
    mess += '| No.|  ID  |  Name     |    Price   |Quantity|    Total    |\n'
    mess += ('-' * 62) + '\n'
    n = 1
    try:
        for prod in products:
            price = float(prod[2])
            qty = float(prod[3])
            total = price * qty
            mess += f'|{n:3} |{prod[0]:5} |{prod[1]:10} |'
            mess += f' {price:>11,.2f} |{float(prod[3]):>7,} |'
            mess += f' {total:>11,.2f} |\n'
            n += 1
        mess += ('-' * 62)
    except IndexError:
        print('Index list not found.')
    else:
        print(mess)
 