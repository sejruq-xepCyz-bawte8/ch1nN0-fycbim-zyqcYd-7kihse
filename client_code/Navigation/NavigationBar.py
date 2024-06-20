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
        {'text':'Писател', 'form':'Author_Works', 'is_author':True,},
        {'text':'Творба', 'form':'ViewerW_Work','style':'thin', 'init_hidden':True,},
        {'text':'Автор', 'form':'ViewerA_Author','style':'thin', 'init_hidden':True,},
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
        {#VieverAuthor
        'group': 'ViewerA',
        'is_device':True,
        'is_user':False,
        'is_author':False,
        'onclick':'open_form',
        'style':'duotone',
        'init_hidden':True,
        'links':[
        {'text':'Назад', 'form':'Reader_Today'},
        {'text':'Инфо', 'form':'ViewerA_Author'},
        {'text':'Творби', 'form':'ViewerA_Works'},
        {'text':'Запази', 'form':'ViewerA_Author', 'onclick':'click_bookmark'},
        {'text':'Харесай', 'form':'ViewerA_Author', 'onclick':'click_like'},
        ],
    },
        {#VieverWork
        'group': 'ViewerW',
        'is_device':True,
        'is_user':False,
        'is_author':False,
        'onclick':'open_form',
        'style':'duotone',
        'init_hidden':True,
        'links':[
        {'text':'Назад', 'form':'Reader_Today'},
        {'text':'Творба', 'form':'ViewerW_Work'},
        {'text':'Корица', 'form':'ViewerW_Cover'},
        {'text':'Запази', 'form':'ViewerW_Work', 'onclick':'click_bookmark'},
        {'text':'Харесай', 'form':'ViewerW_Engage'},
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
        {'text':'Нова', 'form':'Author_NewWork'},
        {'text':'Чернови', 'form':'Author_Works'},
        {'text':'Онлайн', 'form':'Author_PWorks'},
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
        {'text':'Текст', 'form':'Editor_Work'},
        {'text':'Жанр', 'form':'Editor_Tags'},
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
        self.current_link = None
        self.build()

    def build(self):
        
        for container in self.tree:
            if not App.IS_DEVICE and container['is_device'] : continue
            if not App.IS_USER and container['is_user'] : continue
            if not App.IS_AUTHOR and container['is_author'] : continue
            group_name:str = container['group']
            group_el = jQ(f'<dir>')
            group_el.addClass('ch ch-nav-group')
            group_el.attr('id', f'navg-{group_name}')
            if container['init_hidden']: group_el.hide()
            jQ(self.el).append(group_el)

            aw_style:str = container['style'] if 'style' in container else None
            for link in container['links']:
                if not App.IS_DEVICE and 'is_device' in link and link['is_device'] : continue
                if not App.IS_USER and 'is_user' in link and link['is_user'] : continue
                if not App.IS_AUTHOR and 'is_author' in link and link['is_author'] : continue
                if 'style' in link : aw_style = link['style'] 
                link_el = jQ(f'<dir>')
                
                formgroup:str = link['form'].split('_')[0]

                onclick_func:str = link['onclick'] if 'onclick' in link else container['onclick']

                link_id = f'navl-{group_name}-{link["form"]}'
                link_el.addClass('ch ch-nav-link')
                link_el.attr('id', link_id)
                link_el.attr('onclick', f'anvil.call($("#appGoesHere > div"), "navClick", $(this))')
                link_el.attr('data-form', link['form'])
                link_el.attr('data-current_group', container['group'])
                link_el.attr('data-form_group', formgroup)
                link_el.attr('data-onclick', onclick_func)

                icon_el = jQ(f'<span>')
                awesome_css:str = App.AW.get_css(bg=link['text'], style=aw_style)
                icon_el.addClass(f'ch ch-nav-icon {awesome_css}')

                text_el = jQ(f'<span>')
                text_el.addClass('ch ch-nav-text')
                text_el.text(link['text'])

                if link.get('init_hidden'):
                    link_el.hide()

                jQ(link_el).append(icon_el)
                jQ(link_el).append(text_el)
                jQ(group_el).append(link_el)

    def add_to_body(self):
        jQ('body').append(self.el)

    def reset(self):
        self.el.empty()
        self.build()

    def click(self, link):
        if link.attr('data-onclick') == 'open_form':
            if self.current_link : self.current_link.removeClass('nav-clicked')
            new_link = jQ(f"#navl-{link.attr('data-form_group')}-{link.attr('data-form')}")
            new_link.addClass('nav-clicked')
            self.current_link = new_link

        if link.attr('data-current_group') is not link.attr('data-form_group'):
            jQ(f"#navg-{link.attr('data-current_group')}").hide()
            jQ(f"#navg-{link.attr('data-form_group')}").show()
        print(link.attr('data-current_group'), link.attr('data-form_group'))
 
        
            
            




        
        