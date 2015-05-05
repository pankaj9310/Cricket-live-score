import requests
import feedparser
import pynotify
from time import sleep

def sendmessage(title, message):

    pynotify.init("Test")

    notice = pynotify.Notification(title, message)

    notice.show()

    return

url = "http://static.cricinfo.com/rss/livescores.xml"
print url
d=feedparser.parse(url)
n=str(d).count("href")-2
for i in range(n):
    print i,d.entries[i].title
print "Give index of match"
idx=int(input())
while True:

    r = requests.get(url)
    
    while r.status_code is not 200:

            r = requests.get(url)

    score = d.entries[idx].title
    sendmessage("Match Score", d.entries[idx].title)
    sleep(60)
