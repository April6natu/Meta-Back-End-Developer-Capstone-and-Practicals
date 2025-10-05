def calculate_tax(bill, tax_rate):
    return round((bill * tax_rate) / 100.0, 2)

print('Total Tax:', calculate_tax(175.00, 15))

print('Total Tax:', calculate_tax(164.33, 22))