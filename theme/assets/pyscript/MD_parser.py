from markdown2 import Markdown


def md_to_html(jsObject)->str:

    bytes = jsObject.to_bytes()

    markdowner = Markdown()
   
    markdown_text = bytes.decode('utf-8')

    html = markdowner.convert(markdown_text)

    return html