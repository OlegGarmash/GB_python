from controller import AppRunner
from model import NoteModel
from view import NoteView

if __name__ == '__main__':
    model = NoteModel()
    view = NoteView()
    controller = AppRunner(model, view)
    controller.run()