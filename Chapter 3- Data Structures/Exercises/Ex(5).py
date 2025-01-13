guestlists=["zeji","diether","argeo"]
for friend in guestlists:
    print("Hi there "+friend+", would you like to come to my dinner")
    
#removal
print(guestlists[guestlists.index("diether")], "can't make it to the dinner") 
guestlists.remove("diether")

#adding
guestlists.append("renan")
print(guestlists[guestlists.index("renan")], "is invited\n") 


print("updated invitation:")
for guest in guestlists:
    print(guest)
