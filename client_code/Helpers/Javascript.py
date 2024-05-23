from anvil.js.window import document

def script_to_head_load(src:str) -> None:
    script = document.createElement('script')
    script.src = src
    document.head.appendChild(script)