net_price = int(input("Enter net price product : "))

price = net_price / (1 + 7 / 100)
vat   = net_price - price

print(f"Price product : {price:.1f}")
print(f"Vat product : {vat:.1f}")