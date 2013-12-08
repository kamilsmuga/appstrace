from bs4 import BeautifulSoup
from ManScrapper import ManScrapper
from urlparse import urljoin
import time

class ManScrapThemAll():

    """ Class that commands to scrap all man pages for syscalls """
    """ Designed to be run periodically - only when update for this core data is
needed """
   
    url = 'http://man7.org/linux/man-pages/fake/fake'
    urls = []

    def __init__(self):
        self.get_urls()
        self.open_urls_and_store_data()

    def get_urls(self):
        # will start from syscalls man page and go through all links available there
        m = ManScrapper(urljoin(self.url, '../man2/syscalls.2.html'))
        soup = BeautifulSoup(m.body)
        urls = soup.find_all('a')

        for s in urls:
            try: 
                if (s['href'].startswith('..')): 
                    url = urljoin(self.url, s['href'])
                    self.urls.append(url)
            except KeyError:
                # don't care if we find a tag that is not a link
                continue
        
    def open_urls_and_store_data(self):
        for url in self.urls:
            entity = ManScrapper(url)
            entity.save()
            # let's be nice to man page server. 1 request per second
            time.sleep(1)

ManScrapThemAll()
