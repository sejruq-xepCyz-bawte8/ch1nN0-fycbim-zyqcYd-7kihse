from anvil.js.window import jQuery as jQ
from ..Index import App
from anvil import *

NAV_TREE = [
    {   
        'group': 'Reader',
        'is_device':True,
        'is_user':False,
        'is_author':False,
        'onclick':'open_form',
        'style':'duotone',
        'init_hidden':False,
        'links':[
        {'text':'Днес', 'form':'Reader_Today'},
        {'text':'Творби', 'form':'Reader_Charts'},
        {'text':'Автори', 'form':'Reader_Authors'},
        {'text':'Отметки', 'form':'Reader_Bookmarks'},
        {'text':'Настр.', 'form':'Settings_Info'},
        {'text':'Писател', 'form':'Author_Works', 'is_author':False,},
        {'text':'Творба', 'form':'Work_Viewer','style':'thin'},
        ],
    },
            {   
        'group': 'Settings',
        'is_device':True,
        'is_user':False,
        'is_author':False,
        'onclick':'open_form',
        'style':'duotone',
        'init_hidden':True,
        'links':[
        {'text':'Назад', 'form':'Reader_Today'},
        {'text':'Филтри', 'form':'Settings_Filters'},
        {'text':'Теми', 'form':'Settings_Interface'},
        {'text':'Потребител', 'form':'Settings_User'},
        {'text':'Инфо', 'form':'Settings_Info'},
        ],
    },
        {   
        'group': 'Work',
        'is_device':True,
        'is_user':False,
        'is_author':False,
        'onclick':'open_form',
        'style':'duotone',
        'init_hidden':True,
        'links':[
        {'text':'Назад', 'form':'Reader_Today'},
        {'text':'Творба', 'form':'Work_Viewer'},
        {'text':'Корица', 'form':'Work_Cover'},
        {'text':'Запази', 'form':'Work_Viewer', 'onclick':'click_bookmark'},
        {'text':'Харесай', 'form':'Work_Viewer', 'onclick':'click_like'},
        ],
    },
        {   
        'group': 'Author',
        'is_device':True,
        'is_user':False,
        'is_author':False,
        'onclick':'open_form',
        'style':'duotone',
        'init_hidden':True,
        'links':[
        {'text':'Днес', 'form':'Reader_Today'},
        {'text':'Нова', 'form':'Editor_NewWork'},
        {'text':'Творби', 'form':'Author_Works'},
        {'text':'Профил', 'form':'Author_Profile'},
        {'text':'Статс', 'form':'Author_Stats'},
        ],
    },
            {   
        'group': 'Editor',
        'is_device':True,
        'is_user':False,
        'is_author':False,
        'onclick':'open_form',
        'style':'duotone',
        'init_hidden':True,
        'links':[
        {'text':'Назад', 'form':'Author_Works'},
        {'text':'Текст', 'form':'Editor_NewWork'},
        {'text':'Жанр', 'form':'Editor_Cover'},
        {'text':'Корица', 'form':'Editor_Cover'},
        {'text':'Публикувай', 'form':'Editor_Publish'},
        ],
    }
  
]

class NavigationClass:
    def __init__(self) -> None:
        self.el = jQ(f'<dir>')
        self.el.attr('id', 'navigation')
        self.el.addClass('ch ch-nav')
        self.tree:list = NAV_TREE
        self.is_device:bool = bool(App.DEVICE_ID)
        self.is_user:bool = bool(App.USER_ID)
        self.is_author:bool = bool(App.AUTHOR_ID)
        self.build()

    def build(self):
        for container in self.tree:
            if not self.is_device and container['is_device'] : continue
            if not self.is_user and container['is_user'] : continue
            if not self.is_author and container['is_author'] : continue
            group_name:str = container['group']
            group_el = jQ(f'<dir>')
            group_el.addClass('ch ch-nav-group')
            group_el.attr('id', f'navg-{group_name}')
            if container['init_hidden']: group_el.hide()
            jQ(self.el).append(group_el)

            aw_style:str = container['style'] if 'style' in container else None
            for link in container['links']:
                if not self.is_device and 'is_device' in link and link['is_device'] : continue
                if not self.is_user and 'is_user' in link and link['is_user'] : continue
                if not self.is_author and 'is_author' in link and link['is_author'] : continue
                if 'style' in link : aw_style = link['style'] 
                link_el = jQ(f'<dir>')
                
                formgroup:str = link['form'].split('_')[0]

                onclick_func:str = link['onclick'] if 'onclick' in link else container['onclick']

                link_id = f'navl-{group_name}-{link["form"]}-{formgroup}-{onclick_func}'
                link_el.addClass('ch ch-nav-link')
                link_el.attr('id', link_id)
                link_el.attr('onclick', f'anvil.call($("#appGoesHere > div"), "navClick", $(this))')

                icon_el = jQ(f'<span>')
                awesome_css:str = App.AW.get_css(bg=link['text'], style=aw_style)
                icon_el.addClass(f'ch ch-nav-icon {awesome_css}')

                text_el = jQ(f'<span>')
                text_el.addClass('ch ch-nav-text')
                text_el.text(link['text'])

                jQ(link_el).append(icon_el)
                jQ(link_el).append(text_el)
                jQ(group_el).append(link_el)

    def add_to_body(self):
        jQ('body').append(self.el)

    def reset(self):
        self.el.clear()
        self.is_device:bool = bool(App.DEVICE_ID)
        self.is_user:bool = bool(App.USER_ID)
        self.is_author:bool = bool(App.AUTHOR_ID)

    def click(self, link, group_name:str, form_name:str, form_group:str, function_name:str):
        jQ('#navigation *').removeClass('nav-clicked')
        jQ(f'#navl-{form_group}-{form_name}-{form_group}-{function_name}').addClass('nav-clicked')
        if group_name is not form_group:
            jQ(f'#navg-{group_name}').hide()
            jQ(f'#navg-{form_group}').show()

 
        
            
            




        
        