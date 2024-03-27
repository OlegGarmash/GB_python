class NoteView:
    def display_menu(self):
        print("\nВыберете пункт меню:\n"
              + "1. Добавить заметку\n"
              + "2. Показать все заметки\n"
              + "3. Редактировать заметку\n"
              + "4. Удалить заметку\n"
              + "5. Фильтр заметок по дате\n"
              + "6. Отобразить заметку\n"
              + "0. Выход\n")

    def get_input(self, message):
        return input(message)
