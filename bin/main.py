#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json
import os
import sys
import time

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from slackclient import SlackClient

from app.gui.main_window import Ui_MainWindow

token = os.environ['SLACK_API_TOKEN']


def print_response(response):
    print(json.dumps(response, sort_keys=True, indent=2,
                     separators=(',', ': ')))


class WatcherThread(QThread):
    # signal emitted when new message from Slack arrived
    new_message = pyqtSignal(dict)

    def __init__(self, parent=None):
        QThread.__init__(self, parent)

        self.slack_client = SlackClient(token)

    def run(self):
        if self.slack_client.rtm_connect():
            while True:
                for element in self.slack_client.rtm_read():
                    if element['type'] == 'message':
                        self.new_message.emit(element)

                time.sleep(1)

    # slot used for rending message into slack
    def send_message(self, message_text):
        self.slack_client.api_call('chat.postMessage',
                                   channel='#general', text=message_text)


def main():

    app = QApplication(sys.argv)

    # show main window
    w = MainWindow()
    w.show()

    # start watcher
    watcher_thread = WatcherThread()
    watcher_thread.start()

    # connect watcher thread with window
    watcher_thread.new_message.connect(w.print_message)
    w.new_message.connect(watcher_thread.send_message)

    sys.exit(app.exec_())


class MainWindow(QMainWindow, Ui_MainWindow):
    # signal emitted when new message is sent from window
    new_message = pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)

        self.setupUi(self)

        self.lineEdit.returnPressed.connect(self.send_message)

    # slot used to print incoming messages
    def print_message(self, message):
        self.chatWindow.append(message['text'])

    # slot used to handle [enter] key in line edit
    def send_message(self):
        text = self.lineEdit.text()
        self.new_message.emit(text)
        self.lineEdit.clear()


if __name__ == '__main__':
    main()
