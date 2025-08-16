head = "| Tax Main Menu |"
line = "=" * len(head)
h = "|         Net     Income      |Tax Rate|                 Tax                  |"
l = "=" * len(h)
salary = 0

while True:
    print(line, head, line, f"{" 0. Exit"}", f"{" 1. Input Salaey"}({salary:,.2f})", f"{" 2. Display Tax"}", sep='\n')

    choice = input("Enter choice : ")

    if choice == '0':
        print("\nExit Program ...")
        break

    elif choice == '1':
        salary = float(input("Enter salary : "))
        print()

    elif choice == '2':
        income = salary * 12
        discount = 100000
        net_income = income - discount
        tax = 0.0

        print(f"\nSalary : {salary:,.2f}\nIncome : {salary * 12:,.2f}\nDiscount : 100,000.00\nNet Income : {net_income:,.2f}", "\nReport Tax:", l, h, l, sep='\n')

        if net_income > 0:
            lower = 0
            upper = min(net_income, 150000)
            rate = 0.00
            taxable = upper - lower
            tax_amount = taxable * rate
            tax += tax_amount
            range_str = f"{lower + 1:>12,.2f}{'-':^3}{upper:>12,.2f}"
            calc_str = f"{taxable:,.2f} * {rate:.2f}"
            print(f"| {range_str} | {rate*100:>4.0f}%  | {calc_str:<20} | {tax_amount:>13,.2f} |")

        if net_income > 150000:
            lower = 150000
            upper = min(net_income, 300000)
            rate = 0.05
            taxable = upper - lower
            tax_amount = taxable * rate
            tax += tax_amount
            range_str = f"{lower + 1:>12,.2f}{'-':^3}{upper:>12,.2f}"
            calc_str = f"{taxable:,.2f} * {rate:.2f}"
            print(f"| {range_str} | {rate*100:>4.0f}%  | {calc_str:<20} | {tax_amount:>13,.2f} |")

        if net_income > 300000:
            lower = 300000
            upper = min(net_income, 500000)
            rate = 0.10
            taxable = upper - lower
            tax_amount = taxable * rate
            tax += tax_amount
            range_str = f"{lower + 1:>12,.2f}{'-':^3}{upper:>12,.2f}"
            calc_str = f"{taxable:,.2f} * {rate:.2f}"
            print(f"| {range_str} | {rate*100:>4.0f}%  | {calc_str:<20} | {tax_amount:>13,.2f} |")

        if net_income > 500000:
            lower = 500000
            upper = min(net_income, 750000)
            rate = 0.15
            taxable = upper - lower
            tax_amount = taxable * rate
            tax += tax_amount
            range_str = f"{lower + 1:>12,.2f}{'-':^3}{upper:>12,.2f}"
            calc_str = f"{taxable:,.2f} * {rate:.2f}"
            print(f"| {range_str} | {rate*100:>4.0f}%  | {calc_str:<20} | {tax_amount:>13,.2f} |")

        if net_income > 750000:
            lower = 750000
            upper = min(net_income, 1000000)
            rate = 0.20
            taxable = upper - lower
            tax_amount = taxable * rate
            tax += tax_amount
            range_str = f"{lower + 1:>12,.2f}{'-':^3}{upper:>12,.2f}"
            calc_str = f"{taxable:,.2f} * {rate:.2f}"
            print(f"| {range_str} | {rate*100:>4.0f}%  | {calc_str:<20} | {tax_amount:>13,.2f} |")

        if net_income > 1000000:
            lower = 1000000
            upper = min(net_income, 2000000)
            rate = 0.25
            taxable = upper - lower
            tax_amount = taxable * rate
            tax += tax_amount
            range_str = f"{lower + 1:>12,.2f}{'-':^3}{upper:>12,.2f}"
            calc_str = f"{taxable:,.2f} * {rate:.2f}"
            print(f"| {range_str} | {rate*100:>4.0f}%  | {calc_str:<20} | {tax_amount:>13,.2f} |")

        if net_income > 2000000:
            lower = 2000000
            upper = min(net_income, 5000000)
            rate = 0.30
            taxable = upper - lower
            tax_amount = taxable * rate
            tax += tax_amount
            range_str = f"{lower + 1:>12,.2f}{'-':^3}{upper:>12,.2f}"
            calc_str = f"{taxable:,.2f} * {rate:.2f}"
            print(f"| {range_str} | {rate*100:>4.0f}%  | {calc_str:<20} | {tax_amount:>13,.2f} |")

        if net_income > 5000000:
            lower = 5000000
            upper = net_income
            rate = 0.35
            taxable = upper - lower
            tax_amount = taxable * rate
            tax += tax_amount
            range_str = f"{'':>12}{'>':^3}{lower:<12,.2f}"
            calc_str = f"{taxable:,.2f} * {rate:.2f}"
            print(f"| {range_str} | {rate*100:>4.0f}%  | {calc_str:<20} | {tax_amount:>13,.2f} |")

        print(l, f"|{'Total Tax':^61}|{tax:>14,.2f} |", l, sep='\n')
        print()