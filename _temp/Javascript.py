from anvil.js import window
from anvil.js.window import document
from anvil.js.window import navigator

def add_class_html(css:str):
    document.documentElement.classList.add(css)

def scriptLoad(src):
    script = document.createElement('script')
    script.src = src
    document.head.appendChild(script)



scripts = [
"_/theme/javascript/init.js",
"https://kit.fontawesome.com/dcfe5f394f.js",
"https://cdn.jsdelivr.net/npm/quill@2.0.1/dist/quill.js",
"_/theme/javascript/init_viewport.js",
"_/theme/javascript/lokijs.js",
"_/theme/javascript/loki-indexed-adapter.js",
"_/theme/javascript/quill_counter.js",
]

def is_touch(addclass:bool = True):
    if 'ontouchstart' in window:
        result = 'is_touch'
    elif 'maxTouchPoints' in navigator:
        if navigator.maxTouchPoints > 0 :
            result = 'is_touch'
    elif 'msMaxTouchPoints' in navigator:
        if navigator.msMaxTouchPoints > 0 :
            result = 'is_touch'
    result = 'not_touch'
    if addclass:
        add_class_html(result)
    return result

def screen_info(addclass:bool = True):
    width = window.screen.width
    height = window.screen.height
    if width > height:
        orientation = "portrait"
    else:
        orientation = "landscape"
    if addclass:
        add_class_html(orientation)
        if width < 400:
            add_class_html('small')
        elif width < 600:
            add_class_html('medium')
        elif width < 800:
            add_class_html('big')
        else:
            add_class_html('large')
    return width, height, orientation