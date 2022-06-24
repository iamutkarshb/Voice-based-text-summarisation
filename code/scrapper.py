from bs4 import BeautifulSoup
import requests as req

def get(topic):
    a=topic.split()
    tom="_".join(a)

    r=req.get("https://en.wikipedia.org/wiki/"+tom)
    soup = BeautifulSoup(r.content, 'html5lib')
    data = soup.find_all("p")

    feed = ""
    for i in data:
        feed=feed+i.text
    return feed 