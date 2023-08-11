import json
import datetime

# Создание новой заметки
def create_note():
    note_id = input("Введите идентификатор заметки: ")
    note_title = input("Введите заголовок заметки: ")
    note_text = input("Введите текст заметки: ")
    note_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"id": note_id, "title": note_title, "text": note_text, "date": note_date}

# Сохранение заметки в файл
def save_note_to_file(note):
    with open("notes.json", "a") as file:
        file.write(json.dumps(note) + "\n")

# Чтение заметок из файла
def read_notes_from_file():
    notes = []
    with open("notes.json", "r") as file:
        for line in file:
            notes.append(json.loads(line))
    return notes

# Вывод списка всех заметок на экран
def print_notes(notes):
    for note in notes:
        print("Id: ", note["id"])
        print("Заголовок: ", note["title"])
        print("Дата/время: ", note["date"])
        print("Текст: ", note["text"])
        print("---------------")

