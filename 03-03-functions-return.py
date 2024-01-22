def tax_calc(money):
  return money * 0.35

def pay_tax(tax):
  print("thank you for paying", tax)

tax = tax_calc(15000000000)
pay_tax(tax)