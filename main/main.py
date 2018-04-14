import requests
from bs4 import BeautifulSoup
class Scraper:
    
    @classmethod
    def run(cls):
        c = Scraper()
        c.liverpool_news()
        c.man_city_news()
        c.man_utd_news()
        c.tottenham_news()
        return c

    def liverpool_news(self):
        liverpool                = requests.get('http://www.liverpoolfc.com/news/first-team')
        liverpool_news           = BeautifulSoup(liverpool.text, 'html.parser')
        liverpool_news_articles  = liverpool_news.find_all(class_=['post-synopsis', 'synopsis'])
        for h in liverpool_news_articles:
            print(h)

    def man_city_news(self):
        man_city          = requests.get('https://www.mancity.com/news/first-team')
        man_city_news     = BeautifulSoup(man_city.text, 'html.parser')
        man_city_articles = man_city_news.find_all(class_='article--preview-body')
        for h in man_city_articles:
            print(h.find_next('h2'))

    def man_utd_news(self):
        man_utd          = requests.get('http://www.manutd.com/en/News-And-Features/Club-News.aspx')
        man_utd_news     = BeautifulSoup(man_utd.text, 'html.parser')
        man_utd_articles = man_utd_news.find_all(class_='storycontent')
        for h in man_utd_articles:
            print(h.find_next('strong'))

    def tottenham_news(self):
        tottenham          = requests.get('http://www.tottenhamhotspur.com/news/')
        tottenham_news     = BeautifulSoup(tottenham.text, 'html.parser')
        tottenham_articles = tottenham_news.find_all('h4')
        for h in tottenham_articles:
            print(h)

Scraper.run()