import MyNattakon

def main():
    branches = 15
    days = 7

    sales, sum_days, sum_week = MyNattakon.generate_sales(branches, days)

    MyNattakon.print_report(branches, days, sales, sum_days, sum_week)

if __name__ == "__main__":
    main()