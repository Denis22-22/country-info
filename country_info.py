import json

# Зчитування даних з JSON-файлу
with open("countries.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Запит назви країни від користувача
country_name = input("Введіть назву країни: ")

# Пошук країни за назвою у JSON-даних
for country in data:
    if country["name"] == country_name:
        # Отримання необхідної інформації
        country_name = country["name"]
        capital_name = country["capital"]
        region_name = country["region"]

        # Виведення отриманої інформації
        print("Назва країни:", country_name)
        print("Назва столиці:", capital_name)
        print("Назва регіону:", region_name)
        break
else:
    print("Країна не знайдена.")

