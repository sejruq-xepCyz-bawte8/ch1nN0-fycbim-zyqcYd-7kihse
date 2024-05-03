from .Collection_Module import Collection


class Awesome(Collection):
  def __init__(self):
    super().__init__()
    self.collection.insert(icons)

  def get_icon_code(self, bg):
    return self.get_one('bg', bg)

  def get_icon_bg(self, name):
    return self.get_one('name', name)


icons = [{'name':'home', 'bg':'Днес'},
         {'name':'glasses', 'bg':'Автори'},
         {'name':'books', 'bg':'Творби'},
         {'name':'bookmark', 'bg':'Отметки'},
         {'name':'user', 'bg':'Вход'},
         {'name':'sliders', 'bg':'Настройки'},
         {'name':'typewriter', 'bg':'Автор'},
         {'name':'file-plus', 'bg':'Създай'},
          {'name':'chart-simple', 'bg':'Стат'},
         {'name':'address-card', 'bg':'Профил'},
         {'name':'icons', 'bg':'Тест'},
        ]


