countryMap = {
    "Australia": "Canberra",
    "Argentina": "Buenos Aires",
    "Sweden": "Stockholm",
    "England": "London",
    "France": "Paris",
    "Denmark": "Copenhagen",
    "USA": "Washington DC"
}

# Prints the value of the key
print(countryMap["Sweden"])     # output = "Stockholm"
print(countryMap["Argentina"])  # output = "Buenos Aires"
print(countryMap["France"])     # output = "Paris"
print(countryMap["USA"])        # output = "Washington DC"

for x in countryMap.items():
    print(x[0], x[1])
