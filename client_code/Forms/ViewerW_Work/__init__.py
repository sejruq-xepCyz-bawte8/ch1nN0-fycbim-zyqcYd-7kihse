from anvil import *
from .._FormTemplate import _FormTemplate
import anvil.js
from anvil.js.window import document
from time import time
from ...Index.App import READER

class ViewerW_Work(_FormTemplate):
  def __init__(self, **properties):
    super().__init__(**properties)
    
    self.init_components(**properties)
 

    
    #SOURCE 
    self.source = document.createElement("div")
    self.source.innerHTML = READER.html
   
    #self.goStart = self.add_button()
    #self.goStart.page = "1"
    #self.goStart.add_event_handler('click', self.scrollTo)
    #self.goEnd = self.add_button()
    #self.goEnd.add_event_handler('click', self.scrollTo)


    

  def show_form(self, **event):
    #READER CONTAINER 
    self.add_div(id="cheteme_reader")
    self.reader =  document.getElementById("cheteme_reader")
    self.reader.setAttribute('onscroll', 'anvil.call($("#appGoesHere > div"), "scroll_reader", $(this))')
    self.targetHeigth = self.reader.offsetHeight

    #LABELS self.pagesLabel = self.add_label() #"#navl-ViewerW-ViewerW_Work"
    self.work_link = document.getElementById('navl-ViewerW-ViewerW_Work')
    self.pagesLabel = self.work_link.querySelectorAll('.ch-nav-text')[0]

    #self.add_label(text=self.form_name)
    self.last_scroll = time()
    self.mostVisible = 1
    self.pages = []

    self.currentPage = None
    self.currentParagraph = None
    self.pageNumber = 0
    self.headingsCount = 0
#self.add_event_handler('show', self.createNewPage) 
#self.targetHeigth = self.reader.offsetHeight
        
    #START PAGINATION
    self.distribute()


    
  def distribute(self):
        self.reader.innerHTML = ''
        self.last_scroll = time()
        self.pages = []
        self.currentPage = None
        self.currentParagraph = None
        self.pageNumber = 0
        #self.add_event_handler('show', self.createNewPage)


        self.createNewPage()
        for element in self.source.childNodes:
            if 'tagName' in element:
                if element.tagName.lower() == 'p':
                    words = element.innerHTML.split(' ')
                    self.createNewParagraph(element)
                    for word in words:
                        wordSpan = document.createElement('span')
                        wordSpan.innerHTML = word
                        self.currentParagraph.appendChild(wordSpan)
                        if self.currentPage.offsetHeight > self.targetHeigth:
                            self.currentParagraph.removeChild(wordSpan)
                            self.createNewPage()
                            self.createNewParagraph(element)
                            self.currentParagraph.appendChild(wordSpan)
                
                elif element.tagName.lower() == 'h1' and self.headingsCount > 0:
                    self.headingsCount += 1
                    self.createNewPage()
                    clone = element.cloneNode('true')
                    self.currentPage.appendChild(clone)
                
                
                else:
                    if element.tagName.lower() == 'h1' : self.headingsCount += 1
                    clone = element.cloneNode('true')
                    self.currentPage.appendChild(clone)
                    if self.currentPage.offsetHeight > self.targetHeigth:
                        self.currentPage.removeChild(clone)
                        self.createNewPage()
                        self.currentPage.appendChild(clone)
  
  def createNewPage(self):
        
        self.pageNumber += 1
        page = document.createElement('div')
        page.className = 'page'
        page.id = self.pageNumber
        self.currentPage = page
        self.pages.append(page)
        self.reader.appendChild(self.currentPage)
        self.pagesLabel.textContent = f"1/{self.pageNumber}"
        #self.goEnd.page = f"{self.pageNumber}"

  def createNewParagraph(self, sourceElement):
        self.currentParagraph = document.createElement('p')
        styleAttribute = sourceElement.getAttribute('style')
        if styleAttribute:
            self.currentParagraph.setAttribute('style', styleAttribute)
        css_classes = sourceElement.classList
        self.currentParagraph.classList.add(*css_classes)
        self.currentPage.appendChild(self.currentParagraph)

  def parse_most_visible(self):
      pages = document.querySelectorAll('.page')
      for page in pages:
          rect = page.getBoundingClientRect()
          print(rect['y'])

  def scrollTo(self, **event):
        element = document.getElementById(event['sender'].page)
        if element:
            element.scrollIntoView({'behavior': 'smooth', 'block': 'start'})
            
  def scroll_reader(self, page, *event):
        self.parse_most_visible()
        self.mostVisible = page
        self.pagesLabel.textContent = f"{self.mostVisible}/{self.pageNumber}"

  def click_cover(self):
    print('clic_cover')

  def click_toc(self):
    print('clic_toc')

  def click_bookmark(self):
    print('clic_bookmark')

  def click_like(self):
    print('clic_like')





    
    




