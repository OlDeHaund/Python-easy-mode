import random

with open('riigid_pealinnad.txt', 'r', encoding='utf-8') as file:
    countries_and_capitals = {}  # Словарь
    for line in file:
        country, capital = line.strip().split('-')  # Разделяем строку на страну и столицу
        countries_and_capitals[country] = capital  # Заполнение столиц


def get_capital_by_country():
    country = input("Введите название страны: ")  
    print(countries_and_capitals.get(country, "Эта страна не найдена."))  


def get_country_by_capital():
    capital = input("Введите название столицы: ")  
    for country, cap in countries_and_capitals.items():
        if cap == capital:  # Поиск
            print(country)
            return
    print("Этой столицы нет.")  # Если столица не найдена

# Новая страна/Столица
def add_new_entry():
    country = input("Введите название новой страны: ")  
    capital = input("Введите столицу этой страны: ")  
    countries_and_capitals[country] = capital  
    print(f"Страна {country} и столица {capital} добавлены были добавлены в список.")


def correct_entry():
    country = input("Введите страну, которую хотите поменять: ")  
    if country in countries_and_capitals:  
        new_capital = input(f"Введите правильную столицу для {country}: ") 
        countries_and_capitals[country] = new_capital  
        print(f"Столицу для {country} заменили на {new_capital}.")
    else:
        print(f"Страна {country} не была найдена.") 

# Test
def knowledge_test():
    correct_answers = 0
    total_questions = 3  

    for _ in range(total_questions):
        question_type = random.choice(['country', 'capital'])  

        if question_type == 'country':
            country = random.choice(list(countries_and_capitals.keys()))  
            answer = input(f"Какая столица у страны {country}? ")  
            if answer.lower() == countries_and_capitals[country].lower():  
                print("Ваш ответ верный!")
                correct_answers += 1
            else:
                print(f"Неправильно! Верный ответ: {countries_and_capitals[country]}")
        else:
            capital = random.choice(list(countries_and_capitals.values()))  
            answer = input(f"У какой страный столица - {capital}? ")  
            country = [k for k, v in countries_and_capitals.items() if v == capital][0]  
            if answer.lower() == country.lower():  # Проверяем ответ
                print("Ваш ответ верный!")
                correct_answers += 1
            else:
                print(f"Неправильно! Верный ответ: {country}")

    print(f"Вы ответили правильно на {correct_answers} из {total_questions} вопросов.")
    print(f"Ваш результат: {correct_answers * 100 / total_questions:.2f}%.") 


while True:
    print("\nВыберите опцию:")
    print("1 - Отобразить столицу по названию страны")
    print("2 - Отобразить страну по названию столицы")
    print("3 - Добавить новую пару страна-столица")
    print("4 - Исправить ошибку в словаре")
    print("5 - Проверить знания")
    print("0 - Выйти")

    choice = input("Ваш выбор: ")

    if choice == '1':
        get_capital_by_country()  # Столица по стране
    elif choice == '2':
        get_country_by_capital()  # Страна по столице 
    elif choice == '3':
        add_new_entry()  
    elif choice == '4':
        correct_entry()  
    elif choice == '5':
        knowledge_test()  # Тест
    elif choice == '0':
        break 
    else:
        print("Нет такого варианта")