import anvil.http

from anvil_extras import zod as z
import re

schema_url = z.string().url()



def uri_zod(sender, **event):

    sender.valid = schema_url.safe_parse(sender.text).success
    sender.background = "LightBlue" if sender.valid else "LightSalmon"

def encode_uri(string:str=None):
    if string == None:
        return None
    else:
        return anvil.http.url_encode(string)