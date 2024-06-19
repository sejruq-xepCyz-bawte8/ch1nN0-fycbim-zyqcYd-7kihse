from ..API.ReaderApi import api_today, api_work_data, api_work_html, api_author_data, api_author_html
from anvil_extras import non_blocking
from time import sleep
from anvil.js.window import jQuery as jQ
from anvil_extras.storage import indexed_db
import json

class ReaderClass:
    def __init__(self) -> None:
        self.store_registry = indexed_db.create_store('registry')
        self.store_cache_html = indexed_db.create_store('cache_html')
        #self.store_cache_log = indexed_db.create_store('cache_log')
        self.data:dict = None
        self.html:str = None
        self.work_id:str = None
        self.author_uri = None
        self.author_id:str = None
        self.author_data:dict = None
        self.author_html:str = None
        self.cache = {}
        
        self.today = self.store_registry.get('today')
        if self.today == None : self.today = []
        self.today_update = non_blocking.defer(self.update_today, 3)
        
        self.works_data = self.store_registry.get('works_data')
        if self.works_data == None : self.works_data = {}

        self.works_html = self.store_registry.get('works_html')
        if self.works_html == None : self.works_html = {}

        self.authors_data = self.store_registry.get('authors_data')
        if self.authors_data == None : self.authors_data = {}

        self.authors_html = self.store_registry.get('authors_html')
        if self.authors_html == None : self.authors_html = {}


    def update_today(self):
        today_new = api_today()
        today_old = self.store_registry.get('today')
        self.update_changed_works(today_new=today_new, today_old=today_old)
        self.store_registry['today'] = today_new
        self.today = today_new
        icon_element = jQ('.fa-home')
        icon_element.toggleClass('fa-fade')
        sleep(5)
        icon_element.toggleClass('fa-fade')
        self.today_update = non_blocking.repeat(self.update_today, 1800)

    def set_current_work(self, work_id:str):
        self.work_id = work_id
        self.data = None
        self.html = None
        self.data = self.get_work_data(work_id)
        self.html = self.get_work_html(work_id)
        return True

    def set_current_author(self, author_id:str):
        self.author_id = author_id
        self.author_data = None
        self.author_html = None
        self.author_data = self.get_author_data(author_id)
        self.author_html = self.get_author_html(author_id)
        return True


    def get_work_data(self, wid:str):
        data = self.works_data.get(wid)
        if data:
            return data
        else:
            data = api_work_data(wid)
            self.works_data[wid] = data
            self.store_registry['works_data'] = self.works_data
            return data

    def get_work_html(self, wid:str):
        html = self.works_html.get(wid)
        if html:
            return html
        else:
            html = api_work_html(wid)
            self.works_html[wid] = html
            self.store_registry['works_html'] = self.works_html
            return html

    def get_author_data(self, author_id:str):
        data = self.authors_data.get(author_id)
        if data:
            return data
        else:
            data = api_author_data(author_id)
            self.authors_data[author_id] = data
            self.store_registry['authors_data'] = self.authors_data
            return data

    def get_author_html(self, author_id:str):
        html = self.authors_html.get(author_id)
        if html:
            return html
        else:
            html = api_author_html(author_id)
            self.authors_html[author_id] = html
            self.store_registry['authors_html'] = self.authors_html
            return html
        




    def update_changed_works(self, today_old, today_new):
        if today_old:
            # Convert lists to dictionaries
            old_works = {list(d.keys())[0]: list(d.values())[0]['version'] for d in today_old}
            new_works = {list(d.keys())[0]: list(d.values())[0]['version'] for d in today_new}

            # Check for newer versions
            newer_versions = {}
            for id, version in old_works.items():
                if id in new_works and new_works[id] > version:
                    newer_versions[id] = new_works[id]

            
            for key in newer_versions.keys():
                self.get_work_data(wid=key)
                if key in self.works_html:
                    self.get_work_html(wid=key)


