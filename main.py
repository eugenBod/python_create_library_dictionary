def book_list_view(library):
    if not library:
        print("В библиотеке нет книг.")
    else:
        print("Список книг в библиотеке:")
        for title in library:
            print(title)

def add_book(library, title, author, year):
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
        library[title]["автор"] = author
        library[title]["год издания"] = year
        print(f"Информация о книге '{title}' изменена.")
    else:
        print(f"Информация о книге '{title}' не изменена.")


def remove_book(library, title):
    if is_book_in_library(library, title):
        del library[title]
        print(f"Книга '{title}' удалена из библиотеки")
    else:
        print(f"Книга '{title}' не найдена в библиотеке")


def issue_book(library, title):
    if is_book_in_library(library, title):
        if library[title]["наличие"]:
            library[title]["наличие"] = False
            print(f"Книга '{title}' выдана")
        else:
            print(f"Книга '{title}' уже взята")
    else:
        print(f"Книга '{title}' не найдена в библиотеке")


def return_book(library, title):
    if is_book_in_library(library, title):
        if not library[title]["наличие"]:
            library[title]["наличие"] = True
            print(f"Книга '{title}' возвращена в библиотеку")
        else:
            print(f"Книга '{title}' уже находится в библиотеке")
    else:
        print(f"Книга '{title}' не найдена в библиотеке")


def find_book(library, title):
    if is_book_in_library(library, title):
        if library[title]["наличие"]:
            status = "Книга доступна"
        else:
            status = "Книга выдана"
        print(f"Информация о книге '{title}':\n"
              f"Автор: {library[title]['автор']}\n"
              f"Год издания: {library[title]['год издания']}\n"
              f"Статус: {status}")
    else:
        print(f"Книга '{title}' не найдена в библиотеке")


def is_book_in_library(library, title):
    return title in library


def validate_not_empty_field(field_value, field_name):
    if not field_value:
        print(f"Ошибка: {field_name} не может быть пустым")
        return False
    return True


def validate_year(year_input):
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

while True:
    user_input = input("Меню:\n1. Показать список книг.\n2. Добавить книгу.\n3. Удалить книгу.\n"
          "4. Выдать книгу.\n5. Вернуть книгу.\n6. Найти книгу.\n0. Выход.\n"
          "Введите номер нужного действия: ")
    if user_input == "1":
        book_list_view(library)
    elif user_input == "2":
        print("Добавление новой книги:")
        title = input("Введите название книги: ").strip()
        if not validate_not_empty_field(title, "название книги"):
            continue

        author = input("Введите автора книги:").strip()
        if not validate_not_empty_field(author, "автор книги"):
            continue

        year_input = input("Введите год издания книги: ")
        year = validate_year(year_input)
        if year is None:
            continue

        add_book(library, title, author, year)
    elif user_input == "3":
        title = input("Удаление книги.\nВведите название книги, которую нужно удалить: ")
        remove_book(library, title)
    elif user_input == "4":
        title = input("Выдача книги.\nВведите название книги, которую нужно выдать: ")
        issue_book(library, title)
    elif user_input == "5":
        title = input("Возврат книги.\nВведите название книги, которую нужно вернуть: ")
        return_book(library, title)
    elif user_input == "6":
        title = input("Поиск книги.\nВведите название книги, которую хотите найти: ")
        find_book(library, title)
    elif user_input == "0":
        print("Выход из программы.")
        break
    else:
        print("Некорректный ввод.")