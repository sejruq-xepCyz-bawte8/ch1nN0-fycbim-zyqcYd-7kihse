from anvil import *
from .Device import has_device, init_device
import App
from anvil.js import window




VER = '0.8.1'

def version():
    n = Notification(f'<i class="fa-regular fa-flask"></i><span>Тестова версия - {VER}</span>', style="info", timeout=2)
    n.show()


def is_init()->bool:
    if has_device():
        return App.init_app()
    else:
        if init_device():
            return App.init_app()
        else:
            n = Notification('грешно устройство :)', style="danger", timeout=1.5)
            n.show()
            return False

def main():
    
# This code displays an Anvil alert, rather than
# the default red box, when an error occurs.
    version()
    def error_handler(err):
        n = Notification('<i class="fa-regular fa-bug"></i> упс открихте бъг', style="danger", timeout=1.5)
        n.show()
        #alert(str(err), title="An error has occurred")

    set_default_error_handling(error_handler)


    App.NAVIGATION.add_to_body()
    
    open_form('Forms.Reader_Today')
    

    
    

if __name__ == "__main__":
    #window.console.clear()
    
    if is_init(): main()
    else:
        print('NO INIT')