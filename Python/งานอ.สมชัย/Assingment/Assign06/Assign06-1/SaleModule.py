from random import randint

def random_and_save(filename, colum, day):
    with open(filename, 'w') as file:
        for i in range(1, colum + 1):
            for a in range(1, day + 1):
                sale = randint(500, 5000)
                file.write(str(sale))
                if a < day:
                    file.write(",")
            file.write("\n")

def report_sale(filename):
    with open(filename, 'r') as file:
        data = file.readlines()

    first_line = data[0].strip()
    days = first_line.split(',')
    day = len(days)
    colum = len(data)

    h = "Report of Sales"
    header = ": No.:"

    for d in range(1, day + 1):
        header += f"   Day  {d}   :"
    header += "   Total    :"

    line = "-" * len(header)

    print(f"{h:^{len(header)}}", line, header, line, sep='\n')

    grand_total = 0  # ยอดรวมทั้งหมด
    day_totals = [0] * day

    for i in range(colum):
        line_data = data[i].strip()
        day_list = line_data.split(',')

        row = f":{i + 1:>3} :"  # หมายเลขสาขา
        branch_total = 0  # ยอดรวมของสาขานี้

        for d in range(day):
            sale = int(day_list[d])
            branch_total += sale
            day_totals[d] += sale
            row += f"{sale:>11,.2f} :"

        row += f"{branch_total:>11,.2f} :"
        grand_total += branch_total

        print(row)

    # แสดงยอดรวมทั้งหมด
    total_day_row = f"Total:"
    grand_total_2 = 0
    for dt in day_totals:
        total_day_row += f"{dt:>11,.2f} :"
        grand_total_2 += dt
    total_day_row += f"{grand_total_2:>11,.2f} :"

    print(line, total_day_row, line, sep='\n')
