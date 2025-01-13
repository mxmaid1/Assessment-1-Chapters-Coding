sandwich_orders = ["Chicken", "Nutella", "Vegetables", "Cheese"]
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(sandwich+" sandwich is made.")
    finished_sandwiches.append(sandwich)

print("\nThese Sandwiches is finished:")
for sandwich in finished_sandwiches:
    print(sandwich+" sandwich")
