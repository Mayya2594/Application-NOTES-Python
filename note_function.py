import json
import datetime

# Создание новой заметки
def create_note():
    note_id = input("Введите идентификатор заметки: ")
    note_title = input("Введите заголовок заметки: ")
    note_text = input("Введите текст заметки: ")
    note_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"id": note_id, "title": note_title, "text": note_text, "date": note_date}
