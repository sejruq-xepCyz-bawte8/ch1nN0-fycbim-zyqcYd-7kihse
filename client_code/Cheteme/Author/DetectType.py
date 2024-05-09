import re
def parse_type(html: str) -> dict:
    print(html)
    pattern_prose = r'[.!?\'"]<\/p>'
    pattern_poetry = r'[^.!?\'">]<\/p>'
    p_poetry = len(re.findall(pattern_poetry, html, re.MULTILINE))
    p_prose = len(re.findall(pattern_prose, html, re.MULTILINE))
    paragraphs  = p_prose + p_poetry
    if paragraphs == 0 :
        paragraphs = 1
    is_prose = p_prose / paragraphs
    
    if is_prose > 0.5:
        return {'type': 'prose', 'paragraphs': paragraphs}
    else:
        return {'type': 'poetry', 'paragraphs': paragraphs}

    


if __name__ == "__main__":
    html = "<p>dsf sdf </p><p>sdf sdf sd f,</p><p>.</p><p>asdas </p><p>asd.</p>"
    print(parse_type(html))