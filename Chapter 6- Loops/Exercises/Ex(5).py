sandwich_orders = ["Pastrami","Chicken", "Nutella", "Vegetables", "Cheese","Pastrami"]
finished_sandwiches = []

print("deli has run out of pastrami")
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(sandwich+" sandwich is made.")
    finished_sandwiches.append(sandwich)

print("\nThese Sandwiches is finished:")
for sandwich in finished_sandwiches:
    print(sandwich+" sandwich")
