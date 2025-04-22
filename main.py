def book_list_view(library):
    if not library:
        print("В библиотеке нет книг.")
    else:
        print("Список книг в библиотеке:")
        for title in library:
            print(title)

def add_book(library, title, author, year):
    if title in library:
        user_input = input(f"Книга '{title}' уже есть в библиотеке.\nЖелаете обновить информацию о книге? (да\нет)").lower()
        if user_input == "да":
            library[title]["автор"] = author
            library[title]["год издания"] = year
            print(f"Информация о книге '{title}' изменена.")
        else:
            print(f"Информация о книге '{title}' не изменена.")
    else:
        library[title] = {
            "автор" : author,
            "год издания" : year,
            "наличие" : None
        }
        print(f"Книга '{title}' успешно добалена")


def remove_book(library, title):
    if title in library:
        del library[title]
        print(f"Книга '{title}' удалена из библиотеки.")
    else:
        print(f"Книга '{title}' не найдена в библиотеке")


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

book_list_view(library)
add_book(library, "Отцы и дети", "Иван Тургенев", 1862)
add_book(library, "Анна Каренина", "Лев Толстой", 1873)
remove_book(library, "Герой нашего времени")
remove_book(library, "Не существующая книга")
book_list_view(library)