#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json
import os
import sys

from PyQt5.QtWidgets import QApplication, QWidget
from slackclient import SlackClient


def main():
    print('hello')
    token = os.environ['SLACK_API_TOKEN']
    sc = SlackClient(token)

    response = sc.api_call("channels.list",
                           exclude_archived=1)

    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
