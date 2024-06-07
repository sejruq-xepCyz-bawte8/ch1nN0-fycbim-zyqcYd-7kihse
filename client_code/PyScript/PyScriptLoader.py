from anvil.js.window import jQuery as jQ


PYSCRIPT_FILE_PARSER = False

#<script type="py" src="./main.py" config="./pyscript.toml" terminal></script>

def load_pyscript(src:str=None) -> None:
    
    scriptId = 'pyscript'
    scriptUrl = 'https://pyscript.net/releases/2024.5.2/core.js'
    existingScript = jQ(f'#{scriptId}')
    if not existingScript:
      script = jQ('<script>', {
                        'type': 'module',
                        'src': scriptUrl,
                        'id': scriptId
                    })
      jQ('head').append(script)
     

def load_pyscript_docx_parser(src:str=None) -> None:
    scriptId = 'docx_parser'
    scriptUrl = '/_/theme/pyscript/DOCX_parser.py'
    scriptConfig = '/_/theme/pyscript/DOCX_parser.toml'
    existingScript = jQ(f'#{scriptId}')
    if not existingScript:
      script = jQ('<script>', {
                        'type': 'py',
                        'src': scriptUrl,
                        'config': scriptConfig,
                        'id': scriptId,
                      
                    })
      jQ('head').append(script)

def load_pyscript_md_parser(src:str=None) -> None:
    scriptId = 'md_parser'
    scriptUrl = '/_/theme/pyscript/MD_parser.py'
    scriptConfig = '/_/theme/pyscript/MD_parser.toml'
    existingScript = jQ(f'#{scriptId}')
    if not existingScript:
      script = jQ('<script>', {
                        'type': 'py',
                        'src': scriptUrl,
                        'config': scriptConfig,
                        'id': scriptId,
                      
                    })
      jQ('head').append(script)

def load_pyscript_files_parser(src:str=None) -> None:
    scriptId = 'files_parser'
    scriptUrl = '/_/theme/pyscript/FILES_parser.py'
    scriptConfig = '/_/theme/pyscript/FILES_parser.toml'
    existingScript = jQ(f'#{scriptId}')
    if not existingScript:
      script = jQ('<script>', {
                        'type': 'py',
                        'src': scriptUrl,
                        'config': scriptConfig,
                        'id': scriptId,
                      
                    })
      jQ('head').append(script)