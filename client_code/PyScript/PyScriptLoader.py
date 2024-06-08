from anvil.js.window import jQuery as jQ

def has_pyscript():
   return jQ('html').hasClass('pyscript-cheteme')

def load_pyscript(src:str=None) -> None:
    scriptIdCore = 'pyscript-core'
    existingCore = jQ(f'#{scriptIdCore}')
    if not existingCore:
      script = jQ('<script>', {
                        'type': 'module',
                        'src': 'https://pyscript.net/releases/2024.5.2/core.js',
                        'id': scriptIdCore
                    })
      jQ('head').append(script)
     
    scriptIdCheteme = 'pyscript-cheteme'
    existingCheteme = jQ(f'#{scriptIdCheteme}')
    if not existingCheteme:
      script = jQ('<script>', {
                        'type': 'py',
                        'src': '/_/theme/pyscript/main.py',
                        'config': '/_/theme/pyscript/main_settings.toml',
                        'id': scriptIdCheteme,
                      
                    })
      jQ('head').append(script)