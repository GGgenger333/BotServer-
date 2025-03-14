import sys

def search_phone_number(phone_number):
    # Ваш код для поиска номера
    # Пример:
    result = f"Результаты поиска для {phone_number}:\n"
    result += " ├Источник: HTMLWEB & Veriphone\n"
    result += " ├Телефонный код: +7\n"
    result += " ├Страна: Российская Федерация\n"
    result += " ├Округ: Уральский федеральный округ\n"
    result += " ├Регион: Тюменская область\n"
    result += " ├Город: Тюмень\n"
    result += " ├Широта: 57.1549\n"
    result += " ├Долгота: 65.5156\n"
    result += " ├Часовой пояс: +5 UTC\n"
    result += " ├Тип: mobile\n"
    result += " ├Оператор: ОАО \"Вымпел-Коммуникации\"\n"
    result += " ├Адрес:\n"
    result += " │├Улица: улица Чернышевского\n"
    result += " │├Номер дома: 15\n"
    result += " │├Район: Затюменка\n"
    result += " │├Почтовый индекс: 625001\n"
    result += " ├Источник: Одноклассники\n"
    result += " ├Привязанный номер: +79634509139\n"
    result += " ├Имя аккаунта: Роман Б*********\n"
    result += " ├Инфо профиля: 23 года\n"
    result += " ├Дата регистрации: Профиль создан 28 марта 2023"
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Пожалуйста, передайте номер для поиска.")
    else:
        phone_number = sys.argv[1]
        print(search_phone_number(phone_number))