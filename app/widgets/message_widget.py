from PyQt5.QtWidgets import QWidget

from app.gui.message_widget import Ui_MessageWidget


class MessageWidget(QWidget, Ui_MessageWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)

    def select(self, channel):
        pass

