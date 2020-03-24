#!/usr/bin/env python3

import datetime
import feedparser
import vlc
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel

data = feedparser.parse('https://www.nhk.or.jp/r-news/podcast/nhkradionews.xml')
url = data['entries'][0]['links'][0]['href']
print(datetime.datetime.now(), url)
player = vlc.MediaPlayer(url)
player.play()

app = QApplication(sys.argv)
widget = QWidget()
widget.resize(250, 150)
widget.move(300, 300)
widget.setWindowTitle('NHKラジオ')

layout = QHBoxLayout(widget)
widget.setLayout(layout)

label = QLabel('NHKランジオ')
label.setAlignment(Qt.AlignCenter)
layout.addWidget(label)

widget.show()

sys.exit(app.exec_())
