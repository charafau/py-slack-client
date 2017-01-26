from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget

from app.gui.chat_window import Ui_chatWidget
from app.widgets.channel_windget import ChannelWidget


class ChatWindow(QWidget, Ui_chatWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)
        channelWidget = ChannelWidget()
        self.channelListLayout.addWidget(channelWidget)

