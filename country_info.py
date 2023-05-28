import json

country = input("Введіть назву країни: ")

with open("countries.json", "r") as file:
    countries_data = json.load(file)

found_country = None
for data in countries_data:
    if data["name"]["common"].lower() == country.lower():
        found_country = data
        break

if found_country:
    capital = found_country["capital"]
    country_name = found_country["name"]["common"]
    region = found_country["region"]

    print("Назва країни:", country_name)
    print("Столиця:", capital)
    print("Регіон:", region)
else:
    print("Країну не знайдено.")
