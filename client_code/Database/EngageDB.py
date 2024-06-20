from ..API.ReaderApi import api_today, api_work_data, api_work_html, api_author_data, api_author_html
from anvil_extras import non_blocking
from time import time
from anvil.js.window import jQuery as jQ
from anvil_extras.storage import indexed_db
import json

from ..Helpers import hash_strings
from ..API.EngagementApi import api_engagement
from ..Index import App


class EngageClass:
    def __init__(self) -> None:
        self.store_registry = indexed_db.create_store('registry')
        self.data:dict = None
        self.work_id:str = None
        self.author_uri = None
        self.author_id:str = None
        self.author_data:dict = None
        self.cache = {}
        
        
        self.engagements = self.store_registry.get('engagements')
        self.myengagements = self.store_registry.get('myengagements')
        self.myengagements = self.store_registry.get('myengagements')
        if self.engagements == None : self.works_data = {}


    def my_engage(self, wid, comment:str=None, engagement:list=None):
        
        result = api_engagement(wid=wid, engagement=engagement, comment=comment)
        print('engagement result', result)


