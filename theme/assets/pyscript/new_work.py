from pyscript import when, display
from js import document, window, Uint8Array
from DOCX_parser import docx_to_html



#@when("click", "#my_button")
def handle_click(event):
    print(event)   


#@when("change", "#file-upload")
async def upload_file(e):
    file_list = e.target.files
    first_item = file_list.item(0)

    my_bytes: bytes = await get_bytes_from_file(first_item)
    #print(my_bytes[:10]) # Do something with file contents
    html = docx_to_html(my_bytes)
    #print(html)

async def get_bytes_from_file(file):
    array_buf = await file.arrayBuffer()
    return array_buf.to_bytes()


def parse_docx(jsObject):
    print("PS jsObject", dir(jsObject))
    
    
    bytes = jsObject.to_bytes()
    return docx_to_html(bytes)
 
window.PCH_parse_docx = parse_docx
