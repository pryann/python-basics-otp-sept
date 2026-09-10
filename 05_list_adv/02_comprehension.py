net_prices = [1000, 2000, 3000, 4000]
vat_rate = 1.27
# gross_prices = []

# for i in net_prices:
#     gross_prices.append(i * vat_rate)

gross_prices = [i * vat_rate for i in net_prices]

print(gross_prices)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# even = []
# for i in numbers:
#     if i % 2 == 0:
#         even.append(i)

even = [i for i in numbers if i % 2 == 0]

print(even)
