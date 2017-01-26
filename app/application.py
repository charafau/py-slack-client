import sys
from PyQt5.QtWidgets import QApplication
from app.widgets.chat_window import ChatWindow


class Application:
    def __init__(self):
        super().__init__()

    def start(self):
        print('starting application')

        app = QApplication(sys.argv)

        chatWindow = ChatWindow()
        chatWindow.show()

        sys.exit(app.exec_())
