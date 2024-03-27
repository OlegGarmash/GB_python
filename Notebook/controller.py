class AppRunner:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        self.model.load_notes()
        b = True
        while b:
            self.view.display_menu()
            a = self.view.get_input("-> ")
            if a == '1':
                title = self.view.get_input("Введите заголовок: ")
                body = self.view.get_input("Введите заметку: ")
                self.model.add_note(title, body)
            elif a == '2':
                self.model.list_notes()
            elif a == '3':
                note_id = int(self.view.get_input("Введите ID заметки: "))
                new_title = self.view.get_input("Введите новый заголовок: ")
                new_body = self.view.get_input("Введите новую заметку: ")
                self.model.add_note(note_id, new_title, new_body)
            elif a == '4':
                note_id = int(self.view.get_input("Введите ID заметки, которую хотите удалить: "))
                self.model.delete_note(note_id)
            elif a == '5':
                date = self.view.get_input("Введите дату в формате ГГГГ-ММ-ДД: ")
                self.model.filter_notes(date)
            elif a == '6':
                note_id = int(self.view.get_input("Введите ID заметки, которую хотите отобразить: "))
                self.model.read_note(note_id)
            elif a == '0':
                print("Работа с программой завершена.")
                b = False;
            else:
                print("Введено некоррктное значение. Попробуйтей снова.\n")
