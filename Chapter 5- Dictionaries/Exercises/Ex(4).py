rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'mississippi': 'united states'
}
rivers = {
    "Nile":"Egypt",
    "Amazon":"Brazil",
    "Mississippi":"United states",
}

# print what the rivers runs through
for river, country in rivers.items():
    print("The "+river+" runs through "+country+".\n")

# print rivers name in dictionary
print("\nRivers:")
for river in rivers:
    print(river)

#prints the countries of the rivers
print("\nCountries:")
for country in rivers.values():
    print(country)
