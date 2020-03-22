#!/usr/bin/env python3

import datetime
import feedparser
import webbrowser

data = feedparser.parse('https://www.nhk.or.jp/r-news/podcast/nhkradionews.xml')
url = data['entries'][0]['links'][0]['href']
print(datetime.datetime.now(), url)
webbrowser.open(url)
