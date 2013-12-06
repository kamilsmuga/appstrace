import requests
import re
from Db import Db
from bs4 import BeautifulSoup

class ManScrapper():
   
    url = None 
    name = None 
    body = None
    header = None

    def __init__(self, url):
        ManScrapper.url = url
        r = self.get_man_page()
        self.get_name(r)
        self.set_body_and_header(r)

    def get_man_page(self):
        return requests.get(ManScrapper.url)

    def get_name(self, request):
        soup = BeautifulSoup(request.text)
        m = re.search('.*?\(', soup.pre.string)
        ManScrapper.name = m.group(0).replace('(','')

    def set_body_and_header(self, request):
        self.body = request.text
        self.header = request.headers
    
    def save(self):
        db_obj = Db()
        db_obj.save_raw(self)

a = ManScrapper("http://man7.org/linux/man-pages/man2/clock_nanosleep.2.html")
print a.name
print a.url
a.save()
