from anvil_extras.storage import indexed_db

user_settings = indexed_db.create_store('user_settings')
browser = indexed_db.create_store('browser')


def save_last_open(last_open):
    user_settings['last_open'] = last_open

def get_last_open():
    if 'last_open' in user_settings:
        return user_settings['last_open']
    else:
        return 'Reader.Today'