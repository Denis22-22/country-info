import requests
import json

country = input("Введіть назву країни: ")

# Виконуємо HTTP-запит до API для отримання даних про країну
response = requests.get(f"https://restcountries.com/v3/name/{country}")

# Перевіряємо статус код запиту
if response.status_code == 200:
    # Отримуємо JSON-дані з відповіді
    data = json.loads(response.text)

    # Отримуємо назву столиці, назву країни та регіон з JSON-даних
    capital = data[0]["capital"]
    country_name = data[0]["name"]["common"]
    region = data[0]["region"]

    # Виводимо дані в консоль
    print("Назва країни:", country_name)
    print("Столиця:", capital)
    print("Регіон:", region)
else:
    print("Країну не знайдено.")

