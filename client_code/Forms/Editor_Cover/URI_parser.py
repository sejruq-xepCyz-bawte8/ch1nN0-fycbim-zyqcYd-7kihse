import anvil.http

from anvil_extras import zod as z
import re

schema_url = z.coerce.string().min(3).regex(re.compile(r"^[a-zA-Z\d\-._~]+$")) #@$!%*?&#


def uri_zod(sender, **event):

    sender.valid = schema_url.safe_parse(sender.text).success
    sender.background = "1px solid LightBlue" if sender.valid else "1px solid LightSalmon"

def encode_uri(string:str=None):
    if string == None:
        return None
    else:
        return anvil.http.url_encode(string)