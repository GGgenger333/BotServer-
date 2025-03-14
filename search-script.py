import sys

def search_data(phone_number):
    # Здесь должна быть твоя логика поиска, сейчас просто заглушка
    return f"🔍 Найденные данные для {phone_number}:\n- Имя: Иван Иванов\n- Город: Москва"

if __name__ == "__main__":
    # Проверяем переданный пароль и номер
    if len(sys.argv) < 3 or sys.argv[1] != "алылыжта":
        print("Ошибка: Неверный пароль или недостаточно аргументов.")
        sys.exit(1)

    phone_number = sys.argv[2]
    print(search_data(phone_number))