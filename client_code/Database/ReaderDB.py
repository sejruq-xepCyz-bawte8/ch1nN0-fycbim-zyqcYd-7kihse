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
        self.today_update = non_blocking.defer(self.update_today, 0)
        
        self.works_data = self.store_registry.get('works_data')
        if self.works_data == None : self.works_data = {}

        self.works_html = self.store_registry.get('works_html')
        if self.works_html == None : self.works_html = {}

        self.authors_data = self.store_registry.get('authors_data')
        if self.authors_data == None : self.authors_data = {}

        self.authors_html = self.store_registry.get('authors_html')
        if self.authors_html == None : self.authors_html = {}


    def update_today(self):
        today = api_today()
        self.store_registry['today'] = today
        self.today = today
        icon_element = jQ('.fa-home')
        icon_element.toggleClass('fa-fade')
        sleep(3)
        icon_element.toggleClass('fa-fade')
        self.today_update = non_blocking.repeat(self.update_today, 600)

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
        







html_template = """<h1>Последният ден на XX век</h1>
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