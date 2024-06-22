from anvil_extras import zod as z
import re

schema_url = z.coerce.string().min(3).regex(re.compile(r"^[a-zA-Z\d\-_~]+$")) #@$!%*?&#
schema_title = z.coerce.string().min(3)

def uri_zod(sender):

    sender.valid = schema_url.safe_parse(sender.text).success
    sender.border = "1px solid LightGreen" if sender.valid else "1px solid LightSalmon"

def title_zod(sender):

    sender.valid = schema_title.safe_parse(sender.text).success
    sender.border = "1px solid LightGreen" if sender.valid else "1px solid LightSalmon"
