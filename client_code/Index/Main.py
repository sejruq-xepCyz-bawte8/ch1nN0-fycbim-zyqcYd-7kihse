from anvil import *
from .Device import has_device, init_device
import App
from anvil.js import window


VER = '0.8.1'

def version():
    n = Notification(f'<i class="fa-regular fa-flask"></i><span>Тестова версия - {VER}</span>', style="info", timeout=2)
    n.show()


def main():
    device = has_device()
    if not device:
        print('new device')
        device = init_device()
    
    if device:
        print('device ok')
        app = App.init_app()
    else:
        print('no device')
        app = None
   
    if app:
        App.NAVIGATION.add_to_body()
        version()
        open_form('Forms.Reader_Today')
    else:
        print('no app')


def error_handler(err):
    n = Notification('<i class="fa-regular fa-bug"></i> упс открихте бъг', style="danger", timeout=1.5)
    n.show()  
    

if __name__ == "__main__":
    
    print(f'ЧетеМе - {VER}')
    
    set_default_error_handling(error_handler)
    
    main()
    
    