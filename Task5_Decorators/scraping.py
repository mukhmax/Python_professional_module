from fake_headers import Headers
from requests import get
from bs4 import BeautifulSoup
from main import logger

KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'максимум']
base_URL = 'http://habr.com'
URL = base_URL + '/ru/all/'
headers = Headers(os="win", headers=True).generate()


def articles_search(word_list):
    request = get(URL, headers=headers).text
    soup = BeautifulSoup(request, 'html.parser')
    articles = soup.find_all('article')
    for article in articles:
        link_ = base_URL + article.find('h2').find('a').attrs['href']
        request_full_article = get(link_, headers=headers).text
        soup_full_article = BeautifulSoup(request_full_article, 'html.parser')
        full_article = soup_full_article.find(class_='tm-article-presenter__body').text
        for word in word_list:
            if word.lower() in full_article.lower():
                time_ = article.find('time').attrs['datetime'].split('T')[0]
                header_ = article.find('h2').find('span').text
                print(time_ + ' - ' + header_ + ' - ' + link_)
                break


if __name__ == "__main__":
    articles_search = logger(articles_search, log_path='/home/mukhmax/Documents/Netology/')
    articles_search(KEYWORDS)
