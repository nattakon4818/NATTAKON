import random

def random_and_save(filename, rows, cols):
    with open(filename, 'w') as f:
        for _ in range(rows):
            sales = [str(random.randint(500, 5000)) for _ in range(cols)]
            f.write(','.join(sales) + '\n')

def report_sale(filename):
    print('\n\t\t\tReport of Sales\n')
    with open(filename, 'r') as f:
        data = []
        for line in f:
            sales = list(map(int, line.strip().split(',')))
            data.append(sales)

    total_sales = []
    for i, row in enumerate(data):
        total = sum(row)
        total_sales.append(total)
        print(f'Branch {i+1:2}: ', end='')
        for value in row:
            print(f'{value:8,}', end=' ')
        print(f'| {total:10,}')

    max_sale = max(total_sales)
    min_sale = min(total_sales)
    avg_sale = sum(total_sales) / len(total_sales)

    print('\nSummary:')
    print(f'Maximum Sale: {max_sale:,.2f}')
    print(f'Minimum Sale: {min_sale:,.2f}')
    print(f'Average Sale: {avg_sale:,.2f}')