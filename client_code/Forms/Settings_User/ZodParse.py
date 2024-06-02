from anvil_extras import zod as z
import re

schema_email = z.coerce.string().min(8).email()
schema_password = z.coerce.string().min(8).regex(re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$")) #@$!%*?&#
schema_code = z.coerce.string().min(8).email().endswith("CHE")



def code_zod(sender, **event):
    sender.valid = schema_email.safe_parse(sender.text).success
    sender.background = "LightBlue" if sender.valid else "LightSalmon"

def email_zod(sender, **event):
    sender.valid = schema_email.safe_parse(sender.text).success
    sender.background = "LightGreen" if sender.valid else "LightSalmon"
    
def password_zod(sender, **event):
    sender.valid = schema_password.safe_parse(sender.text).success
    sender.background = "LightGreen" if sender.valid else "LightSalmon"
    return sender.valid