def book_list_view(library):
    if not library:
        print("В библиотеке нет книг.")
    else:
        print("Список книг в библиотеке:")
        for title in library:
            print(title)

def add_book(library, title, author, year):
    if not validate_not_empty_field(title, "название книги") or \
        not validate_not_empty_field(author, "автор книги") or not validate_year_is_a_number(year):
        print("Заполните все поля корректно.")
        return
    if is_book_in_library(library, title):
        refresh_book_information(library, title, author, year)
    else:
        library[title] = {
            "автор" : author,
            "год издания" : year,
            "наличие" : True
        }
        print(f"Книга '{title}' успешно добалена")


def refresh_book_information(library, title, author, year):
    user_input = input(f"Книга '{title}' уже есть в библиотеке.\nЖелаете обновить информацию о книге? (да\нет)").lower()
    if user_input == "да":
        if not validate_not_empty_field(title, "название книги") or \
            not validate_not_empty_field(author, "автор книги") or not validate_year_is_a_number(year):
            print("Заполните все поля корректно.")
            return
        library[title]["автор"] = author
        library[title]["год издания"] = year
        print(f"Информация о книге '{title}' изменена.")
    else:
        print(f"Информация о книге '{title}' не изменена.")


def remove_book(library, title):
    if not is_book_in_library(library, title):
        return
    del library[title]
    print(f"Книга '{title}' удалена из библиотеки")


def issue_book(library, title):
    if not is_book_in_library(library, title):
        return
    if library[title]["наличие"]:
        library[title]["наличие"] = False
        print(f"Книга '{title}' выдана")
    else:
        print(f"Книга '{title}' уже взята")


def return_book(library, title):
    if not is_book_in_library(library, title):
        return
    if library[title]["наличие"]:
        library[title]["наличие"] = True
        print(f"Книга '{title}' возвращена в библиотеку")
    else:
        print(f"Книга '{title}' уже находится в библиотеке")


def find_book(library, title):
    if not is_book_in_library(library, title):
        return
    if library[title]["наличие"]:
        status = "Книга доступна"
    else:
        status = "Книга выдана"
    print(f"Информация о книге '{title}':\n"
          f"Автор: {library[title]['автор']}\n"
          f"Год издания: {library[title]['год издания']}\n"
          f"Статус: {status}")


def is_book_in_library(library, title):
    if title in library:
        return True
    else:
        print(f"Книга '{title}' не найдена в библиотеке")
        return False


def validate_not_empty_field(field_value, field_name):
    if not field_value:
        print(f"Ошибка: {field_name} не может быть пустым")
        return False
    return True


def validate_year_is_a_number(year_input):
    try:
        year = int(year_input)
        return year
    except ValueError:
        print("Ошибка: год должен быть целым числом.\n")
        return None


library = {
    "Мастер и Маргарита" : {
        "автор" : "Михаил Булгаков",
        "год издания" : 1940,
        "наличие" : True
    },
    "Евгений Онегин" : {
        "автор" : "Александр Пушкин",
        "год издания" : 1830,
        "наличие" : False
    },
    "Герой нашего времени": {
        "автор": "Михаил Лермонтов",
        "год издания": 1840,
        "наличие": True
    },
    "Анна Каренина": {
        "автор": "Лев Николаевич Толстой",
        "год издания": 1873,
        "наличие": False
    },
    "Преступление и наказание": {
        "автор": "Федор Достоевский",
        "год издания": 1866,
        "наличие": True
    }
}

user_actions = {
    "1": lambda: book_list_view(library),
    "2": lambda: add_book(library, input("Название: "), input("Автор: "), input("Год издания: ")),
    "3": lambda: remove_book(library, input("Удаление книги.\nВведите название книги, которую нужно удалить: ")),
    "4": lambda: issue_book(library, input("Выдача книги.\nВведите название книги, которую нужно выдать: ")),
    "5": lambda: return_book(library, input("Возврат книги.\nВведите название книги, которую нужно вернуть: ")),
    "6": lambda: find_book(library, input("Поиск книги.\nВведите название книги, которую хотите найти: ")),
    "0": lambda: print("Выход из программы.")
}

while True:
    user_input = input("Меню:\n1. Показать список книг.\n2. Добавить книгу.\n3. Удалить книгу.\n"
          "4. Выдать книгу.\n5. Вернуть книгу.\n6. Найти книгу.\n0. Выход.\n"
          "Введите номер нужного действия: ")
    user_action = user_actions.get(user_input)
    if user_action:
        if user_input == "0":
            user_action()
            break
        else:
            user_action()
    else:
        print("Некорректный ввод.")