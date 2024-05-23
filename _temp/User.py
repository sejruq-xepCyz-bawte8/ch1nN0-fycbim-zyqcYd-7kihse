import anvil.users
from Javascript import add_class_html

def update_user(addclass:bool = True):
    user = anvil.users.get_user()
    if addclass and user:
        add_class_html('is_user')
        if 'is_author' in user:
            if user['is_author']:
                add_class_html('is_author')
    elif addclass and not user:
        print('THIS')
        add_class_html('not_user')

    return user