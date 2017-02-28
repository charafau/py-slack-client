from PyQt5.QtWidgets import QWidget

from app.gui.chat_window import Ui_chatWidget
from app.widgets.channel_windget import ChannelWidget
from app.widgets.message_widget import MessageWidget


class ChatWindow(QWidget, Ui_chatWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)
        channel_widget = ChannelWidget()
        self.channelListLayout.addWidget(channel_widget)
        channel_widget.get_click_observable().subscribe(lambda value: print("Received {0}".format(value)))
        message_widget = MessageWidget()
        self.layout_message.addWidget(message_widget)






