import requests
from bs4 import BeautifulSoup

liverpool = requests.get('http://www.liverpoolfc.com/news/first-team')
man_city  = requests.get('https://www.mancity.com/news/first-team')
man_utd   = requests.get('http://www.manutd.com/en/News-And-Features/Club-News.aspx')
tottenham = requests.get('http://www.tottenhamhotspur.com/news/')

liverpool_news = BeautifulSoup(liverpool.text, 'html.parser')
liverpool_news_summaries = liverpool_news.find_all(class_=['post-synopsis', 'synopsis'])
print(liverpool_news_summaries)

man_city_news = BeautifulSoup(man_city.text, 'html.parser')
man_city_articles = man_city_news.find_all(class_='article--preview-body')
for h in man_city_articles:
    print(h.find_next('h2'))
    
