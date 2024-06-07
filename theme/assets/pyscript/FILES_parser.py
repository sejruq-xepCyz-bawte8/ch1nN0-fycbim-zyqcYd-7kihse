from js import window, document
from markdown2 import Markdown
import zipfile
from io import BytesIO
import xml.etree.ElementTree as ET

def confirm_loading():
    element = document.querySelector('#appGoesHere > div')
    window.anvil.call(element, "FILES_parser_loaded", 'this')


def expose_to_anvil():
    window.MD_parser = md_to_html
    window.DOCX_parser = docx_to_html


def docx_to_html(jsObject)->str:
    bytes = jsObject.to_bytes()

    with zipfile.ZipFile(BytesIO(bytes)) as docx:
        # Read the document.xml file from the docx zip archive
        xml_content = docx.read('word/document.xml')

    # Parse the XML content
    root = ET.fromstring(xml_content)

    # Namespaces used in the XML
    namespaces = {
        'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
    }

    # Start HTML content
    html_content = ""

    # Extract paragraphs and handle different styles
    for paragraph in root.findall('.//w:p', namespaces):
        # Determine the style of the paragraph
        p_style = paragraph.find('.//w:pStyle', namespaces)
        if p_style is not None:
            style = p_style.attrib.get(f'{{{namespaces["w"]}}}val')
        else:
            style = None

        if style and style.startswith('Heading'):
            level = style[-1]
            try:
                level = int(level)  # Ensure it's a valid number
                html_content += f"<h{level}>"
                for run in paragraph.findall('.//w:r', namespaces):
                    text_elements = run.findall('.//w:t', namespaces)
                    for text_elem in text_elements:
                        if text_elem.text:
                            html_content += text_elem.text
                html_content += f"</h{level}>"
            except ValueError:
                # If the style is not a valid heading level, treat it as h1
                html_content += "<h1>"
                for run in paragraph.findall('.//w:r', namespaces):
                    text_elements = run.findall('.//w:t', namespaces)
                    for text_elem in text_elements:
                        if text_elem.text:
                            html_content += text_elem.text
                html_content += "</h1>"
        else:
            html_content += "<p>"
            for run in paragraph.findall('.//w:r', namespaces):
                text_elements = run.findall('.//w:t', namespaces)
                for text_elem in text_elements:
                    if text_elem.text:
                        html_content += text_elem.text
            html_content += "</p>"

    return html_content

def md_to_html(jsObject)->str:
    bytes = jsObject.to_bytes()
    markdowner = Markdown()
    markdown_text = bytes.decode('utf-8')
    html = markdowner.convert(markdown_text)
    return html


if __name__=="__main__":
    expose_to_anvil()
    confirm_loading()