from anvil_extras import zod as z
import re


schema_uri = z.coerce.string().min(1).regex(re.compile(r'^[a-zA-Z0-9._~%-]+$')) 
schema_author_name = z.coerce.string().min(1)
    
def uri_zod(sender, **event):
    sender.valid = schema_uri.safe_parse(sender.text).success
    sender.background = "LightGreen" if sender.valid else "LightSalmon"
    return sender.valid

def author_name_zod(sender, **event):
    sender.valid = schema_author_name.safe_parse(sender.text).success
    sender.background = "LightGreen" if sender.valid else "LightSalmon"
    return sender.valid