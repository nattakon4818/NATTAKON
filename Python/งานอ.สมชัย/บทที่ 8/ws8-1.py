def check_rate(total):
    rates = (0.10, 0.075, 0.05, 0.025, 0.0)
    total_sales = (20000.0, 10000.0, 5000.0, 1000, 1.0)
    for n in range(len(total_sales)):
        if total > total_sales[n]:
            return(rates[n])
        
def get_sale():
    global sales
    for n in range(1, 8):
        sale = float(input(f"Enter sale day {n} : "))
        sales += (sale,)

def report():
    print(f"\nTotal sale : {total_sale:,.2f}")
    print(f"Commission rate : {rate * 100:.2f}")
    print(f"Total commission : {commision:,.2f}")

sales = ()
get_sale()
total_sale = sum( sales )
rate = check_rate(total_sale)
commision = total_sale * rate
report()