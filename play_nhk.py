#!/usr/bin/env python3

import atexit
import datetime
import feedparser
import os
import urllib.request
import vlc
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel

data = feedparser.parse('https://www.nhk.or.jp/r-news/podcast/nhkradionews.xml')
url = data['entries'][0]['links'][0]['href']
print(datetime.datetime.now(), url)

# Although vlc.MediaPlayer can play the url directly, the connection will be
# reset by peer possibly due to URL expiration. Therefore I have to download
# the mp3 file and play it locally. See:
# https://github.com/simon-weber/gmusicapi/issues/286#issuecomment-282594854
content = urllib.request.urlopen(url)
file_path = '/tmp/nhk.mp3'
with open(file_path, 'wb') as output:
    output.write(content.read())
    atexit.register(lambda: os.remove(file_path))

player = vlc.MediaPlayer(file_path)
player.play()

# Open a GUI window so that I can close the program conveniently.
# Otherwise it may be bothersome to close the program manually if
# the program is launched by cron.
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
