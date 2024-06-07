import fitz  # PyMuPDF
from js import window

def parse_from_anvil(jsObject):
    bytes = jsObject.to_bytes()
    return extract_text_with_headings(bytes)




def extract_text_with_headings(pdf_bytes):
    document = fitz.open(stream=pdf_bytes, filetype="pdf")
    extracted_text = []

    for page_num in range(len(document)):
        page = document.load_page(page_num)
        blocks = page.get_text("dict")["blocks"]

        for block in blocks:
            if "lines" in block:
                for line in block["lines"]:
                    text = " ".join(span["text"] for span in line["spans"])
                    font_size = line["spans"][0]["size"]

                    # Assuming a heading has a larger font size
                    if font_size > 12:  # Adjust this threshold based on your PDF's formatting
                        extracted_text.append(f"\n\n# {text}\n")
                    else:
                        extracted_text.append(text)
        
    return "\n".join(extracted_text)



window.PDF_parser = parse_from_anvil