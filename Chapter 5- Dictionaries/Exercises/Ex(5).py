pet1 = {
    "Animal":"Cat",
    "Owner":"Argeo"
}
pet2 = {
    "Animal":"Dog",
    "Owner":"John"
}
pet3 = {
    "Animal":"Rabbit",
    "Owner":"Jane"
}
pets = [pet1, pet2, pet3]
for pet in pets:
    print("Animal: "+pet['Animal'])
    print("Owner: "+pet['Owner']+"\n")
