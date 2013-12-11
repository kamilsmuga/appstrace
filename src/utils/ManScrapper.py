import requests
from Db import Db
from lxml import etree
from lxml.html import fromstring
import urllib2
import re

class ManScrapper():
   
    url = None 
    name = None 
    body = None
    header = None

    def __init__(self, url):
        ManScrapper.url = url
        print '*** url: %s' % url
        r = self.get_man_page()
        print '*** man page downloaded '
        self.get_name_from_url()
        self.set_body_and_header(r)

    def get_man_page(self):
        return requests.get(ManScrapper.url)

    def get_name_from_url(self):
        self.name = self.url.rsplit('/',1)[1].replace('.2.html','')

    def set_body_and_header(self, request):
        self.body = request.text
        self.header = request.headers
    
    def save(self):
        db_obj = Db()
        db_obj.save_raw(self)

