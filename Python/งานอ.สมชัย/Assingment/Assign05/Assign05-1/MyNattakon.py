import random

def generate_sales(branches, days):
    sales = []
    sum_days = [0] * days
    sum_week = 0

    for i in range(branches):
        daily = [random.randint(100, 5000) for _ in range(days)]
        total = sum(daily)
        sales.append([*daily, total])

        for d in range(days):
            sum_days[d] += daily[d]
        sum_week += total

    return sales, sum_days, sum_week

def print_report(branches, days, sales, sum_days, sum_week):
    h = ": No.:   Day  1   :   Day  2   :   Day  3   :   Day  4   :   Day  5   :   Day  6   :   Day  7   :   Total    :"
    l = "-" * len(h)

    print(f"{"Report of Sales":>63}", l, h, l, sep="\n")

    for i, s in enumerate(sales, 1):
        row = f": {i:>2} :"
        for d in range(days):
            row += f" {s[d]:10,.2f} :"
        row += f" {s[-1]:10,.2f} :"
        print(row)

    print(l)

    row_total = "Total:"
    for d in range(days):
        row_total += f" {sum_days[d]:10,.2f} |"
    row_total += f" {sum_week:10,.2f} |"
    print(row_total)
    print(l)

if __name__ == "__main__":
    branches = 5
    days = 7
    sales, sum_days, sum_week = generate_sales(branches, days)
    print_report(branches, days, sales, sum_days, sum_week)