items = ["Pen", "Book", "Bag"]
stock = [50, 30, 20]

for i in range(len(items)):
    print(items[i], "Stock:", stock[i])

item = input("Enter item name: ")
quantity = int(input("Enter quantity sold: "))

if item in items:
    index = items.index(item)

    if quantity <= stock[index]:
        stock[index] -= quantity
        print("Updated stock:", stock[index])
    else:
        print("Insufficient stock")
else:
    print("Item not found")