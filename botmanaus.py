import praw
import config
from bs4 import BeautifulSoup
import urllib
import re
import time

def bot_login():
    r = praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = "Noticias do Amazonas v.0.1")
    return r

def run_bot(r):
    link, title = g1_news()
    n = -1
    while n < 9 :
        n = n + 1
        try :
            print('POSTANDO')
            r.subreddit('manaus').submit(str(title[n]),url=link[n],resubmit=False,send_replies=False)
        except:
            print ('ERRO')
            n = n + 1
        print (n)
    time.sleep(21600)

def g1_news():
    html_page = urllib.request.urlopen("http://g1.globo.com/am/amazonas/")
    soup = BeautifulSoup(html_page, "html.parser")
    links = []
    titles = []
    for link in soup.findAll('a', attrs={'href': re.compile("^https://g1.globo.com/am/amazonas/noticia/"), }):
        links.append(link.get('href'))
    for link2 in soup.findAll('p', class_='feed-post-body-title'):
        titles.append(link2.string)
    return links, titles

r = bot_login()
while True: 
    run_bot(r)
    
