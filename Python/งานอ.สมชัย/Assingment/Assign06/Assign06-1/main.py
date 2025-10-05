from SaleModule import *
def main():
    print('Random sale and save to file "sale.txt".\n')
    random_and_save('sale.txt', 15, 7)
    report_sale('sale.txt')

if __name__ == "__main__":
    main()
