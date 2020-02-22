# -*- coding: cp936 -*-
# encoding: utf-8
import requests
import codecs
import feedparser
import pickle
from dingtalkchatbot.chatbot import DingtalkChatbot
import os
#https://pythonhosted.org/feedparser/
path = os.getcwd()

## Rss??
url = ''
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36'}
page = requests.get(url, headers=headers)
page.encoding = 'utf-8'
page_content = page.text
f = codecs.open('new_rss.txt', 'w', 'utf-8')
f.write(page_content)
f.close()

## Rss??
rss = feedparser.parse('new_rss.txt')

#print(rss.feed.image.href)
new = rss.entries[0].summary
titl = rss.feed.title
filename = path + '\summary.txt'
#print(filename)
if os.path.exists(filename):
       old = pickle.load(open('summary.txt', 'rb'))
else:
	pickle.dump(new,open('summary.txt', 'wb') )
	old=''

if  new != old:
	webhook = ''
	xiaoding = DingtalkChatbot(webhook)
	xiaoding.send_markdown(
	title='News', text='### \n'
	'News:'+new+'\n\n',
	is_at_all = True
	)
	pickle.dump(new,open('summary.txt', 'wb') )
else:
	print('Nothing')