guestlists=["zeji","diether","argeo"]
for friend in guestlists:
    print("Hi there "+friend+", would you like to come to my dinner")

#list removal
removedguest = guestlists.pop()
print("Sorry,",removedguest,"can't be invited (Removed from list)")
removedguest = guestlists.pop()
print("Sorry,",removedguest,"can't be invited (Removed from list)")

print("\nGuest left")
for guest in guestlists:
    print(guest)

#list clear
print("\nThe Invitation is cancelled, the list is blank")
del guestlists[:]
print(guestlists)
