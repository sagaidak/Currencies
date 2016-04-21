import urllib
from bs4 import BeautifulSoup

BASE_URL = 'http://korrespondent.net/'
BASE_URL2 = 'http://finance.i.ua/'


def get_html(url):
    response = urllib.urlopen(url)
    return response.read()


def korrespondent(html):
    soup = BeautifulSoup(html, 'html.parser')
    ul = soup.find('ul', {'class': 'dropdown-menu'})

    col = ul.find_all('b')

    usd = 'USD: ' + col[0].text.strip()
    eur = 'EUR: ' + col[1].text.strip()
    rub = 'RUB: ' + col[2].text.strip()
    return usd, eur, rub


def parse_i_ua(html):
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.find('table', {'class': 'local_table nbu_rate'})

    col = div.find_all('td')

    usd = 'USD: ' + col[2].text
    eur = 'EUR: ' + col[5].text
    rub = 'RUB: ' + col[8].text
    return usd, eur, rub


def main():
    site = raw_input('Enter site: 1 - korrespondent.net, 2 - finance.i.ua: ')
    if site == '1':
        url = BASE_URL
        print url
        get_html(url)
        curr = korrespondent(get_html(url))
        print curr
    elif site == '2':
        url = BASE_URL2
        print url
        get_html(url)
        curr = parse_i_ua(get_html(url))
        print curr
    else:
        print 'error'


if __name__ == '__main__':
    main()
