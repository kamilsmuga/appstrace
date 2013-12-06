import os
from pymongo import MongoClient

class Db():

    client = None
    db_inst = None

    def __init__(self):
        self.openConnection()

    def openConnection(self):
        self.client = MongoClient(os.environ["MONGO_HOST"], int(os.environ["MONGO_PORT"]))
        self.db_inst = self.client.appstrace_db
    
    def save_raw(self, raw_scrap):
        collection = self.db_inst.man_raw
        entity = { "name": raw_scrap.name,
                   "url": raw_scrap.url,
                   "body": raw_scrap.body }
                   # "header": raw_scrap.header }
        entity_id = collection.insert(entity)
        print entity_id
