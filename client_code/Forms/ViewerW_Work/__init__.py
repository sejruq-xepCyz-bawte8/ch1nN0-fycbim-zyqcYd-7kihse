from anvil import *
from .._FormTemplate import _FormTemplate
import anvil.js
from anvil.js.window import document
from time import time, sleep

class ViewerW_Work(_FormTemplate):
  def __init__(self, **properties):
    super().__init__(**properties)
    
    self.init_components(**properties)
 
    #self.pagesLabel = self.add_label() #"#navl-ViewerW-ViewerW_Work"
    self.work_link = document.getElementById('navl-ViewerW-ViewerW_Work')
    self.pagesLabel = self.work_link.querySelectorAll('.ch-nav-text')[0]


    #self.goStart = self.add_button()
    #self.goStart.page = "1"
    #self.goStart.add_event_handler('click', self.scrollTo)
    #self.goEnd = self.add_button()
    #self.goEnd.add_event_handler('click', self.scrollTo)
    

  def show_form(self, **event):

    #self.add_label(text=self.form_name)
    self.last_scroll = time()
    self.mostVisible = 1
    self.pages = []
    self.add_div(id="cheteme_reader")
    self.reader =  document.getElementById("cheteme_reader")
    self.source = document.createElement("div")
    self.targetHeigth = self.reader.offsetHeight
        
    self.source.innerHTML = html
        
    self.currentPage = None
    self.currentParagraph = None
    self.pageNumber = 0
        #self.add_event_handler('show', self.createNewPage)
        
    self.distribute()
        # Any code you write here will run before the form opens.

    
  def distribute(self):
        self.reader.innerHTML = ''
        self.last_scroll = time()
        
        self.pages = []
        self.reader =  document.getElementById("cheteme_reader")
        self.source = document.createElement("div")
        self.targetHeigth = self.reader.offsetHeight
        
        self.source.innerHTML = html
        
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
                else:
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
        
        self.currentPage.appendChild(self.currentParagraph)



  def scrollTo(self, **event):
        element = document.getElementById(event['sender'].page)
        if element:
            element.scrollIntoView({'behavior': 'smooth', 'block': 'start'})
            
  def scroll_reader(self, page, *event):
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





html = """<h1>Последният ден на XX век</h1>
<img width="200" src="https://upload.wikimedia.org/wikipedia/commons/c/c7/Ivan_Vazov_Coloured_Improved.jpg">
<p>Младият още цар Иван беше се поправил вече от своята простуда, която го бе задържала няколко дена в двореца. Днес се усещаше бодър и добре. Зимният ден беше особено мек, без слънце и заоблачен, но топъл. Царят отвори за малко прозореца, за да поеме чист въздух отвън. Той гълташе с удоволствие живителните му струи и погледът му бягаше през големите ясени и акации на Градската градина по пространната столица, с покриви, побелели от сняг, отдето се дигаха в небето безбройни кули и високи сводове на дворци и държавни учреждения и кръстове от черкови. Най-близо се издигаше монументалната сграда на Народния театър.</p>
<p>На вратата на кабинета се почука почтително. Царят се издигна. Адютантът му, генерал Шанов, влезна и съобщи:</p>
<p>— Ваше величество, охридския управител пита ще ли благоволите да го приемете? Също и другите.</p>
<p>— Ах, добре, нека влезе в приемний салон. Поради болестта си аз ги заставих да чакат няколко дена…</p>
<p>Царят затвори прозореца, облече си официалната дреха и се спря при писалищний стол, дето лежаха куп книжа, вестници и депеши, и взе да дочита нещо. Зад него, сериозен, гледаше из голямата си златна рамка внушителния образ на цар Фердинанда I. По стените на кабинета, облечени с великолепни цветни пиротски килими, висяха други големи портрети, тоже в златни кръжила на членове от фамилията, работа на знаменити български живописци. Между образите особено жив стоеше образа на баща му, Бориса I, със своето изразително, но благо, белобрадо лице, озарено от умни сини очи. Царят остави депешата и се приближи до апарата на стената (фоноскопа), натисна нещо и той издрънка. След една минута апарата сам издрънка. Царят тогава си приближи устата до тръбата, а с очите, като гледаше в едно стъкло над нея, извика:</p>
<p>— А, Константине, добър ден!</p>
<p>От апарата излезе ясен глас:</p>
<p>— Добър ден, тате. Не те питам поправи ли се; виждам по лицето ти, че си бодър сега. Какво има да ми заповядаш?</p>
<p>Царят отговори:</p>
<p>— Добре съм. Напусни Одрин и ела тая вечер да изпратим заедно векът. Имаш на разположение цели два часа. Трябва да ми доложиш лично за въпроса… Аз мисля обаче, че мъчнотиите са изгладени…</p>
<p>— Да, изгладиха се щастливо. Но аз се обещах на великия княз Александра да бъда тая вечер в Цариград.</p>
<p>— Защо?</p>
<p>— Покани ме и аз обещах да присъствувам заедно с него на бдението в „Света София“ и после на гощавката в Александровския дворец на Босфора.</p>
<p>— Тогава дръж си думата, синко. Поздрави великия княз и великата княгиня. Изпратете двадесетия век радостно, както и ний тука ще го изпратим. Той беше щастлив век за славянството.</p>
<p>След малко царят приемаше в салона охридския управител и изслушваше устния му доклад по произшествията, извикани на най-южната граница на България от албанските немирници, под воеводството на безпокойния Иренк Мивош.</p>
<p>Дадоха се после аудиенции на английския посланик, на новоназначения от Екзархията Нишки митрополит, бивший Сливенски архиепископ, на адмирала на българската флота, която се бе прибрала в Кавала, подир маневрите си по Бяло море заедно с руската; на сръбския посланик, който наскоро се бе завърнал от Рагуза, станала зимна резиденция на негово величество сръбския крал, който предпочиташе да живее в новите си далматински владения. Последния приет беше представителя на Испанската република.</p>
<p>Цар Иван се завърна в кабинета поуморен от тия приеми. Той бутна електрическия звънец и влезе дворцовия маршал.</p>
<p>— Славомире, моля, кажете да ми запретнат каляската; искам да се поразходя… Лекарят ми разреши. Приготовленията за тазвечерният прием, както и за бала, стават ли? Нека бъде бляскаво.</p>
<p>— Да, господарю.</p>
<p>— Какво прави царицата? Върна ли се?</p>
<p>— Върна се. Ходила е лично да раздава помощи на бедните.</p>
<p>— Прекрасно. По доброта, сърдечност и по благодат тя наумява баба ми… Попитай я желае ли да ме придружи.</p>
<p>И царят погледна към портрета на жена си, тип на истинска красива рускиня, изписана в носията, идеализирана, на кюстендилска селянка, обезателният дамски костюм при дворцовите тържества.</p>
<p>След малко адютантът яви, че царицата е поуморена и се извинява. Царят слезна долу. На дворцовата порта чакаше каляската с два черни жребеца, дар от султана, живущ сега в Коня. Но той, като видя колко е хубаво времето, отказа да се вози и тръгна пеш из разкошната с богати здания и къщи улица „Цар Освободител“. Непоследван от никой телохранител, облечен просто, царят отвръщаше усмихнато поздравите на минувачите. Той мина покрай остарялото, почерняло от времето здание на Военния клуб, мина край Народното събрание и величавий бронзов паметник на императора Александра II, дето се срещна и приказва няколко минути с прочутия по подвизите си във войната през 1972 г. генерал Шайханов, после мина из алеята на акациите, между два реда дворци, край величественото здание на университета и по-нататък — на сената и на министерството на мореплаването, срещайки се с върволяци граждани и гражданки, излезли също да се порадват на хубавия зимен ден. Той срещаше изражение на искрена любов и дълбока почит във всичките лица. Отвъд Орловия мост той се размина с малките князове, които яздеха на новоизобретения инструмент „флигт-вег“ (един вид велосипед, движен от каучукови крила). Царят се поумори, извърна се и даде знак на каляската, която го следеше отдалеко, качи се и потегли край столетната гора на Борисовия парк, обезлистен сега, покрит със сняг и пуст с мълчаливите си мраморни статуи на богини и дриади. Отляво хубавите трикатни здания, дворци и вили се простираха на два километра далеко. От висотата, дето се свърши парка, той хвърли поглед назад въз безкрайната с 350-хилядното си население столица, гърмяща като море, дето десетки високи фабрични комини изхвърляха черни стълпове пушек и замъгляваха атмосферата й. Няколко шопа из пътя, облечени чисто и спретнато, с лица здрави, умни и вчеловечени, както бяха всичките сега, привлякоха вниманието му и той приказва с тях за поминъка им и живота им; по обичая си, той правеше това, желающ лично да опознае нуждите на любимия си народ. Няколко време той се любува̀ на града, станал център на богатството, светлина и култура за обширното царство. На юг Витоша се белееше величествена и на гърба й, зад Резньовете, се забелязваше кубето на приоблачната гостилница „Кръгозор“, посещавана лете от туристи из цяла Европа, додето се отиваше от Драгалевци по зъбчеста железница. Силни чувства изпитваше царят сега. През ума му минаваха ред произшествия и велики преврати, ознаменували предидущите царствувания и неговото през XX век, а неговий поглед сякаш се впиваше в бъдещето, като да иска да види тайните, които то криеше в дълбокий си мрак…</p>
<p>Когато царят се завърна, беше вече късно. Той влезе в дворецът, цял блеснал от светлини, дето щеше тая вечер да се посреща радостно новия XXI век.</p>
<p>30 дек. 1899 год.</p>

"""
    
    




