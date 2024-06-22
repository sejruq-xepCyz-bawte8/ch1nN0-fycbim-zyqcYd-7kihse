from anvil.js.window import jQuery as jQ
from ...Index.App import GENRES, AW
from .Fonts import fonts


class CoverClass:
    def __init__(self, data:dict) -> object:
        self.data = data
        self.icons_bg = []

        for g in data['genres'][1:]:
            if g : self.icons_bg.append(g)
        for i in data['icons']:
            if AW.has_name(bg=i):
                self.icons_bg.append(i)


        #COVER CONTAINER
        self.el = jQ(f'<dir>')
        #self.el.attr('id', 'navigation')
        self.el.addClass('ch ch-cover-work')
        self.el.css('background-color', self.data['background_color'])
        if self.data['background_image'] :
            image = f"""url("{self.data['background_image']}")"""
            self.el.css('background-image', image) #f'url("{self.data['background_image']}")'
        self.el.css('color', self.data['color'])

        #HEADER
        self.el_header = jQ(f'<dir>')
        self.el_header.addClass('ch ch-cover-header')
        

        
        
        #MASK
        self.el_mask = jQ(f'<dir>')
        self.el_mask.addClass('ch ch-cover-mask')

        
        mask = int(self.data['cover_mask']) / 100
        hex_shadow = self.data['mask_color'].lstrip('#')
        rgb = tuple(int(hex_shadow[i:i+2], 16) for i in (0, 2, 4))
        mask_color = f'linear-gradient(to top, rgba({rgb[0]},{rgb[1]},{rgb[2]},{mask}) 0%, rgba({rgb[0]},{rgb[1]},{rgb[2]}, 0) 100%)'
        self.el_mask.css('background-image', mask_color)


        #TITLE
        self.el_title = jQ(f'<dir>')
        self.el_title.text(self.data['title'])
        self.el_title.addClass('ch ch-cover-title')
        

        #font = fonts[self.data['font']]
        #if self.data['font'] in fonts:
        #    font = fonts[self.data['font']]
        #else:
        #    font = fonts['serif']

        self.el_title.addClass(self.data['font'])
        #self.el_title.css('font-family', font['font-family'])
        #self.el_title.css('font-weight', font['font-weight'])
        #self.el_title.css('font-style', font['font-style'])


        #ICONS
        self.el_icons = jQ(f'<dir>')
        self.el_icons.addClass('ch ch-cover-icons')
        level=0
        for bg in self.icons_bg:
            icon_el = jQ(f'<span>')
            aw = AW.get_css(bg=bg)
            icon_css = f'ch ch-cover-icon ch-cover-icon-{level} {aw}'
            icon_el.addClass(icon_css)
            jQ(self.el_icons).append(icon_el)
            level += 1



        self.assemle_cover()



    def add_cover(self, container:object)->bool:
        if self.el:
            jQ(container).append(self.el)
            return True
        else:
            return False
    
 
        

 
    def assemle_cover(self)->None:
       
        jQ(self.el_mask).append(self.el_header)
        jQ(self.el_mask).append(self.el_title)
        jQ(self.el_mask).append(self.el_icons)
        jQ(self.el).append(self.el_mask)
