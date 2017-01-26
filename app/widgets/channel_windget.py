from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget

from app.gui.channel_list_widget import Ui_ChannelListWidget
from app.viewmodel.channel_viewmodel import ChannelViewModel


class ChannelWidget(QWidget, Ui_ChannelListWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)

        vm = ChannelViewModel()
        ds = vm.fetchChannels()
        x = ds.subscribe(lambda val: [self.channelList.addItem(item['name']) for item in val])
