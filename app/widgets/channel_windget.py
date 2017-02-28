from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

from app.gui.channel_list_widget import Ui_ChannelListWidget
from app.viewmodel.channel_viewmodel import ChannelViewModel
from rx.subjects import BehaviorSubject


class ChannelWidget(QWidget, Ui_ChannelListWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.subject = BehaviorSubject(-1)
        self.channels = []
        vm = ChannelViewModel()
        self.channelList.setAttribute(Qt.WA_MacShowFocusRect, 0)
        self.privateMessageList.setAttribute(Qt.WA_MacShowFocusRect, 0)
        ds = vm.fetchChannels()
        x = ds.subscribe(lambda val: [self.add_channel(item) for item in val])
        self.channelList.selectionModel().currentChanged.connect(self.on_row_changed)

    def add_channel(self, item):
        self.channels.append(item)
        self.channelList.addItem(item['name'])

    def on_row_changed(self, current, previous):
        print('Row %d selected' % current.row())
        self.subject.on_next(self.channels[current.row()])

    def get_click_observable(self):
        return self.subject
