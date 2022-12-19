"""
total = 0
get number of items
while items < 0:
    display Invalid items
    get number of items

"""
total = 0
items = int(input("Number of items: "))
while items < 0:
    print("Invalid items")
    items = int(input("Number of items: "))
for i in range(items):
    Price = float(input("Price of items: "))
    total += Price
if total > 100:
    discount = total * 0.1
    total_price = total - discount
print(f"Total price for {items} Items is ${total_price:.2f}")
