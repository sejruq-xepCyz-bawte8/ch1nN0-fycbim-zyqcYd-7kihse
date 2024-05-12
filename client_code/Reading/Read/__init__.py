from ._anvil_designer import ReadTemplate
from anvil import *
import anvil.server
import anvil.js
from anvil.js.window import document
from time import time


class Read(ReadTemplate):
    def __init__(self, **properties):
        self.add_event_handler('show', self.form_show)
        self.goStart = Button(icon = "fa:chevron-left")
        self.goStart.page = "1"
        self.goStart.add_event_handler('click', self.scrollTo)
        self.goEnd = Button(icon = "fa:chevron-right")
        self.goEnd.add_event_handler('click', self.scrollTo)
        self.pagesLabel = Label(text=0)
        self.add_component(self.goStart, slot = 'reading_bar')
        self.add_component(self.pagesLabel, slot = 'reading_bar')
        self.add_component(self.goEnd, slot = 'reading_bar')
        self.init_components(**properties)
    def scrollTo(self, **event):
        element = document.getElementById(event['sender'].page)
        if element:
            element.scrollIntoView({'behavior': 'smooth', 'block': 'start'})

    def form_show(self, **event):
        # Set Form properties and Data Bindings.
        #self.reader = self.dom_nodes['cheteme_reader']
        self.last_scroll = time()
        self.mostVisible = 1
        self.pages = []
        self.reader =  document.getElementById("cheteme_reader")
        self.source = document.createElement("div")
        self.targetHeigth = self.reader.offsetHeight
        
        self.source.innerHTML = html
        self.reader.innerHTML = "hello"
        
        self.currentPage = None
        self.currentParagraph = None
        self.pageNumber = 0
        #self.add_event_handler('show', self.createNewPage)
        
        self.distribute()
        # Any code you write here will run before the form opens.
    def createNewPage(self):
        
        self.pageNumber += 1
        page = document.createElement('div')
        page.className = 'page'
        page.id = self.pageNumber
        self.currentPage = page
        self.pages.append(page)
        self.reader.appendChild(self.currentPage)
        self.pagesLabel.text = f"1/{self.pageNumber}"
        self.goEnd.page = f"{self.pageNumber}"

    def createNewParagraph(self, sourceElement):
        self.currentParagraph = document.createElement('p')
        styleAttribute = sourceElement.getAttribute('style')
        if styleAttribute:
            self.currentParagraph.setAttribute('style', styleAttribute)
        
        self.currentPage.appendChild(self.currentParagraph)
    
    def distribute(self):
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
                
    def scroll_reader(self, *event):
        self.mostVisible = 0
        for element in self.pages:
            self.mostVisible += 1
            rect = element.getBoundingClientRect()
            if rect.top >= 0 and rect.top <=100:
                break
                
                
        self.pagesLabel.text = f"{self.mostVisible}/{self.pageNumber}"
            
           


html = """<h1>Title of the Article</h1>

<p>
  Груби, силни ръце извиха неговите с пукане отзад и студена игла прониза врата
  му.
  <i>italic</i> <strong>string</strong>.
</p>
<p>
  Натрапчиво вибриране на телефон извади Емет от приятния сън, завладял го след
  гмуркането в океана. Загледа се в красивото тяло на жена си. Напрегнатият и
  безкраен разговор, на психоложката най-накрая завърши. Последният ден от
  едномесечната ваканция в Мексико, не беше изключение от уговорката, да работят
  докато почиват.
</p>
<img src="https://www.w3schools.com/html/img_chania.jpg" alt="Flowers in Chania" width="460" height="345">

<p>“Кали?” - погледна я той многозначително.</p>
<p>
  “Да. Представи си, само. Купила си е последния роман на Стивън Кинг. И още в
  края на първа глава отново я е връхлетяла старата фобия.”
</p>
<p>
  Замълчаха. Кракът му се зарови в топлия пясък и бавно се придвижи към нейния
  докато не я докосна по петата.
</p>
<p>“Пандора, мила, много съжалявам.”</p>
<p>
  Продължаващото ѝ мълчание издаваше причината за страданията на пациентката.
  Преди да публикува последната си статия в блога, тя го предупреди, че опасна
  за хора, като нейните пациенти. Замисли се - зад хилядите благодарствени
  коментари, колко ли хора опитали да погледнат страха в очите, за да го
  преодолеят сега се гърчат още по-ужасени. Но пък благодарение на него можеха
  да си позволят почивка като тази. А последната статия, о тя беше хит.
</p>
<p>
  “Емет! Само моля те не изпитвай сега вина. Не искам следващия ти текст да бъде
  за това.” - смехът и изпълни опустелия вече плаж.
</p>
<p>
  “Всъщност дори ми се роди една идея. С това ще ми се реваншираш. Искам да
  напишеш разказ, който да плаши всички без изключение. Ще го използвам в моята
  дисертация. Ще се справиш ли?”
</p>
<p>“Хорор?!?”</p>
<p>
  “О да. Искам … универсалния!” - присвитите и очи означаваха “не мога” не е
  правилния отговор.
</p>
<p>
  Известен писател, историите му създаваха в хората позитивна енергия и ги
  мотивираха към живота. Думите “универсален страх” обаче завладяха
  любопитството му въпреки, че не харесваше слъзливи или кървави сцени и
  текстове. Ако открие “отровата”, значи ще открие и “антидота”.
</p>
<p>
  “О Пандора! Току що отвори кутията с ужаси!” - смехът му се сля с нейния и
  нежно я придърпа към себе си. Прегърнати и щастливи посрещнаха последния си
  залез в Мексико.
</p>
<p>
  Три месеца по-късно търсенето на “универсалният хорър” покри със смачкани
  листа хартия пода в кабинета на Емет. Разбира се, не беше сам в това
  маниакално вече проучване. Спалнята им, преди - неприкосновен храм на любовта,
  се превърна в лабиринт от разхвърляни учебници по психология за всички
  възможни фобии преследващи homo sapiens. Верандата, любимо място на
  множеството им приятели, посрещаше вече само прочелите хорър роман от списъка
  залепен над купчината книги.
</p>
<p>
  “Мисля, че зациклихме … хммм ужасно” - прекъсна мълчаливата вечеря Пандора.
</p>
<p>
  “Не искам да се отказваме скъпа, но да - права си. Тези дни мислих, че е време
  да сменим подхода.”
</p>
<p>“Да сменим подхода? Емет, какво искаш да кажеш?”</p>
<p>
  “Пандора, сега ние търсим универсалния страх изследвайки всички възможности и
  всички хора. Това виждаш се оказа непосилна задача. Мисля, да подложим един,
  човек на нещо, което да изведе всичките му страхове наяве. И да ги пресеем за
  да открием този, този който търсим.”
</p>
<p>
  “Какво? Ти си луд? Това е рисковано и неетично. А и няма как да определим тези
  страхове обективно.”
</p>
<p>
  “Всъщност има начин. Единственият възможен е аз да бъда хммм … опитната
  мишка.”
</p>
<p>
  “Ти? Уравновесения, логичния?!? Хаха това вече ще е непосилна задача.”- смехът
  и обаче бързо заглъхна. Както обикновено, Емет имаше безпогрешна логика. Но
  как, той дори не се поддаде на хипноза когато пробваха от любопитство в
  началото на връзката си.
</p>
<p>
  “Знам какво мислиш мила, но имам още една идея. Спомняш ли си бармана в
  Мексико, който ни разказа за шамана, негов роднина. Тази седмица много мислих.
  И проучвах. Струва да опитам.”
</p>
<p>“Каквооооо?!? Не! Не съм съгласна. Твърде опасно е, дори за теб.”</p>
<p>
  “Разбирам, но ако до седмица не открием това, което търсим ще поема този
  риск.” - очакваше този отговор и премълча, за купения вече билет.
</p>
<p>
  Каменистия път свърши и раздрънкания пикап спря рязко вдигайки облак прах.
  Хосе посочи в далечината посивяла дървена къща сред хълмовете обрасли с
  кактуси.
</p>
<p>
  “Не е късно да се откажеш. Аз съм до тук. Ще се върна за теб след седмица.”
</p>
<p>“До скоро приятелю.” - Емет подаде запечатан плик и намигна за довиждане.</p>
<p>
  Бараката се оказа по-далече отколкото изглеждаше, затова спря да си почине.
  Бармана скоро изчезна от хоризонта. След още три почивки, най-накрая малко
  преди залеза, уморен да гони нахалните мухи привлечени от калните солени
  вадички по лицето, се добра пред дома на шамана. Почука внимателно няколко
  пъти, но никой не отговори. Натисна бавно вратата, която толкова лесно и тихо
  се отвори, че се оказа неусетно в средата на полътумна стая. Очакваше скърцане
  или други, стимулиращи уплаха ефекти. Дотук с очакванията. В дъното, сред
  процеждащата се оранжево червена светлина между дъсчените стени, стоеше
  неподвижен тъмния силует на шамана. Една сянка се плъзна бавно по пода към
  Емет. Различи ръка, която му сочеше с пръст нара зад вратата. Умората надделя
  раздразненото и незадоволено любопитство и реши да се наспи първо.
</p>
<p>
  Сутринта завари до себе си купа с корени и бутилка вода. Тишината, горчивите
  корени и непомръдващия силует на шамана не се промениха и на петия ден.
  Прекара цялото това време на нара с изключение на минутите за облегчаване на
  биологичните си нужди зад бараката. Няколко пъти заговаряше шамана, но сянката
  размахваше пръст и застиваше отново, а той така и не се реши да я доближи. Е
  това беше, опитахме но явно е време е да приемем този проект за неуспешен -
  недоволен разтри схванатите си рамене и заспа с решението утрешния ден да е
  последен и да се разходи наоколо с фотоапарата си.
</p>
<p>“Добро утро!” - казани на правилен английски думи събудиха Емет.</p>
<p>Ниската масичка пред нара му беше отрупана с различни плодове от кактуси.</p>
<p>
  “Нахрани се добре, ще имаш нужда.” - усмивката не слизаше от лицето на шамана.
</p>
<p>
  По време на дългата закуска говориха много. Сянката, която с дни стоеше в
  другия край на дървената къща се оказа интересен и образован мъж. Също като
  него е учил първо инженерство а после икономика. Но след това е решил, че
  науката не може да обясни много неща и е се е обърнал към тайните, предавани в
  неговия род на духовни водачи. Разбра защо е бил подложен на изпитание -
  сливането на съзнанието и подсъзнанието щеше го заведе в свят от, който могат
  да се върнат хора имащи във всеки един момент връзка с реалността. Щяха да
  направят три последователни опита и за всеки от тях имаше приготвена малка
  купичка с разноцветни изсушени гъби.
</p>
<p>
  “И не забравяй, не изпускай малкото огледало от ръката си. Ако загубиш
  представа кое е сън и кое не - погледни в него. Ако не видиш себе си и надписа
  над главата си значи си в илюзията. Време е.”- подаде му първата малка купичка
  шамана, и стисна юмрука му за да не изпуска и за секунда ценния предмет.
</p>
<p>
  Огромна ръка се плъзна под тялото му и го сграбчи. Стреснат се събуди но
  невидимата сила го стегна още по здраво в хватката си. Ръцете и краката
  изтръпнали не можеха да помръднат. Инстинктивно се опита да извика но гърдите
  му притиснати от невидимата сила не успяха да издадат и звук. Не! Това не е
  реално - логиката му опита да внесе спокойствие. Огледа се. Беше се стъмнило
  но беше сам. Съпротивлявайки се с тежеста върху гърдите си, пое бавно дълбоко
  въздух. Лека по-лека хватката се отпусна и изчезна.
</p>
<p>
  Е “номер едно” си струваше, ухили се доволно а адреналина разнесе топла вълна
  във вените му.
</p>
<p>
  Докато си почиваше преди да вземе втората купичка вратата с трясък се удари в
  стената от рязкото отваряне и в къщата нахълтаха Пандора и бармана. Запъхтени
  и потни крещяха - “Бързо, няма време!”
</p>
<p>Докато се осъзнае какво се случва оплетоха краката му с дебело въже.</p>
<p>
  “Скъпи не забравяй ръцете!” - жена му целуна латиноамериканеца и извади
  огромна спринцовка.
</p>
<p>
  Ледена и влажна дланта ѝ запуши устата му а другата ѝ ръка замахна. Острата
  игла проби гръкляна спирайки се в прешлена на врата, пресичайки изненадания му
  вик. Черен мрак.
</p>
<p>
  Задушаваше се. Лепкава течност гъргореше в гърлото му. Опита се да преглътне
  но забитата игла му попречи и изкрещя изненадан от болката. На масата догаряше
  свещ до празната купичка. Пандора и Хосе седяха на пода, вторачени един в друг
  безмълвно и неподвижно. С всеки опит да помръдне примките на въжето го стягаха
  все по здраво. Огледалцето! Размърда пръстите на ръцете си. Стискаше
  спасителния предмет, но не можеше да го погледне. Пламъка на свеща се разклати
  за последно и стаята се изпълни с тъмнина. Все още не можеше да помръдне а
  болката в гърлото му стана нетърпима. Мисли Логично! … Мисли Логично! Оххх…
  Поспи за да изтлее този кошмар! Оммм!
</p>
<p>
  Жажда. Чак когато изпи пълната стъклена кана вода и седна на нара съзнанието
  му възстанови напълно реалността. Процеждащите се през дъските слънчеви лъчи
  идваха от посоката на залеза. Нямаше никой в къщата. А пред него имаше две
  празни и една пълна купички. Тялото му все още потръпваше от въображаемата
  болка. А гърлото му продължаваше да е сухо и парещо където “беше” прободено.
  Дълго медитира докато смелостта и спокойствието му се окопитят. Всичко е
  илюзия осъзнаваше, но определено не беше приятно изживяване. В едната си ръка
  стисна огледалцето и изсипа съдържанието на последната купичка в устата си.
  Легна и зачака, повтаряйки си мислено, този път - да остане буден и в съзнание
  каквото и да се случва.
</p>
<p>
  Миризмата на белина разбунтува стомаха му и стисна зъби за да не повърне. Но,
  господи?! Какво е това? Болките в тялото му бяха изчезнали. Но с тях беше
  изчезнала и дървената къща на шамана. Около него всичко беше бяло. Матово
  стъкло на тавана се светеше със студена неонова светлина. В дъното, до беглото
  очертание на врата без дръжка, на пода имаше поднос с парче хляб, чиния с
  някаква каша и бутилка вода. Разочаровано изцъка с език. Това тук беше загуба
  на време. Но все пак очакваше най-страшното при третия последен опит. Затова
  реши да изчака. Сетивата му затворени в тази стая загубиха представа за
  времето. Но след пореденото задоволяване на въображаемия си глад се замисли.
  Не помнеше броя на тези хранения - безкрайно много но подробностите му се
  губеха. Реши да направи експеримент и остави парче хляб зад леглото си.
</p>
<p>
  Броенето беше единственото забавление този ден. И следващия. И по следващия.
  Когато стигна до 300 спря. Не искаше да прекъсва експеримента но досадата и
  усещането как цялото му същество и тяло отслабват и придобиват неприятна
  тежест взеха връх. Искаше всичко това да свърши, да се отпусне във ваната си с
  бутилка вино и да забрави за винаги металната кофа от която се разнасяше воня
  в дъното на тази отвратителна бяла стая. Край. Потърси огледалцето.
</p>
<p>
  Седнал на леглото гледаше безизразно. Беше опипал всеки сантиметър. Не можеше
  да спре желанието да прекрати този безумен сън а от спасителния изход нямаше и
  следа. Беше загубил проклетото огледалце.
</p>
<p>
  500, изпълни се с отчаяние. Това трябва да свърши сега! Захапа с всичка сила
  кутрето си и коста изхрущя. Нетърпима болка схвана ръката му. Изплю пръста и
  закрещя. Подът под него се отвори. Мрак.
</p>
<p>
  Гледаше превързаната си ръка и недоумяваше защо го боли челюстта а не раната.
  Опипа лицето си. Брада в съня? Истеричния му смях изпръска белия под с капки
  кръв. А болката в устата стана нетърпима. Пръста му се плъзна в устата и на
  мястото на прекрасните зъби, с които се гордееше, напипа болезнени дупки.
  Повърна и въпреки разбирането, че това е илюзия, безпомощността на продължилия
  цяла вечност сън го разплака. За пръв път се чустваше толкова отчаян.
</p>
<p>
  Изминаха още много дни. Единственото което правеше, когато беше буден, е да
  опита отново да медитира. Трябваше да съхрани съзнанието си и да се събуди от
  този кошмар. Целта му - да се подготви да победи затвора на собственото си
  подсъзнание. Малко по малко се успокои.
</p>
<p>
  Един ден реши, време е да действа. Ако не друго, поне да намери по-приятно
  място където има и зъболекари - абсурдния сарказъм оставаше единственото му
  забавление. Само да успее да размърда тялото си в реалността, може и да успее
  да намери огледалцето. Тази фантасмагория със сигурност има своите си правила
  - все пак храната се появява, някой се погрижи за пръста, о да и за усмивката
  ми. Хилеше се докато обмисляше спасителния план.
</p>
<p>
  Реши да не докосва донесената храна. Трябваше да се случи нещо. Имаше
  достатъчно запаси под леглото си за да симулира гладна стачка пред
  подсъзнанието си. Още първата вечер връхлитащия го до сега дълбок сън не се
  появи. Цялата нощ наблюдава очертанията на вратата.
</p>
<p>
  В момента в който вратата се отвори скочи от леглото. Блъсна огромната жена,
  която се бе появила да смени подноса с храна. Озова се в дълъг полутъмен
  коридор. В дъното го очакваше спасение - двойна врата в рамката на която имаше
  огледало. Облегчен, радостно напрегна последните си сили и хукна към
  отражението си там в далечината, което също затича към него.
</p>
<p>
  Дланта с липсващ пръст докосна двойника си на хладното стъкло. Възрастен,
  кльощав, брадясал мъж с дълга разчорлена коса - го гледаше обезумяло от
  другата страна. Беззъбата му уста се отвори в ужас. Разпозна своя образ. Но
  прочете и надписа над себе си - Психиатричен Затвор “Сан Себастиан”.
</p>"""