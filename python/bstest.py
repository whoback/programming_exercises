# imports

from bs4 import BeautifulSoup
import urllib2
import requests
import csv
import time
# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

page_to_read = 'http://danjohn.net/category/blog'
headers = {'User-Agent': 'Mozilla/5.0'}

html_doc = requests.get(page_to_read, headers=headers)

soup = BeautifulSoup(html_doc.text, 'html.parser')

posts = soup.find_all('article', attrs={'class': 'post'})

# create loop to write content to csv
counter = 1
while (counter <= 10):
	for post in posts:
		# get article title
		h1 = post.find('h1', attrs={'class': 'entry-title'})
		title = h1.text.strip()
		# get article text
		content = post.find('div', attrs={'class': 'entry-content'})
		article = content.text.strip()
		post_line = [counter, title, article]
		with open('output.csv', 'a') as f:
			writer = csv.writer(f)
			writer.writerow(post_line)
		counter += 1

	older_posts_button = soup.find('div', attrs={'class': 'nav-previous'})
	older_posts_link = older_posts_button.find("a").attrs['href']
	time.sleep(2)
	new_page = requests.get(older_posts_link, headers=headers)
	soup = BeautifulSoup(new_page.text, 'html.parser')
