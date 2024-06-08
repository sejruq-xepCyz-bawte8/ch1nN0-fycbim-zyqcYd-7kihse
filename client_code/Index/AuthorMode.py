



# PYSCRIPT
def init_pyscript(self):
if not PyScriptLoader.PYSCRIPT_FILE_PARSER:
    PyScriptLoader.load_pyscript()
    PyScriptLoader.load_pyscript_files_parser()

def FILES_parser_loaded(self, pyscript, **event):
    PyScriptLoader.PYSCRIPT_FILE_PARSER = True