from ModuleProduct import *

def main():
    PRODUCTFILE = 'product.txt'
    menu = ('=' * 17) + '\n| Product  Menu |\n' + ('=' * 17)
    menu += '\n1. Add Product\n2. Report Product from File\n'
    menu += '3. Report Product by Price\n4. Exit\nEnter Choice : '
    while True:
        choice = input(menu)
        if choice == '1' : add_product(PRODUCTFILE)
        elif choice == '2' : report_from_file(PRODUCTFILE)
        elif choice == '3' :
            products = read_product(PRODUCTFILE)
            report_product(products)
        elif choice == '4' : break
        else: print('No choice, input aain.')
    print('Exit Program.')

if __name__ == '__main__':
    main()