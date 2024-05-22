from ._anvil_designer import EditorTemplate
from ...Cheteme.Main import navigation_click
from anvil import *
from anvil_extras.hashlib import sha256
from time import time

from ...Cheteme.Main import user

class Editor(EditorTemplate):
  def __init__(self, **properties):
    self.navigation_click = navigation_click
    #print(sha256("Hello World!"))
    #self.add_event_handler('show', self.form_show)
    self.init_components(**properties)


  def post(self, *event):
    from anvil.js.window import quill
    
    work_id = None

    if user:
      if 'uid' in user:
        uid = user['uid']
      else:
        uid = 'testuser'
    else:
      uid = 'testuser'

    if work_id:
      wid = work_id
    else:
      wid = sha256(f"{uid}{str(time())}")

    words = int(self.dom_nodes['counter'].innerText)
    html_content = quill.getSemanticHTML()


    data = {
      'wid': wid,
      'uid': uid,
      'words': words,
      'html': html_content
    }
    print(data)
    open_form('Author.Publish', data)




