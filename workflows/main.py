import sys
import webbrowser

from utils import Log

log = Log('main')


def open(url):
    webbrowser.open(url)
    log.info('Opening: ' + url)


def book(search_term):
    for prefix in [
        'https://www.vijithayapa.com/product/search?q=',
        'https://www.sarasavi.lk/serach-result?keyword=',
        'https://www.expo-graphic.com/search?keyword=',
        'https://jumpbooks.lk/?product_cat=&post_type=product&s=',
        'https://cgabooksonline.com/search'
        + '?controller=search&orderby=position&orderway=desc&search_query=',
        'https://bookyard.lk/?post_type=product&dgwt_wcas=1&s=',
        'https://samudrabooks.com/more_books_search?key=',
        'https://www.books.lk/?s=',
        'https://jeyabookcentre.com/search?key=',
        'https://www.pererahussein.com/books?search=',
        'https://www.amazon.com/s?i=stripbooks-intl-ship&k=',
    ]:
        url = prefix + search_term
        open(url)


def thesaurus(search_term):
    url = 'https://www.thesaurus.com/browse/' + search_term
    open(url)


def google_map(search_term):
    url = 'https://www.google.com/maps/search/' + search_term
    open(url)


def main(search_type, search_term):
    if search_type == 'book':
        book(search_term)
    elif search_type in ['thesaurus', 'the']:
        thesaurus(search_term)
    elif search_type in ['google_map', 'map', 'maps']:
        google_map(search_term)
    else:
        log.error('Invalid search type: ' + search_type)


if __name__ == '__main__':
    search_type = sys.argv[1]
    search_term = sys.argv[2]

    main(search_type, search_term)
