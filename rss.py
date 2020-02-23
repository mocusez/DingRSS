
# encoding: utf-8
import requests
import codecs
import feedparser
import pickle
from dingtalkchatbot.chatbot import DingtalkChatbot
import os
path = os.getcwd()

def fet():
	global url
	url = 'https://www.ithome.com/rss/'
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36'}
	page = requests.get(url, headers=headers)
	page.encoding = 'utf-8'
	page_content = page.text
	f = codecs.open('new_rss.txt', 'w', 'utf-8')
	f.write(page_content)
	f.close()

def ana():
	global new
	global titl
	global old
	global link
	rss = feedparser.parse('new_rss.txt')
	#print(rss.feed.image.href)
	new = rss.entries[0].summary
	titl = rss.feed.title
	link = rss.entries[0].id
	filename = path + '/summary.txt'
	print(filename)
	if os.path.exists(filename):
		old = pickle.load(open('summary.txt', 'rb'))
	else:
		pickle.dump(new,open('summary.txt', 'wb') )
		old=''
	titl.encode('utf-8').decode('unicode-escape')
	new.encode('utf-8').decode('unicode-escape')
	link.encode('utf-8').decode('unicode-escape')

def sen():
	if  new != old:
		webhook = ''
		xiaoding = DingtalkChatbot(webhook)
		xiaoding.send_markdown(
		title='News', text='### '+titl+'\n'
		'ITNews:'+new+'\n\n'
		'Link:'+link
		)
		pickle.dump(new,open('summary.txt', 'wb') )
	else:
		print('Nothing')
	

fet()
ana()
sen()
