def calculate_discount(price, discount_percent):
  discount_amount = 0
  if (discount_percent >= 20):
    discount_amount = price * (discount_percent / 100)
    bill = price - discount_amount
    return bill
  else:
    return price
  
print(calculate_discount(int(input("Enter the price: ")), int(input("Enter the discount percent: "))))