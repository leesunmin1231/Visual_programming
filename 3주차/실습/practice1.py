import decimal
a=decimal.Decimal('0.0')
delta=decimal.Decimal('0.1')
for k in range(3):
    a+=delta
print(a)
