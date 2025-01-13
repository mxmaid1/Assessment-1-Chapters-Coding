places=["BurjKhalifa","AbuDhabi","California"]
print("original list:")
print(places)

print("\nsorted modified list:")
print(sorted(places))

print("\nlist still original order after sorted():")
print(places)

print("\nreverse sorted modified list:")
print(sorted(places, reverse=True))

print("\nlist still original order after sorted(?,reverse=True):")
print(places)

places.reverse()
print("\n.reverse() modified list:")
print(places)

places.reverse()
print("\nrepeat .reverse() modified list:")
print(places)

places.sort()
print("\n.sort() modified list:")
print(places)

places.sort(reverse=True)
print("\n.sort(reverse=True) modified list:")
print(places)