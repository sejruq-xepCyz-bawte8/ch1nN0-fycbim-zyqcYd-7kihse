from anvil import *
from .Device import has_device, init_device
import App


def is_init()->bool:
    if has_device():
        return App.init_app()
    else:
        if init_device():
            return App.init_app()
        else:
            return False

def main():
    App.NAVIGATION.add_to_body()
    open_form('Forms._Welcome')
    

    
    

if __name__ == "__main__":
    if is_init(): main()
    else:
        print('NO INIT')